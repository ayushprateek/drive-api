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

        # --- BOOLEAN HANDLING (FIXED) ---
        show_val = str(data.get('show', 'true')).lower() == 'true'
        open_now_val = str(data.get('open_now', 'false')).lower() == 'true'

        # --- JSON FIELD HANDLING (FIXED) ---
        reviews_data = json.loads(data.get('reviews', '[]'))
        
        # --- CREATE SITE INSTANCE (ALL FIXES APPLIED) ---
        site = Site.objects.create(
            # Required fields
            name=data.get('name'),
            category=category,
            city=city,
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),

            # Optional Text/URL fields with .get() for safety
            place_id=data.get('place_id'),
            property_id=data.get('property_id'),
            description=data.get('description'),
            cover_image=data.get('cover_image'), # From manual URL input
            address=data.get('address'),
            icon=iconPath, # Use the safely initialized iconPath
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
            
            # Numeric fields handled safely
            ad_status=to_num(data.get('ad_status', 0)),
            rating=to_num(data.get('rating')),
            user_ratings_total=to_num(data.get('user_ratings_total')),
            start_price=to_num(data.get('start_price')),
            end_price=to_num(data.get('end_price')),

            # Date fields
            event_start_date=data.get('event_start_date') or None,
            event_end_date=data.get('event_end_date') or None,

            # Boolean fields handled safely
            show=show_val,
            open_now=open_now_val,
            
            # JSON fields loaded correctly
            contact_info=json.loads(data.get('contact_info', '{}')),
            check_in_data=json.loads(data.get('check_in_data', '{}')),
            amenities=json.loads(data.get('amenities', '{}')),
            service_amenities=json.loads(data.get('service_amenities', '{}')),
            policy=json.loads(data.get('policy', '{}')),
            meta_data=json.loads(data.get('meta_data', '{}')),
            regular_opening_hours=json.loads(data.get('regular_opening_hours', '{}')),
            regular_secondary_opening_hours=json.loads(data.get('regular_secondary_opening_hours', '[]')),
            # NOTE: The main `reviews` field is removed from here as we process it into PlaceReview below
        )

        # --- ADD M2M RELATIONSHIPS ---
        site.photos.add(*photo_objs) # More efficient way to add M2M objects

        for review in reviews_data:
            # Skip empty review objects sent from the frontend
            if review and (review.get('authorName') or review.get('text')):
                # Safely parse date, provide a default
                publishTime_str = review.get('publishTime')
                publishTime = dateParser(publishTime_str) if publishTime_str else datetime.now()

                review_obj = PlaceReview.objects.create(
                    author_name=review.get('authorName', ''),
                    rating=to_num(review.get('rating')) or 0,
                    text=review.get('text', ''),
                    original_text=review.get('text', ''), # Assuming this is intended
                    publish_time=publishTime,
                    # Add defaults for other fields if necessary
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
        site_id = data.get('id')

        if not site_id:
            return Response({"error": "Site ID ('id') is required for an update."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the main object to update inside the try block
        site = Site.objects.get(id=site_id)

        # A helper function to safely convert potential empty strings to None for numeric fields
        def to_num(val):
            if val is None or val == '':
                return None
            try:
                # Attempt to convert to float or int
                return float(val) if '.' in str(val) else int(val)
            except (ValueError, TypeError):
                return None

        # --- FILE HANDLING: ICON ---
        iconPath = site.icon  # Start with the existing icon path
        icon_file = request.FILES.get('icon')
        if icon_file:
            # If a new icon is uploaded, delete the old file if it exists
            if site.icon and os.path.exists(os.path.join(settings.BASE_DIR, site.icon)):
                delete_file(os.path.join(settings.BASE_DIR, site.icon))
            iconPath = save_file(icon_file, 'static/icon')
            print("New iconPath =", iconPath)

        # --- FILE HANDLING: PHOTOS (M2M) ---
        
        # 1. Delete images marked for deletion
        delete_images_ids = json.loads(data.get('delete_images', '[]'))
        if delete_images_ids:
            photos_to_delete = site.photos.filter(id__in=delete_images_ids)
            print("photos_to_delete =", photos_to_delete)
            for photo in photos_to_delete:
                if photo.static:
                    file_path = os.path.join(settings.BASE_DIR, photo.static)
                    delete_file(file_path)
            # This deletes the Photo objects and removes the M2M relationship
            photos_to_delete.delete()

        # 2. Add newly uploaded images
        photo_objs = []
        uploaded_files = request.FILES.getlist('images')
        print("New image length =", len(uploaded_files))
        for uploaded_file in uploaded_files:
            imagePath = save_file(uploaded_file, 'static/site')
            print("New imagePath =", imagePath)
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
        # Only fetch new objects if their IDs are provided in the request
        category = Category.objects.get(id=data.get('category_id')) if 'category_id' in data else site.category
        city = City.objects.get(id=data.get('city_id')) if 'city_id' in data else site.city

        # --- BOOLEAN HANDLING ---
        # Only update boolean if key exists in request data
        if 'show' in data:
            site.show = str(data.get('show')).lower() == 'true'
        if 'open_now' in data:
            site.open_now = str(data.get('open_now')).lower() == 'true'

        # --- M2M HANDLING: REVIEWS (PlaceReview) ---
        # Strategy: Clear existing reviews and add the new set from the request.
        if 'reviews' in data:
            reviews_data = json.loads(data.get('reviews', '[]'))
            
            # Delete old review objects associated with this site
            site.place_review.all().delete()
            
            new_review_objs = []
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
                    new_review_objs.append(review_obj)
            
            # Add the newly created reviews to the site
            if new_review_objs:
                site.place_review.add(*new_review_objs)

        # --- UPDATE SITE INSTANCE FIELDS ---
        
        # Foreign Keys
        site.category = category
        site.city = city
        
        # Required & Optional Text/URL fields with .get(key, existing_value) for safety
        site.name = data.get('name', site.name)
        site.latitude = data.get('latitude', site.latitude)
        site.longitude = data.get('longitude', site.longitude)
        site.place_id = data.get('place_id', site.place_id)
        site.property_id = data.get('property_id', site.property_id)
        site.description = data.get('description', site.description)
        site.cover_image = data.get('cover_image', site.cover_image)
        site.address = data.get('address', site.address)
        site.icon = iconPath  # Use the safely handled iconPath
        site.discount_url = data.get('discount_url', site.discount_url)
        site.business_status = data.get('business_status', site.business_status)
        site.icon_background_color = data.get('icon_background_color', site.icon_background_color)
        site.icon_mask_base_uri = data.get('icon_mask_base_uri', site.icon_mask_base_uri)
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
        site.website = data.get('website', site.website)
        site.facility_overview = data.get('facility_overview', site.facility_overview)
        
        # Numeric fields handled safely
        if 'ad_status' in data:
            new_ad_status = to_num(data.get('ad_status'))
            # Only update the field if the new value is a valid number (not None).
            # This prevents overwriting a valid status with None.
            if new_ad_status is not None:
                site.ad_status = new_ad_status
        
        # The logic for other nullable numeric fields is okay, but can also be hardened
        if 'rating' in data:
             new_rating = to_num(data.get('rating'))
             if new_rating is not None:
                site.rating = new_rating

        if 'user_ratings_total' in data:
            new_total = to_num(data.get('user_ratings_total'))
            if new_total is not None:
                site.user_ratings_total = new_total

        if 'start_price' in data:
            new_price = to_num(data.get('start_price'))
            if new_price is not None:
                site.start_price = new_price

        if 'end_price' in data:
            new_price = to_num(data.get('end_price'))
            if new_price is not None:
                site.end_price = new_price

        # Date fields (set to None if empty string is passed)
        if 'event_start_date' in data: site.event_start_date = data.get('event_start_date') or None
        if 'event_end_date' in data: site.event_end_date = data.get('event_end_date') or None
        
        # JSON fields loaded correctly
        json_field_defaults = {
            'contact_info': '{}', 'check_in_data': '{}', 'amenities': '{}',
            'service_amenities': '{}', 'policy': '{}', 'meta_data': '{}',
            'regular_opening_hours': '{}', 'regular_secondary_opening_hours': '[]'
        }
        for field, default in json_field_defaults.items():
            if field in data:
                setattr(site, field, json.loads(data.get(field, default)))

        # Save the updated site instance before adding M2M relationships
        site.save()

        # Add new photos to the M2M relationship
        if photo_objs:
            site.photos.add(*photo_objs)

        return Response({"message": "Site updated successfully", "site_id": site.id}, status=status.HTTP_200_OK)

    except (Site.DoesNotExist, Category.DoesNotExist, City.DoesNotExist):
        return Response({"error": "Invalid ID provided for site, category, or city."}, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON data provided for one of the fields."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Exception raised in updateSite =", str(e))
        import traceback
        traceback.print_exc() # For more detailed logs
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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