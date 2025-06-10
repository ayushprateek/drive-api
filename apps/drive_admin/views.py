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
from apps.trip.models import City,Category, Keyword, Site
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
            lat_long=tempData.get('lat_long', []),
            scrape=bool(int(tempData.get('scrape', 0)))
        )

            return JsonResponse({
                'message': 'City created successfully',
                'city': model_to_dict(city)
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
        cities = City.objects.all().order_by('-created_at')

        paginator = CustomPagination()
        # paginator.page_size = 10  # Default page size, can be customized or read from query param

        paginated_cities = paginator.paginate_queryset(cities, request)
        cities_list = []
        for city in paginated_cities:
            city_dict = model_to_dict(city)
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

        return JsonResponse({
            'message': 'City updated successfully',
            'city': model_to_dict(city)
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
            keyword_objs = Keyword.objects.filter(id__in=keywords_list)
            category.keywords_relation.set(keyword_objs)

        return JsonResponse({
            'message': 'Category created successfully',
            'category': model_to_dict(category)
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
        categories = Category.objects.all().order_by('-created_at')
        paginator = CustomPagination()
        # paginated_sites = paginator.paginate_queryset(sites, request)

        # paginator = PageNumberPagination()
        # paginator.page_size = 10  # You can customize page size here or read from query param

        paginated_categories = paginator.paginate_queryset(categories, request)
        categories_list = []
        for category in paginated_categories:
            cat_dict = model_to_dict(category)
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
            keyword_list = [kw.strip() for kw in tempData.get('keywords').split(',') if kw.strip()]
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

        return JsonResponse({
            'message': 'Category updated successfully',
            'category': model_to_dict(category)
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

@api_view(['GET'])
@authentication_classes([AdminTokenAuthentication])
@permission_classes([IsAuthenticatedAdmin])
def getSite(request,id):
    try:
        site_instance = Site.objects.filter(id=id, show=True).annotate(icon_url=F('category__icon_url')).first()
        if site_instance:
            return JsonResponse({'id': site_instance.id,
                                'name': site_instance.name,
                                 'description': site_instance.description,
                                 'place_id': site_instance.place_id,
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