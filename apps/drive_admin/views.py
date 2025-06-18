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
from apps.trip.models import City,Category, Country, Keyword, Photo, Site
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
            lat_long=tempData.get('lat_long', []),
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
        # Fetch and validate foreign keys
        category = Category.objects.get(id=data.get('category_id'))
        city = City.objects.get(id=data.get('city_id'))

        # Create Photo instances from uploaded files
        photo_objs = []
        uploaded_files = request.FILES.getlist('images')
        print("Image length = ",len(uploaded_files))
        

        for uploaded_file in uploaded_files:
            imagePath = save_file(uploaded_file, 'static/site')
            print("imagePath = ",imagePath)

            # Create Photo object
            photo = Photo.objects.create(
                height=0,
                width=0,
                html_attributions='',
                photo_reference='',
                photo_name='',
                static=imagePath,
            )
            photo_objs.append(photo)

        # Create the Site instance
        site = Site.objects.create(
            place_id=data.get('place_id'),
            property_id=data.get('property_id'),
            ad_status=data.get('ad_status', 0),
            category=category,
            name=data.get('name'),
            city=city,
            description=data.get('description'),
            contact_info=data.get('contact_info', {}),
            check_in_data=data.get('check_in_data', {}),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            reviews=data.get('reviews', {}),
            amenities=data.get('amenities', {}),
            service_amenities=data.get('service_amenities', {}),
            facility_overview=data.get('facility_overview'),
            policy=data.get('policy', {}),
            meta_data=data.get('meta_data', {}),
            cover_image=data.get('cover_image'),
            images=data.getlist('image_urls', []),  # optional pre-existing image URLs
            address=data.get('address'),
            rating=data.get('rating', 0),
            user_ratings_total=data.get('user_ratings_total', 0),
            start_price=data.get('start_price'),
            end_price=data.get('end_price'),
            icon=data.get('icon'),
            discount_url=data.get('discount_url'),
            business_status=data.get('business_status'),
            icon_background_color=data.get('icon_background_color'),
            icon_mask_base_uri=data.get('icon_mask_base_uri'),
            open_now=data.get('open_now', False),
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
            show=data.get('show', True),
            event_start_date=data.get('event_start_date'),
            event_end_date=data.get('event_end_date'),
            website=data.get('website'),
            regular_opening_hours=data.get('regular_opening_hours', {}),
            regular_secondary_opening_hours=data.get('regular_secondary_opening_hours', {}),
        )

        # Add photos to site
        for photo in photo_objs:
            site.photos.add(photo)

        return Response({"message": "Site created successfully", "site_id": site.id}, status=status.HTTP_201_CREATED)

    except Category.DoesNotExist:
        return Response({"error": "Invalid category_id"}, status=status.HTTP_400_BAD_REQUEST)
    except City.DoesNotExist:
        return Response({"error": "Invalid city_id"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
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

        # Basic fields
        site.place_id = data.get('place_id', site.place_id)
        site.property_id = data.get('property_id', site.property_id)
        site.ad_status = data.get('ad_status', site.ad_status)
        site.category = category
        site.name = data.get('name', site.name)
        site.city = city
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
        site.icon = data.get('icon', site.icon)
        site.discount_url = data.get('discount_url', site.discount_url)
        site.business_status = data.get('business_status', site.business_status)
        site.icon_background_color = data.get('icon_background_color', site.icon_background_color)
        site.icon_mask_base_uri = data.get('icon_mask_base_uri', site.icon_mask_base_uri)
        site.open_now = data.get('open_now', site.open_now)
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
        site.show = data.get('show', site.show)
        site.event_start_date = data.get('event_start_date', site.event_start_date)
        site.event_end_date = data.get('event_end_date', site.event_end_date)
        site.website = data.get('website', site.website)

        # Parse JSON fields
        json_fields = [
            'contact_info', 'check_in_data', 'reviews', 'amenities',
            'service_amenities', 'policy', 'meta_data',
            'regular_opening_hours', 'regular_secondary_opening_hours'
        ]
        for field in json_fields:
            if field in data:
                try:
                    setattr(site, field, json.loads(data.get(field)))
                except json.JSONDecodeError as e:
                    return Response({f"error": f"Invalid JSON for {field}: {str(e)}"}, status=400)

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
        'name'
    ).order_by('name')

        return JsonResponse({
            'message': 'Cities & Categories retrieved successfully',
            'cities': list(cities),
            'countries': list(countries),
        }, safe=False, status=status.HTTP_200_OK)
    except Exception as ex:
        print("Error in getAllCities:", ex)
        return Response({'error': str(ex)}, status=500)