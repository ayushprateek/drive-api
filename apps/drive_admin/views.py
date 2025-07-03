from copy import deepcopy
from datetime import datetime
from email import parser
from dateutil import parser as dateParser
import json
from django.db.models import F, Q
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
from django.forms import model_to_dict
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import os
import time
from apps.drive_admin.authentication import AdminTokenAuthentication
from apps.drive_admin.serializers import AdminLoginSerializer
from apps.trip.models import City,Category, Country, Keyword, Photo, PlaceReview, Site
from common import constants
from apps.trip.views import CustomPagination

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdminModel
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .middleware import IsAuthenticatedAdmin

class AdminOnlyView(APIView):
    authentication_classes = [AdminTokenAuthentication]  # Only use your custom admin auth
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request):
        # Your logic here
        return Response({"message": f"Hello Admin {request.user.username}"})

class SomeDriveAdminView(APIView):
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request):
        return Response({"message": "This is a secure drive-admin endpoint."})

class AdminLoginAPIView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        try:
            admin = AdminModel.objects.get(username=username)
        except AdminModel.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        if not admin.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        token = admin.tokens()
        return Response({'token': token})

class AdminRegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        username = data.get("username")
        name = data.get("name")
        password = data.get("password")

        if AdminModel.objects.filter(username=username).exists():
            return Response({
                "success": False,
                "code": 400,
                "message": "Admin already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        admin = AdminModel.objects.create_admin(username=username, name=name, password=password)
        tokens = admin.tokens()
        return Response({
            "success": True,
            "code": 200,
            "data": {
                "message": "User Logged In Successfully!",
                **tokens
            }
        })


@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def checkAdminAPI(request):
    return JsonResponse({
            'message': 'Running'})

def save_file(file, folder):
            timestamp = int(time.time())
            base, ext = os.path.splitext(file.name)
            filename = f"{base}_{timestamp}{ext}"
            dir_path = os.path.join(settings.BASE_DIR, folder)
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, filename)
            with open(file_path, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            return os.path.join(folder, filename)

def delete_file(file_path):
    file_path = os.path.join(settings.BASE_DIR,file_path)
    if os.path.exists(file_path):
        os.remove(file_path) 
            

@api_view(['POST'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def addCity(request):
        try:
            tempData = request.data
            # Save uploaded 'icon' file if present
            if 'file' in request.FILES and request.FILES['file']:
                imagePath = save_file(request.FILES['file'], 'static/city')
            city = City.objects.create(
            name=tempData.get('name'),
            country=tempData.get('country'),
            latitude=tempData.get('latitude'),
            longitude=tempData.get('longitude'),
            images=[imagePath],
            description=tempData.get('description'),
            lat_long=json.loads(tempData.get('lat_long', [])),
            scrape=bool(int(tempData.get('scrape', 0)))
        )
            city_data = model_to_dict(city)
            city_data['id'] = city.id
        

            return JsonResponse({
                'message': 'City created successfully',
                'city': city_data
            })
        except Exception as ex:
            print('An error occurred:', ex)
            raise ValidationError(str(ex))

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getCity(request, city_id):
    try:
        city = City.objects.filter(id=city_id).first()
        if not city:
            return Response(
                {"error": constants.ApplicationMessages.CITY_DOES_NOT_EXIST},
                status=404
            )

        city_data = model_to_dict(city)
        city_data['id'] = city.id
        return Response({
            "message": "City retrieved successfully",
            "city": city_data
        }, status=200)

    except Exception as ex:
        print("Error in getCity:", ex)
        raise ValidationError(str(ex))

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getAllCities(request):
    try:
        query=request.GET.get('query')
        if query:
            cities = City.objects.filter(
                Q(name__icontains=query)
            ).order_by('-created_at')
        else:
            cities = City.objects.all().order_by('-created_at')
        paginator = CustomPagination()
        paginated_cities = paginator.paginate_queryset(cities, request)
        cities_list = []
        for city in paginated_cities:
            city_dict = model_to_dict(city)
            city_dict['id'] = city.id
            cities_list.append(city_dict)

        return paginator.get_paginated_response({
            'message': 'Cities retrieved successfully',
            'cities': cities_list
        })
    except Exception as ex:
        print("Error in getAllCities:", ex)
        return Response({'error': str(ex)}, status=500)

@api_view(['PUT'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def updateCity(request, city_id):
    try:
        city = City.objects.filter(id=city_id).first()
        if not city:
            return Response(
            constants.ApplicationMessages.CITY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )

        tempData = request.data

        # Update image if present
        if 'file' in request.FILES and request.FILES['file']:
            file_path = save_file(request.FILES['file'], 'static/city')
            city.images = [file_path]

        # Update fields
        city.name = tempData.get('name', city.name)
        city.country = tempData.get('country', city.country)
        city.latitude = tempData.get('latitude', city.latitude)
        city.longitude = tempData.get('longitude', city.longitude)
        city.description = tempData.get('description', city.description)
        city.scrape = bool(int(tempData.get('scrape', int(city.scrape))))

        # Handle lat_long (as JSON string)
        lat_long_data = tempData.get('lat_long')
        if lat_long_data:
            try:
                city.lat_long = json.loads(lat_long_data)
            except Exception:
                raise ValidationError("Invalid 'lat_long' format. Must be JSON list.")

        city.save()
        city_data=model_to_dict(city)
        city_data['id'] = city.id

        return JsonResponse({
            'message': 'City updated successfully',
            'city': city_data
        })

    except Exception as ex:
        print("Error in updateCity:", ex)
        raise ValidationError(str(ex))

@api_view(['DELETE'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def deleteCity(request, city_id):
    try:
        city = City.objects.filter(id=city_id).first()
        if not city:
            return Response(
            constants.ApplicationMessages.CITY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        city.delete()

        return JsonResponse({
            'message': 'City deleted successfully',
            'city_id': city_id
        })

    except Exception as ex:
        print("Error in deleteCity:", ex)
        raise ValidationError(str(ex))
    

@api_view(['POST'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def addCategory(request):
    try:
        tempData = request.data
        iconPath = None
        imagePath = None
        # Save uploaded 'icon' file if present
        if 'icon' in request.FILES and request.FILES['icon']:
            iconPath = save_file(request.FILES['icon'], 'static/category')

        # Save uploaded 'image' file if present
        if 'image' in request.FILES and request.FILES['image']:
            imagePath = save_file(request.FILES['image'], 'static/category')

        # Handle keywords (should be a JSON list of IDs)
        keywords_list = tempData.get('keywords', '[]')
        try:
            keywords_list = json.loads(keywords_list)
        except:
            raise ValidationError("Invalid format for keywords. Should be a JSON list.")

        category = Category.objects.create(
            name=tempData.get('name'),
            icon_url=iconPath,
            image_url=imagePath,
            scrape=bool(int(tempData.get('scrape', 0))),
            route=tempData.get('route'),
            parent_id=tempData.get('parent')
        )

        if keywords_list:
            # keyword_objs = Keyword.objects.filter(id__in=keywords_list)
            # category.keywords_relation.set(keyword_objs)
            category.keywords=keywords_list
        category_data = model_to_dict(category)
        category_data['id'] = category.id

        return JsonResponse({
            'message': 'Category created successfully',
            'category': category_data
        })
    except Exception as ex:
        print('An error occurred:', ex)
        raise ValidationError(str(ex))

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getCategory(request, category_id):
    try:
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return Response(
                {"error": constants.ApplicationMessages.CATEGORY_DOES_NOT_EXIST},
                status=404
            )
        
        category_data = model_to_dict(category)

        category_data['keywords_relation'] = list(category.keywords_relation.values_list('id', flat=True))
        category_data['id'] = category.id

        return Response({
            "message": "Category retrieved successfully",
            "category": category_data
        }, status=200)
    except Exception as ex:
        print("Error in getCategory:", ex)
        raise ValidationError(str(ex))

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getAllCategories(request):
    try:
        query=request.GET.get('query')
        if query:
            categories = Category.objects.filter(
                Q(name__icontains=query)
            ).order_by('-created_at')
        else:
            categories = Category.objects.all().order_by('-created_at')
        paginator = CustomPagination()
        # paginated_sites = paginator.paginate_queryset(sites, request)

        # paginator = PageNumberPagination()
        # paginator.page_size = 10  # You can customize page size here or read from query param

        paginated_categories = paginator.paginate_queryset(categories, request)
        categories_list = []
        for category in paginated_categories:
            cat_dict = model_to_dict(category)
            cat_dict['id'] = category.id
            cat_dict['keywords_relation'] = list(category.keywords_relation.values_list('id', flat=True))
            categories_list.append(cat_dict)

        return paginator.get_paginated_response(categories_list)
    except Exception as ex:
        print("Error in getAllCategories:", ex)
        return Response({'error': str(ex)}, status=500)

@api_view(['PUT'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def updateCategory(request, category_id):
    try:
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return Response(
            constants.ApplicationMessages.CATEGORY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )

        tempData = request.data

        # Save uploaded 'icon' file if present
        if 'icon' in request.FILES and request.FILES['icon']:
            category.icon_url = save_file(request.FILES['icon'], 'static/category')

        # Save uploaded 'image' file if present
        if 'image' in request.FILES and request.FILES['image']:
            category.image_url = save_file(request.FILES['image'], 'static/category')

        # Update fields
        category.name = tempData.get('name', category.name)
        category.route = tempData.get('route', category.route)
        category.scrape = bool(int(tempData.get('scrape', int(category.scrape))))
        
        if 'keywords' in tempData:
            # Expects comma-separated string of keywords
            # print(type(json.loads(tempData.get('keywords'))))
            # print(type(tempData.get('keywords')))
            # keyword_list = [kw.strip() for kw in tempData.get('keywords').split(',') if kw.strip()]
            keyword_list = json.loads(tempData.get('keywords'))
            if keyword_list:
                category.keywords = keyword_list

        # Set parent category (optional)
        if 'parent_id' in tempData and tempData.get('parent_id'):
            parent = Category.objects.filter(id=tempData.get('parent_id')).first()
            if parent:
                category.parent = parent
        else:
            category.parent=None
        category.save()
        category_data=model_to_dict(category)
        category_data['id']=category.id

        return JsonResponse({
            'message': 'Category updated successfully',
            'category': category_data
        })

    except Exception as ex:
        print("Error in updateCategory:", ex)
        raise ValidationError(str(ex))

@api_view(['DELETE'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def deleteCategory(request, category_id):
    try:
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return Response(
            constants.ApplicationMessages.CATEGORY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        category.delete()

        return JsonResponse({
            'message': 'Category deleted successfully',
            'category_id': category_id
        })

    except Exception as ex:
        print("Error in deleteCity:", ex)
        raise ValidationError(str(ex))

# def collect_missing_keys(reference, user_input, prefix=""):
#     missing = {}
    
#     for key in reference:
#         full_key = f"{prefix}.{key}" if prefix else key

#         if key not in user_input:
#             missing[key] = reference[key]
#         else:
#             # If both values are dicts, check recursively
#             if isinstance(reference[key], dict) and isinstance(user_input[key], dict):
#                 nested_missing = collect_missing_keys(reference[key], user_input[key])
#                 if nested_missing:
#                     missing[key] = nested_missing
#             # If both values are lists, we skip inner element validation (optional)
#             elif isinstance(reference[key], list) and isinstance(user_input[key], list):
#                 continue  # You can optionally validate the structure of list items too
#     return missing

def collect_missing_keys(reference, user_input, prefix=""):
    missing = {}

    for key in reference:
        full_key = f"{prefix}.{key}" if prefix else key

        if key not in user_input:
            missing[key] = reference[key]
        else:
            # If both values are dicts, check recursively
            if isinstance(reference[key], dict) and isinstance(user_input[key], dict):
                nested_missing = collect_missing_keys(reference[key], user_input[key])
                if nested_missing:
                    missing[key] = nested_missing
            # If both values are lists, we skip inner element validation (optional)
            elif isinstance(reference[key], list) and isinstance(user_input[key], list) and len(reference[key]) !=0 and len(user_input[key]) != 0 and isinstance(reference[key][0], dict) and isinstance(user_input[key][0], dict):
                print("key = ",reference[key])
                nested_missing = collect_missing_keys(reference[key][0], user_input[key][0])
                if nested_missing:
                    missing[key] = nested_missing
                # continue  # You can optionally validate the structure of list items too
    return missing

# @api_view(['POST'])
# @authentication_classes([AdminTokenAuthentication])
# @permission_classes([IsAuthenticatedAdmin])
# def addSite(request):
#     # print("Data = ",request.data.get('amenities', '{}'))
#     # print("Data = ",json.loads(request.data.get('amenities', '{}')))
#     # return Response({"message": "Site created successfully"}, status=status.HTTP_201_CREATED)
#     reference={
#     "place_id": "",
#     "property_id": "",
#     "ad_status": 1,
#     "category_id": "",
#     "name": "",
#     "city_id": "",
#     "description": "",
#     "contact_info": {
#         "nationalPhoneNumber": "",
#         "internationalPhoneNumber": ""
#     },
#     "check_in_data": {
#         "minAge": 0,
#         "checkInTime": "",
#         "checkOutTime": "",
#         "specialInstructions": ""
#     },
#     "latitude": 0.0,
#     "longitude": 0.0,
#     "reviews": [
#         {
#             "text": "Amazing stay, wonderful staff and beautiful location!",
#             "rating": 5,
#             "authorName": "Jane Doe",
#             "relativeTimeDescription": "2 weeks ago"
#         },
#         {
#             "text": "Great location, but the room was a bit small.",
#             "rating": 4,
#             "authorName": "John Smith",
#             "relativeTimeDescription": "1 month ago"
#         }
#     ],
#     "amenities": {
#         "allowsDogs": False,
#         "paymentOptions": {
#             "acceptsNfc": False,
#             "acceptsCashOnly": False,
#             "acceptsDebitCards": True,
#             "acceptsCreditCards": True
#         },
#         "goodForChildren": True
#     },
#     "service_amenities": {
#         "roomService": "",
#         "laundry": "",
#         "concierge": True,
#         "airportShuttle": {
#             "available": True,
#             "fee": ""
#         }
#     },
#     "facility_overview": "",
#     "policy": {
#         "pets": "",
#         "smoking": "",
#         "cancellation": ""
#     },
#     "meta_data": {
#         "seoTitle": "",
#         "internalTag": "",
#         "seoKeywords": "",
#         "seoDescription": ""
#     },
#     "vicinity": "",
#     "rating": 0.0,
#     "user_ratings_total": 0,
#     "start_price": 0,
#     "end_price": 0,
#     "discount_url": "",
#     "business_status": "",
#     "icon_background_color": "",
#     "icon_mask_base_uri": "",
#     "open_now": True,
#     "reference": "",
#     "scope": "",
#     "facility": "",
#     "types": "",
#     "keyword": "",
#     "rate_pretty": "",
#     "rate_type": "",
#     "slug": "",
#     "city_anchor": "",
#     "show": True,
#     "event_start_date": "2025-12-01T10:00:00Z",
#     "event_end_date": "2025-12-01T10:00:00Z",
#     "website": "",
#     "regular_opening_hours": {
#         "openNow": False,
#         "periods": [
#             {
#                 "open": {
#                     "day": 0,
#                     "hour": 11,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 0,
#                     "hour": 19,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 1,
#                     "hour": 14,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 1,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 2,
#                     "hour": 14,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 2,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 3,
#                     "hour": 14,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 3,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 4,
#                     "hour": 14,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 4,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 5,
#                     "hour": 14,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 5,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 6,
#                     "hour": 10,
#                     "minute": 30
#                 },
#                 "close": {
#                     "day": 6,
#                     "hour": 21,
#                     "minute": 0
#                 }
#             }
#         ],
#         "nextOpenTime": "2025-01-05T16:00:00Z",
#         "weekdayDescriptions": [
#             "Monday: 2:00 – 9:00\u202fPM",
#             "Tuesday: 2:00 – 9:00\u202fPM",
#             "Wednesday: 2:00 – 9:00\u202fPM",
#             "Thursday: 2:00 – 9:00\u202fPM",
#             "Friday: 2:00 – 9:00\u202fPM",
#             "Saturday: 10:30\u202fAM – 9:00\u202fPM",
#             "Sunday: 11:00\u202fAM – 7:00\u202fPM"
#         ]
#     },
#     "regular_secondary_opening_hours": [
#         {
#             "openNow": False,
#             "periods": [
#                 {
#                     "open": {
#                         "day": 0,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 0,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 1,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 1,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 2,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 2,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 3,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 3,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 4,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 4,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 5,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 5,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 },
#                 {
#                     "open": {
#                         "day": 6,
#                         "hour": 9,
#                         "minute": 0
#                     },
#                     "close": {
#                         "day": 6,
#                         "hour": 22,
#                         "minute": 0
#                     }
#                 }
#             ],
#             "nextOpenTime": "2025-01-05T14:00:00Z",
#             "secondaryHoursType": "ONLINE_SERVICE_HOURS",
#             "weekdayDescriptions": [
#                 "Monday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Tuesday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Wednesday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Thursday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Friday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Saturday: 9:00\u202fAM – 10:00\u202fPM",
#                 "Sunday: 9:00\u202fAM – 10:00\u202fPM"
#             ]
#         }
#     ]
# }

#     try:
#         l=[
#             "contact_info",
#             "check_in_data",
#             "amenities",
#             "service_amenities",
#             "policy",
#             "meta_data",
#             "regular_opening_hours",
#             "reviews",
#             "regular_secondary_opening_hours",
#          ]
#         l2=[]
#         data = deepcopy(request.data)
#         print(data)
#         for key in l:
#             if key not in data:
#                 l2.append(key)
#         if l2:
#             return Response({"message": "Fields does not exists",
#                              "fields": list(l2),}, status=status.HTTP_206_PARTIAL_CONTENT)
#         for key in l:
#             if not isinstance(data[key],dict):
#                 data[key]=json.loads(data[key])
#         print(data)
#         missing_keys=collect_missing_keys(reference,data)
#         if missing_keys:
#             return Response({
#                 "message":"The following fields are missing in the input JSON:",
#                 "keys":missing_keys,
#                 }, status=status.HTTP_201_CREATED)
#         # return Response({"message": "Site created successfully"}, status=status.HTTP_201_CREATED)
        

#         # Fetch and validate foreign keys
#         category = Category.objects.get(id=data.get('category_id'))
#         city = City.objects.get(id=data.get('city_id'))

#         # Create Photo instances from uploaded files
#         photo_objs = []
#         uploaded_files = request.FILES.getlist('images')
#         uploaded_icon_files = request.FILES.getlist('icon')
#         print("Image length = ",len(uploaded_files))
        

#         for icon in uploaded_icon_files:
#             iconPath = save_file(icon, 'static/icon')
#             print("iconPath = ",iconPath)
        
        
#         for uploaded_file in uploaded_files:
#             imagePath = save_file(uploaded_file, 'static/site')
#             print("imagePath = ",imagePath)

#             # Create Photo object
#             photo = Photo.objects.create(
#                 height=0,
#                 width=0,
#                 html_attributions='',
#                 photo_reference='',
#                 photo_name='',
#                 static=imagePath,
#             )
#             photo_objs.append(photo)

        

#         # Create the Site instance
#         site = Site.objects.create(
#             place_id=data.get('place_id'),
#             property_id=data.get('property_id'),
#             ad_status=data.get('ad_status', 0),
#             category=category,
#             name=data.get('name'),
#             city=city,
#             description=data.get('description'),
#             contact_info=data.get('contact_info', {}),
#             check_in_data=data.get('check_in_data', {}),
#             latitude=data.get('latitude'),
#             longitude=data.get('longitude'),
#             reviews=data.get('reviews', {}),
#             amenities=data.get('amenities', {}),
#             service_amenities=data.get('service_amenities', {}),
#             facility_overview=data.get('facility_overview'),
#             policy=data.get('policy', {}),
#             meta_data=data.get('meta_data', {}),
#             cover_image=data.get('cover_image'),
#             images=data.getlist('image_urls', []),  # optional pre-existing image URLs
#             address=data.get('address'),
#             rating=data.get('rating', 0),
#             user_ratings_total=data.get('user_ratings_total', 0),
#             start_price=data.get('start_price'),
#             end_price=data.get('end_price'),
#             icon=iconPath,
#             discount_url=data.get('discount_url'),
#             business_status=data.get('business_status'),
#             icon_background_color=data.get('icon_background_color'),
#             icon_mask_base_uri=data.get('icon_mask_base_uri'),
#             open_now=data.get('open_now', False),
#             reference=data.get('reference'),
#             scope=data.get('scope'),
#             facility=data.get('facility'),
#             types=data.get('types'),
#             keyword=data.get('keyword'),
#             vicinity=data.get('vicinity'),
#             rate_pretty=data.get('rate_pretty'),
#             rate_type=data.get('rate_type'),
#             slug=data.get('slug'),
#             city_anchor=data.get('city_anchor'),
#             show=data.get('show', True),
#             event_start_date=data.get('event_start_date'),
#             event_end_date=data.get('event_end_date'),
#             website=data.get('website'),
#             regular_opening_hours=data.get('regular_opening_hours', {}),
#             regular_secondary_opening_hours=data.get('regular_secondary_opening_hours', []),
#         )

#         # Add photos to site
#         for photo in photo_objs:
#             site.photos.add(photo)
#         for review in data.get('reviews', []):
#             if review:
                
#                 if review.get('publishTime'):
#                     publishTime=dateParser.isoparse(review.get('publishTime'))
#                 else:
#                     publishTime=datetime.now()
#                 review_obj = PlaceReview.objects.create(
#                     original_text=review.get('text',0),
#                     rating=review.get('rating',0),
#                     author_name=review.get('authorName',''),
#                     name=review.get('name','Admin'),
#                     text=review.get('text',''),
#                     publish_time=publishTime,
#                     flag_content_uri=review.get('flagContentUri',''),
#                     google_maps_uri=review.get('googleMapsUri',''),
#                 )
#                 site.place_review.add(review_obj)
#         site.save()

#         return Response({"message": "Site created successfully", "site_id": site.id}, status=status.HTTP_201_CREATED)

#     except Category.DoesNotExist:
#         return Response({"error": "Invalid category_id"}, status=status.HTTP_400_BAD_REQUEST)
#     except City.DoesNotExist:
#         return Response({"error": "Invalid city_id"}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         print("Exception raised = ",str(e))
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def addSite(request):
    try:
        data = request.data

        # A helper function to safely convert potential empty strings to None for numeric fields
        def to_num(val):
            if val is None or val == '':
                return None
            return val

        iconPath = None  # Initialize to None
        icon_file = request.FILES.get('icon') # Use .get() for a single optional file
        if icon_file:
            iconPath = save_file(icon_file, 'static/icon')
            print("iconPath =", iconPath)

        photo_objs = []
        uploaded_files = request.FILES.getlist('images')
        print("Image length =", len(uploaded_files))
        
        for uploaded_file in uploaded_files:
            imagePath = save_file(uploaded_file, 'static/site')
            print("imagePath =", imagePath)
            photo = Photo.objects.create(
                height=0,
                width=0,
                html_attributions='',
                photo_reference='',
                photo_name='',
                static=imagePath,
            )
            photo_objs.append(photo)

        # --- FOREIGN KEY VALIDATION ---
        category = Category.objects.get(id=data.get('category_id'))
        city = City.objects.get(id=data.get('city_id'))

        show_val = str(data.get('show', 'true')).lower() == 'true'
        open_now_val = str(data.get('open_now', 'false')).lower() == 'true'

        reviews_data = json.loads(data.get('reviews', '[]'))
        
        site = Site.objects.create(
            name=data.get('name'),
            category=category,
            city=city,
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),

            place_id=data.get('place_id'),
            property_id=data.get('property_id'),
            description=data.get('description'),
            cover_image=data.get('cover_image'),
            address=data.get('address'),
            icon=iconPath, 
            discount_url=data.get('discount_url'),
            business_status=data.get('business_status'),
            icon_background_color=data.get('icon_background_color'),
            icon_mask_base_uri=data.get('icon_mask_base_uri'),
            reference=data.get('reference'),
            scope=data.get('scope'),
            facility=data.get('facility'),
            types=data.get('types'),
            keyword=data.get('keyword'),
            vicinity=data.get('vicinity'),
            rate_pretty=data.get('rate_pretty'),
            rate_type=data.get('rate_type'),
            slug=data.get('slug'),
            city_anchor=data.get('city_anchor'),
            website=data.get('website'),
            facility_overview=data.get('facility_overview'),
            
            ad_status=to_num(data.get('ad_status', 0)),
            rating=to_num(data.get('rating')),
            user_ratings_total=to_num(data.get('user_ratings_total')),
            start_price=to_num(data.get('start_price')),
            end_price=to_num(data.get('end_price')),

            event_start_date=data.get('event_start_date') or None,
            event_end_date=data.get('event_end_date') or None,

            show=show_val,
            open_now=open_now_val,
            
            contact_info=json.loads(data.get('contact_info', '{}')),
            check_in_data=json.loads(data.get('check_in_data', '{}')),
            amenities=json.loads(data.get('amenities', '{}')),
            service_amenities=json.loads(data.get('service_amenities', '{}')),
            policy=json.loads(data.get('policy', '{}')),
            meta_data=json.loads(data.get('meta_data', '{}')),
            regular_opening_hours=json.loads(data.get('regular_opening_hours', '{}')),
            regular_secondary_opening_hours=json.loads(data.get('regular_secondary_opening_hours', '[]')),
        )

        site.photos.add(*photo_objs) 

        for review in reviews_data:
            if review and (review.get('authorName') or review.get('text')):
                publishTime_str = review.get('publishTime')
                publishTime = dateParser(publishTime_str) if publishTime_str else datetime.now()

                review_obj = PlaceReview.objects.create(
                    author_name=review.get('authorName', ''),
                    rating=to_num(review.get('rating')) or 0,
                    text=review.get('text', ''),
                    original_text=review.get('text', ''), 
                    publish_time=publishTime,
                )
                site.place_review.add(review_obj)
        
        return Response({"message": "Site created successfully", "site_id": site.id}, status=status.HTTP_201_CREATED)

    except (Category.DoesNotExist, City.DoesNotExist):
        return Response({"error": "Invalid category_id or city_id"}, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON data provided for one of the fields."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Exception raised =", str(e))
        import traceback
        traceback.print_exc() # For more detailed logs
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 


@api_view(['PUT'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def updateSite(request):
    try:
        data = request.data
        print(data.get('delete_images'))

        if not Site.objects.filter(id=data.get('id')).exists():
            return Response({"error": "Invalid site"}, status=status.HTTP_400_BAD_REQUEST)
        if not Category.objects.filter(id=data.get('category_id')).exists():
            return Response({"error": "Invalid category"}, status=status.HTTP_400_BAD_REQUEST)
        if not City.objects.filter(id=data.get('city_id')).exists():
            return Response({"error": "Invalid city"}, status=status.HTTP_400_BAD_REQUEST)

        site = Site.objects.get(id=data.get('id'))
        category = Category.objects.get(id=data.get('category_id'))
        city = City.objects.get(id=data.get('city_id'))
        delete_images = json.loads(data.get('delete_images', '[]'))
        if delete_images:
            photos_to_delete = site.photos.filter(id__in=delete_images)
            print("photos_to_delete = ",photos_to_delete)
            for photo in photos_to_delete:
                if photo.static:
                    file_path = os.path.join(settings.BASE_DIR, photo.static)
                    delete_file(file_path)
                site.photos.remove(photo)
                photo.delete()  
        
        icon_file = request.FILES.get('icon') # Use .get() for a single optional file
        if icon_file:
            site.icon = save_file(icon_file, 'static/icon')
            print("iconPath =", site.icon)

        # Handle uploaded files
        photo_objs = []
        uploaded_files = request.FILES.getlist('images')
        for uploaded_file in uploaded_files:
            imagePath = save_file(uploaded_file, 'static/site')  # This function should handle file saving
            photo = Photo.objects.create(
                height=0,
                width=0,
                html_attributions='',
                photo_reference='',
                photo_name='',
                static=imagePath,
            )
            photo_objs.append(photo)

        # Parse JSON fields
        json_fields = [
            'contact_info', 
            'check_in_data', 
            'reviews', 
            'amenities',
            'service_amenities', 
            'policy', 
            'meta_data',
            'regular_opening_hours', 
            'regular_secondary_opening_hours',
        ]
        parsed_json_data = {}
        for field in json_fields:
            if field in data:
                try:
                    parsed_json_data[field] = json.loads(data[field])
                except json.JSONDecodeError as e:
                    return Response({f"error": f"Invalid JSON format for {field}: {str(e)}"}, status=400)

        # JSON Fields
        site.contact_info=parsed_json_data.get('contact_info',site.contact_info)
        site.check_in_data=parsed_json_data.get('check_in_data',site.check_in_data)
        site.reviews=parsed_json_data.get('reviews',site.reviews)
        site.amenities=parsed_json_data.get('amenities',site.amenities)
        site.service_amenities=parsed_json_data.get('service_amenities',site.service_amenities)
        site.policy=parsed_json_data.get('policy',site.policy)
        site.meta_data=parsed_json_data.get('meta_data',site.meta_data)
        site.regular_opening_hours=parsed_json_data.get('regular_opening_hours',site.regular_opening_hours)
        site.regular_secondary_opening_hours=parsed_json_data.get('regular_secondary_opening_hours',site.regular_secondary_opening_hours)

        # Basic fields

        site.place_id = data.get('place_id', site.place_id)
        site.property_id = data.get('property_id', site.property_id)
        site.ad_status = data.get('ad_status', site.ad_status)
        site.category = category
        site.name = data.get('name', site.name)
        site.city = city
        
        # site.amenities = data.get('amenities', site.amenities)
        # site.service_amenities = data.get('service_amenities', site.service_amenities)
        site.description = data.get('description', site.description)
        site.latitude = data.get('latitude', site.latitude)
        site.longitude = data.get('longitude', site.longitude)
        site.facility_overview = data.get('facility_overview', site.facility_overview)
        site.cover_image = data.get('cover_image', site.cover_image)
        site.address = data.get('address', site.address)
        site.rating = data.get('rating') or site.rating
        site.user_ratings_total = data.get('user_ratings_total') or site.user_ratings_total
        site.start_price = data.get('start_price', site.start_price)
        site.end_price = data.get('end_price', site.end_price)
        site.discount_url = data.get('discount_url', site.discount_url)
        site.business_status = data.get('business_status', site.business_status)
        site.icon_background_color = data.get('icon_background_color', site.icon_background_color)
        site.icon_mask_base_uri = data.get('icon_mask_base_uri', site.icon_mask_base_uri)
        site.open_now = data.get('open_now', 'false') == 'true'
        site.reference = data.get('reference', site.reference)
        site.scope = data.get('scope', site.scope)
        site.facility = data.get('facility', site.facility)
        site.types = data.get('types', site.types)
        site.keyword = data.get('keyword', site.keyword)
        site.vicinity = data.get('vicinity', site.vicinity)
        site.rate_pretty = data.get('rate_pretty', site.rate_pretty)
        site.rate_type = data.get('rate_type', site.rate_type)
        site.slug = data.get('slug', site.slug)
        site.city_anchor = data.get('city_anchor', site.city_anchor)
        site.show = data.get('show', 'false') == 'true'
        site.event_start_date = data.get('event_start_date', site.event_start_date)
        site.event_end_date = data.get('event_end_date', site.event_end_date)
        site.website = data.get('website', site.website)

        

        # Array field: images
        if 'image_urls' in data:
            try:
                site.images = json.loads(data.get('image_urls'))
            except json.JSONDecodeError as e:
                return Response({"error": f"Invalid image_urls list: {str(e)}"}, status=400)

        # Add new photos
        if photo_objs:
            site.photos.add(*photo_objs)

        site.save()

        return Response({"message": "Site updated successfully", "site_id": site.id}, status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getSite(request,id):
    try:
        site_instance = Site.objects.filter(id=id).annotate(icon_url=F('category__icon_url')).first()
        if site_instance:
            return JsonResponse({'id': site_instance.id,
                                'name': site_instance.name,
                                 'description': site_instance.description,
                                 'place_id': site_instance.place_id,
                                 'property_id': site_instance.property_id,
                                 'city_anchor': site_instance.city_anchor,
                                 'show': site_instance.show,
                                 'open_now': site_instance.open_now,
                                 'ad_status': site_instance.ad_status,
                                 'start_price': site_instance.start_price,
                                 'end_price': site_instance.end_price,
                                 'rate_pretty': site_instance.rate_pretty,
                                 'rate_type': site_instance.rate_type,
                                 'icon_background_color': site_instance.icon_background_color,
                                 'icon_mask_base_uri': site_instance.icon_mask_base_uri,
                                 'cover_image': site_instance.cover_image,
                                 'icon': site_instance.icon,
                                 'scope': site_instance.scope,
                                 'reference': site_instance.reference,
                                 'event_start_date': site_instance.event_start_date,
                                 'event_end_date': site_instance.event_end_date,
                                 'check_in_data': site_instance.check_in_data,
                                 'policy': site_instance.policy,
                                 'meta_data': site_instance.meta_data,
                                 'types': site_instance.types,
                                 'keyword': site_instance.keyword,
                                 'slug': site_instance.slug,
                                 'category_id': site_instance.category.id,
                                 'category_name': site_instance.category.name,
                                 'city_id': site_instance.city.id,
                                 'city_name': site_instance.city.name,
                                 'rating': site_instance.rating,
                                 'user_ratings_total': site_instance.user_ratings_total,
                                 'latitude': site_instance.latitude,
                                 'longitude': site_instance.longitude,
                                 'icon_url': site_instance.category.icon_url if site_instance.category else None,
                                 'photo_reference': list(
                                      site_instance.photos
                                          .filter(photo_reference__isnull=False)
                                          .exclude(photo_reference='')
                                          .values('id', 'photo_reference')
                                  ),
                                  'photo_name': list(
                                      site_instance.photos
                                          .filter(photo_name__isnull=False)
                                          .exclude(photo_name='')
                                          .values('id', 'photo_name')
                                  ),
                                  'url': list(
                                      site_instance.photos
                                          .filter(url__isnull=False)
                                          .exclude(url='')
                                          .values('id', 'url')
                                  ),
                                  'static': list(
                                      site_instance.photos
                                          .filter(static__isnull=False)
                                          .exclude(static='')
                                          .values('id', 'static')
                                  ),
                                 'facility': site_instance.facility,
                                 'amenities': site_instance.amenities,
                                 'service_amenities': site_instance.service_amenities,
                                 'contact_info': site_instance.contact_info,
                                 'vicinity': site_instance.vicinity,
                                 'discount_url': site_instance.discount_url,
                                 'website': site_instance.website,
                                 "regular_opening_hours": site_instance.regular_opening_hours,
                                 "regular_secondary_opening_hours": site_instance.regular_secondary_opening_hours,
                                 'reviews': list(site_instance.place_review.values())
                                 }, safe=False, status=status.HTTP_200_OK)

        else:
            return JsonResponse({"error": "Site does not exist"}, safe=False, status=status.HTTP_200_OK)
    except Exception as ex:
        return JsonResponse({'error': str(ex)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getAllSites(request):
    try:
        query=request.GET.get('query')
        if query:
            sites = Site.objects.filter(
                Q(name__icontains=query)
            ).annotate(icon_url=F('category__icon_url'))
        else:
            sites=Site.objects.annotate(icon_url=F('category__icon_url')).all()
        paginator = CustomPagination()
        paginated_sites = paginator.paginate_queryset(sites, request)
        site_list = []
        for site_instance in paginated_sites:
            site_list.append({'id': site_instance.id,
                                'name': site_instance.name,
                                 'description': site_instance.description,
                                #  'place_id': site_instance.place_id,
                                #  'rating': site_instance.rating,
                                #  'user_ratings_total': site_instance.user_ratings_total,
                                 'latitude': site_instance.latitude,
                                 'longitude': site_instance.longitude,
                                 'icon_url': site_instance.category.icon_url if site_instance.category else None,
                                 'photo_reference': next(iter(site_instance.photos
                                         .filter(photo_reference__isnull=False)
                                         .exclude(photo_reference='')
                                         .values('id', 'photo_reference')), []),
                                 'photo_name': next(iter(site_instance.photos
                                         .filter(photo_name__isnull=False)
                                         .exclude(photo_name='')
                                         .values('id', 'photo_name')), []),
                                 'url': next(iter(site_instance.photos
                                         .filter(url__isnull=False)
                                         .exclude(url='')
                                         .values('id', 'url')), []),
                                 'static': next(iter(site_instance.photos
                                         .filter(static__isnull=False)
                                         .exclude(static='')
                                         .values('id', 'static')), []),
                                #  'facility': site_instance.facility,
                                #  'amenities': site_instance.amenities,
                                #  'service_amenities': site_instance.service_amenities,
                                #  'contact_info': site_instance.contact_info,
                                #  'vicinity': site_instance.vicinity,
                                 'discount_url': site_instance.discount_url,
                                 'website': site_instance.website,
                                #  "regular_opening_hours": site_instance.regular_opening_hours,
                                #  "regular_secondary_opening_hours": site_instance.regular_secondary_opening_hours,
                                #  'reviews': list(site_instance.place_review.values())
                                 })

        return paginator.get_paginated_response({
            'message': 'Cities retrieved successfully',
            'sites': site_list
        })
    except Exception as ex:
        return JsonResponse({'error': str(ex)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getCityAndCategoryList(request):
    try:
        cities = City.objects.all().values(
            'id',
            'name'
        ).order_by('name')
        
        countries = Country.objects.all().values(
        'id',
        'name',
        'iso',
        ).order_by('name')

        categories = Category.objects.all().values(
            'id', 
            'name'
        ).order_by('name') 

        return JsonResponse({
            'message': 'Cities & Categories retrieved successfully',
            'cities': list(cities),
            'countries': list(countries),
            'categories': list(categories)
        }, safe=False, status=status.HTTP_200_OK)
    except Exception as ex:
        print("Error in getAllCities:", ex)
        return Response({'error': str(ex)}, status=500)