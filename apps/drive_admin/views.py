import json
from django.conf import settings
from django.forms import model_to_dict
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import os
import time
from apps.trip.models import City,Category, Keyword
from common import constants
from apps.trip.views import CustomPagination

@api_view(['GET'])
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