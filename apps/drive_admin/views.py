import json
from django.conf import settings
from django.forms import model_to_dict
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.decorators import api_view
import os

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
            if 'file' in request.FILES and bool(request.FILES['file']) == True:
                uploaded_file = request.FILES['file']
                with open(os.path.join(settings.BASE_DIR, 'static/city', uploaded_file.name), 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                imagePath='static/city/{}'.format(uploaded_file.name)
                print("Name of image = ",imagePath)
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


@api_view(['POST'])
def addCategory(request):
    try:
        tempData = request.data
        iconPath = None
        imagePath = None

        # Save uploaded 'icon' file if present
        if 'icon' in request.FILES and request.FILES['icon']:
            uploaded_icon = request.FILES['icon']
            icon_dir = os.path.join(settings.BASE_DIR, 'static/category')
            os.makedirs(icon_dir, exist_ok=True)
            iconPath = f'static/category/{uploaded_icon.name}'
            with open(os.path.join(icon_dir, uploaded_icon.name), 'wb+') as dest:
                for chunk in uploaded_icon.chunks():
                    dest.write(chunk)

        # Save uploaded 'image' file if present
        if 'image' in request.FILES and request.FILES['image']:
            uploaded_image = request.FILES['image']
            image_dir = os.path.join(settings.BASE_DIR, 'static/category')
            os.makedirs(image_dir, exist_ok=True)
            imagePath = f'static/category/{uploaded_image.name}'
            with open(os.path.join(image_dir, uploaded_image.name), 'wb+') as dest:
                for chunk in uploaded_image.chunks():
                    dest.write(chunk)

        # Handle keywords (should be a JSON list)
        keywords_list = tempData.get('keywords', '[]')
        try:
            keywords_list = json.loads(keywords_list)
        except:
            raise ValidationError("Invalid format for keywords. Should be a JSON list.")

        # Create the Category instance
        category = Category.objects.create(
            name=tempData.get('name'),
            icon_url=iconPath,
            image_url=imagePath,
            scrape=bool(int(tempData.get('scrape', 0))),
            route=tempData.get('route'),
            parent_id=tempData.get('parent')
        )

        # Link related Keyword objects
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
        

