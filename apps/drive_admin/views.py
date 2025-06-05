from django.conf import settings
from django.forms import model_to_dict
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.decorators import api_view
import os

from apps.trip.models import City

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
        

