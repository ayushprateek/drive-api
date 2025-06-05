import json
from django.conf import settings
from django.forms import model_to_dict
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.decorators import api_view
import os
import time

from apps.trip.models import City,Category, Keyword

# Create your views here.
@api_view(['GET'])
def checkAdminAPI(request):
    return JsonResponse({
            'message': 'Running'})


@api_view(['POST'])
def addCity(request):
        try:
            tempData = request.data
            # Save uploaded 'icon' file if present
            if 'file' in request.FILES and request.FILES['file']:
                imagePath = save_file(request.FILES['file'], 'static/city')
            # if 'file' in request.FILES and bool(request.FILES['file']) == True:
            #     uploaded_file = request.FILES['file']
            #     with open(os.path.join(settings.BASE_DIR, 'static/city', uploaded_file.name), 'wb+') as destination:
            #         for chunk in uploaded_file.chunks():
            #             destination.write(chunk)
            #     imagePath='static/city/{}'.format(uploaded_file.name)
            #     print("Name of image = ",imagePath)
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
        

