import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from rest_framework.decorators import api_view
import pandas as pd
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.search.models import SearchLog
from apps.user.models import User
from rest_framework.exceptions import ValidationError
from datetime import date
from django.db import models
from django.db import models
from django.db.models import F
from django.db.models.functions import Coalesce

from apps.trip.helper import (
    ModelMap,
    fetch_pois_for_category,
    fetch_pois_save_for_location,
    fetch_pois_save_with_route,
    get_route,
)
from apps.user import (
    serializers as user_serializer,
    models as user_models, schema,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from common import constants, permissions, pagination
from rest_framework.response import Response
from rest_framework import status, parsers, generics
from rest_framework.filters import SearchFilter
from drf_yasg.utils import swagger_auto_schema

from apps.trip.scrape_hotels import ScrapeHotels
from apps.trip.scraping_service import Scrape
from apps.trip.services.common import get_geo_code
from apps.trip.services.fetch_image import scrap_images
from common.permissions import IsSuperAdmin
from common.constants import Constant
from apps.trip import (
    serializers as trip_serializer,
    models as trip_models,
    schema,
    helper,
)
from drive_ai.settings import GOOGLE_API_KEY
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests
from .models import *
from django.conf import settings
from django.db import connection

import requests
import time

import requests
import json
from shapely.geometry import Point, LineString,box
import math
from drive_ai import settings


def printRoot(request):
    print(settings.STATIC_ROOT+'Temp.png')
    print(settings.STATIC_URL)
    
    Category.objects.create(
    name='Experiences',
    image_url='static/Experiences.jpeg',
    icon_url='static/Experiences.jpeg'
    )
    Category.objects.create(
    name='Experiences',
    image_url='static/Experiences.jpeg',
    icon_url='static/Experiences.jpeg'
    )
    Category.objects.create(
    name='Weird Wacky',
    image_url='static/WeirdWacky.png',
    icon_url='static/WeirdWacky.png'
    )
    Category.objects.create(
    name='Extream Soprts',
    image_url='static/ExtreamSoprts.png',
    icon_url='static/ExtreamSoprts.png'
    )
    Category.objects.create(
    name='Hotel Deals',
    image_url='static/HotelDeals.png',
    icon_url='static/HotelDeals.png'
    )
    Category.objects.create(
    name='National Park',
    image_url='static/NationalPark.png',
    icon_url='static/NationalPark.png'
    )
    Category.objects.create(
    name='Evant Calendar',
    image_url='static/EvantCalendar.png',
    icon_url='static/EvantCalendar.png'
    )
    Category.objects.create(
    name='Historic Sites',
    image_url='static/HistoricSites.png',
    icon_url='static/HistoricSites.png'
    )
    
    return JsonResponse({'message': 'Hotels fetched and saved successfully'})

def cityScrape(request):
    print('cityScrape')
    
    City.objects.create(
        name='Orlando',
        country='US',
        latitude=28.538336,
        longitude=-81.379234,
        images=['static/Orlando.jpeg'],
        description='Orlando is a city in central Florida, known for its theme parks, including Walt Disney World and Universal Studios.'
    )

    City.objects.create(
        name='Tampa',
        country='US',
        latitude=27.950575,
        longitude=-82.457178,
        images=['static/Tampa.jpeg'],
        description='Tampa is a city on Tampa Bay, along Florida’s Gulf Coast. It is known for its museums and other cultural offerings.'
    )

    City.objects.create(
        name='Tallahassee',
        country='US',
        latitude=30.438255,
        longitude=-84.280733,
        images=['static/Tallahassee.jpeg'],
        description='Tallahassee is the capital of the U.S. state of Florida. It is known for its large number of law firms, lobbying organizations, and trade associations.'
    )

    City.objects.create(
        name='St. Petersburg',
        country='US',
        latitude=27.767600,
        longitude=-82.640290,
        images=['static/St_Petersburg.jpeg'],
        description='St. Petersburg is a city on Florida’s Gulf Coast, part of the Tampa Bay area. It is known for its pleasant weather and cultural attractions.'
    )

    City.objects.create(
        name='Fort Lauderdale',
        country='US',
        latitude=26.122439,
        longitude=-80.137317,
        images=['static/Fort_Lauderdale.jpeg'],
        description='Fort Lauderdale is a city on Florida’s southeastern coast, known for its boating canals and stunning beaches.'
    )

    City.objects.create(
        name='Hialeah',
        country='US',
        latitude=25.857596,
        longitude=-80.278105,
        images=['static/Hialeah.jpeg'],
        description='Hialeah is a city in Miami-Dade County, Florida, and a principal city of the Miami metropolitan area.'
    )

    City.objects.create(
        name='Port St. Lucie',
        country='US',
        latitude=27.273049,
        longitude=-80.358226,
        images=['static/Port_St_Lucie.jpeg'],
        description='Port St. Lucie is a city in Florida, known for its beautiful parks, riverfront, and botanical gardens.'
    )

    City.objects.create(
        name='Pembroke Pines',
        country='US',
        latitude=26.007765,
        longitude=-80.296256,
        images=['static/Pembroke_Pines.jpeg'],
        description='Pembroke Pines is a city in southern Broward County, Florida, and a suburb of Miami.'
    )

    # City.objects.create(
    #   name='Miami',
    #   country='US',
    #   latitude=25.761670,
    #   longitude=-80.22534,
    #   images=[statioc/'Miami.jpeg'],
    #   description='Miami, officially the City of Miami, is a coastal city in the U.S. state of Florida and the seat of Miami-Dade County in South Florida'
    # )
    
    # City.objects.create(
    #   name='Jacksonville',
    #   country='US',
    #   latitude=30.387233,
    #   longitude=-81.670820,
    #   images=['static/Jacksonville.jpeg','static/Jacksonville2.jpeg'],
    #   description='Jacksonville is the most populous city proper in the U.S. state of Florida, located on the Atlantic coast of northeastern Florida. It is the seat of Duval County, with which the City of Jacksonville consolidated in 1968. It was the largest city by area in the contiguous United States as of 2020'
    # )
    return JsonResponse({'message': 'City fetched and saved successfully'})


def historicalSitesScrape(request):
    miami=City.objects.filter(id='2089800e-c9b1-439b-a20d-a480ae8d7419').first()
    jacksonville=City.objects.filter(id='f37eb49a-6415-4614-bfa9-6036f8d6f6e0').first()
    HistoricalSite.objects.create(
        name='Vizcaya',
        description='This beautiful estate was built by industrialist James Deering in the early 20th century. It features a stunning Italian Renaissance-style villa',
        images=['Vizcaya.png'],
        city=miami,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    HistoricalSite.objects.create(
        name='Jacksonville',
        description='This beautiful estate was built by industrialist James Deering in the early 20th century. It features a stunning Italian Renaissance-style villa',
        images=['Jacksonville.jpeg'],
        city=jacksonville,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    return JsonResponse({'message': 'HistoricalSite fetched and saved successfully'})


def weird(request):
    miami=City.objects.filter(id='2089800e-c9b1-439b-a20d-a480ae8d7419').first()
    jacksonville=City.objects.filter(id='f37eb49a-6415-4614-bfa9-6036f8d6f6e0').first()
    WeirdAndWacky.objects.create(
        name='Coral Castle',
        description='Chosen TOP 35 out of more than 35,000 Museums in the United States "...guaranteed to be the highlight of...',
        images=['static/WeirdAndWacky1.png'],
        city=miami,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    WeirdAndWacky.objects.create(
        name='Meet The Florida Skunk Ape, The Sunshine State’s Answer To Bigfoot',
        description='The "Swamp Sasquatch" known as the Florida Skunk Ape is a 66, 450...',
        images=['static/WeirdAndWacky2.png'],
        city=miami,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    WeirdAndWacky.objects.create(
        name='Florida 2nd in nation for most UFO sightings',
        description='TAMPA, Fla. (WFLA) – Florida has the second-most reported UFO – or unidentified flying...',
        images=['static/WeirdAndWacky3.png'],
        city=jacksonville,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    
    ExtremeSport.objects.create(
        name='Exotic Indoor Firearm Experience in Miami',
        description='Feel the adrenaline rush of firing a machine gun at an indoor gun range in Miami. Try out the extensive...',
        images=['static/ExtremeSport1.png'],
        city=miami,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    ExtremeSport.objects.create(
        name='Speedboat Sightseeing Tour of Miami',
        description='Speedboat Sightseeing Tour of Miami',
        images=['static/ExtremeSport2.png'],
        city=jacksonville,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    ExtremeSport.objects.create(
        name='Miami Waterlife Tours Biscayne Bay Jet Ski Tour',
        description='See the sights of Miami from the water during this Jet Ski tour along Biscayne Bay. Travel the waters of Biscayn...',
        images=['static/ExtremeSport3.png'],
        city=jacksonville,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    return JsonResponse({'message': 'HistoricalSite fetched and saved successfully'})

@api_view(['POST'])
def likePlace(request):
    print('createPlan called')
    data = json.loads(request.body)
    print(data)
    
    userdata=User.objects.filter(id=data['user_id']).first()
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
    else :
        user_likes = UserLikes.objects.create(user=userdata)
    
    if HistoricalSite.objects.filter(id=data['like_id']).exists():
        historicalsites=HistoricalSite.objects.get(id=data['like_id'])
        user_likes.liked_historicalsites.add(historicalsites)
        return JsonResponse({'message': 'User Liked Historical Site'})
        
    if Hotel.objects.filter(id=data['like_id']).exists():
        hotel = Hotel.objects.get(id=data['like_id'])
        user_likes.liked_hotels.add(hotel)
        return JsonResponse({'message': 'User Liked Hotel'})
        
    if ExtremeSport.objects.filter(id=data['like_id']).exists():
        extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
        user_likes.liked_extremesports.add(extreme_sport)
        return JsonResponse({'message': 'User Liked Extreme Sport'})
        
    if Event.objects.filter(id=data['like_id']).exists():
        event = Event.objects.get(id=data['like_id'])
        user_likes.liked_events.add(event)
        return JsonResponse({'message': 'User Liked Event'})
        
    if WeirdAndWacky.objects.filter(id=data['like_id']).exists():
        weird_and_wacky = WeirdAndWacky.objects.get(id=data['like_id'])
        user_likes.liked_wierdandwacky.add(weird_and_wacky)
        return JsonResponse({'message': 'User Liked Weird And Wacky'})
        
    if Park.objects.filter(id=data['like_id']).exists():
        park = Park.objects.get(id=data['like_id'])
        user_likes.liked_parks.add(park)
        return JsonResponse({'message': 'User Liked Park'})
        
    if Attraction.objects.filter(id=data['like_id']).exists():
        attraction = Attraction.objects.get(id=data['like_id'])
        user_likes.liked_attractions.add(attraction)
        return JsonResponse({'message': 'User Liked Attraction'})
    
    
@api_view(['POST'])
def isPlaceLiked(request):
    data = json.loads(request.body)
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
        if user_likes and user_likes.liked_historicalsites.filter(id=data['like_id']).exists():
            # historicalsites=HistoricalSite.objects.filter(id=data['like_id']).first()
            
            return JsonResponse({'message': 'User Liked Historical Site',
                                 'liked':True})
        
        if user_likes and user_likes.liked_hotels.filter(id=data['like_id']).exists():
            # hotel = Hotel.objects.get(id=data['like_id'])
            # user_likes.liked_hotels.add(hotel)
            return JsonResponse({'message': 'User Liked Hotel',
                                 'liked':True})

        if user_likes and user_likes.liked_extremesports.filter(id=data['like_id']).exists():
            # extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
            # user_likes.liked_extremesports.add(extreme_sport)
            return JsonResponse({'message': 'User Liked Extreme Sport',
                                 'liked':True})

        if user_likes and user_likes.liked_events.filter(id=data['like_id']).exists():
            # event = Event.objects.get(id=data['like_id'])
            # user_likes.liked_events.add(event)
            return JsonResponse({'message': 'User Liked Event',
                                 'liked':True})

        if user_likes and user_likes.liked_wierdandwacky.filter(id=data['like_id']).exists():
            return JsonResponse({'message': 'User Liked Weird And Wacky',
                                 'liked':True})

        if user_likes and user_likes.liked_parks.filter(id=data['like_id']).exists():
            # park = Park.objects.get(id=data['like_id'])
            # user_likes.liked_parks.add(park)
            return JsonResponse({'message': 'User Liked Park','liked':True})

        if user_likes and user_likes.liked_attractions.filter(id=data['like_id']).exists():
            # attraction = Attraction.objects.get(id=data['like_id'])
            # user_likes.liked_attractions.add(attraction)
            return JsonResponse({'message': 'User Liked Attraction','liked':True})
        
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
    else :
        return JsonResponse({
            'message': 'User Did not like',
            'liked':True})
        
@api_view(['POST'])
def unlikePlace(request):
    data = json.loads(request.body)
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
        if user_likes and user_likes.liked_historicalsites.filter(id=data['like_id']).exists():
            historical_site_to_remove = user_likes.liked_historicalsites.filter(id=data['like_id']).first()
            if historical_site_to_remove:
                user_likes.liked_historicalsites.remove(historical_site_to_remove)
            return JsonResponse({'message': 'User Unliked Historical Site',
                                 'liked':False})
        
        if user_likes and user_likes.liked_hotels.filter(id=data['like_id']).exists():
            # hotel = Hotel.objects.get(id=data['like_id'])
            # user_likes.liked_hotels.add(hotel)
            return JsonResponse({'message': 'User Liked Hotel',
                                 'liked':False})

        if user_likes and user_likes.liked_extremesports.filter(id=data['like_id']).exists():
            # extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
            # user_likes.liked_extremesports.add(extreme_sport)
            return JsonResponse({'message': 'User Liked Extreme Sport',
                                 'liked':False})

        if user_likes and user_likes.liked_events.filter(id=data['like_id']).exists():
            # event = Event.objects.get(id=data['like_id'])
            # user_likes.liked_events.add(event)
            return JsonResponse({'message': 'User Liked Event',
                                 'liked':False})

        if user_likes and user_likes.liked_wierdandwacky.filter(id=data['like_id']).exists():
            return JsonResponse({'message': 'User Liked Weird And Wacky',
                                 'liked':False})

        if user_likes and user_likes.liked_parks.filter(id=data['like_id']).exists():
            # park = Park.objects.get(id=data['like_id'])
            # user_likes.liked_parks.add(park)
            return JsonResponse({'message': 'User Liked Park','liked':False})

        if user_likes and user_likes.liked_attractions.filter(id=data['like_id']).exists():
            # attraction = Attraction.objects.get(id=data['like_id'])
            # user_likes.liked_attractions.add(attraction)
            return JsonResponse({'message': 'User Liked Attraction','liked':False})
        
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
    else :
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
    
    
    
    
    
    


@api_view(['POST'])
def createTripPlan(request):
    print('createPlan called')
    data = json.loads(request.body)
    print(data)
    city=City.objects.filter(id=data['city_id']).first()
    user=User.objects.filter(id=data['user_id']).first()
    Plan.objects.create(
    name = data['name'],
    description = data['description'],
    start_date = data['start_date'],
    end_date = data['end_date'],
    city=city,
    user=user,
    created_at=date.today().strftime('%Y-%m-%d %H:%M:%S') 
    )
    return JsonResponse({'message': 'Trip Created'})
@api_view(['POST'])
def getTripPlan(request):
    data = json.loads(request.body)
    plans = Plan.objects.filter(user_id=data['user_id']).select_related('city').values(
        'id', 'name', 'city__id', 'city__name', 'city__images'
    )
    print(len(plans))
    plans_list = list(plans)
    for plan in plans_list:
        plan['city_name'] = plan.pop('city__name')
        plan['city_images'] = plan.pop('city__images')
        plan['city_id'] = plan.pop('city__id')
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getHistoricalsites(request):
    data = json.loads(request.body)
    plans = HistoricalSite.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getWeirdAndWacky(request):
    data = json.loads(request.body)
    plans = WeirdAndWacky.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getExtremeSport(request):
    data = json.loads(request.body)
    plans = ExtremeSport.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)
    # print(data)
    # city=City.objects.filter(id=data['city_id']).first()
    # user=User.objects.filter(id=data['user_id']).first()
    # Plan.objects.create(
    # name = data['name'],
    # description = data['description'],
    # start_date = data['start_date'],
    # end_date = data['end_date'],
    # city=city,
    # user=user,
    # created_at=date.today().strftime('%Y-%m-%d %H:%M:%S') 
    # )
    return JsonResponse({'message': 'Trip Created'})
        
class ScrapeHotelsView(View):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        
        latlang=[
    {"latitude": 30.528997, "longitude": -85.884900},
    {"latitude": 30.467823, "longitude": -85.481728},
    {"latitude": 30.177115, "longitude": -85.285272},
    {"latitude": 30.395227, "longitude": -84.892362},
    {"latitude": 30.346799, "longitude": -84.331061},
    {"latitude": 30.274113, "longitude": -83.853955},
    {"latitude": 30.152850, "longitude": -83.404915},
    {"latitude": 30.201373, "longitude": -83.012004},
    {"latitude": 29.934201, "longitude": -83.124264},
    {"latitude": 29.934201, "longitude": -83.124264},
    {"latitude": 29.644144, "longitude": -82.891468},
    {"latitude": 29.564339, "longitude": -82.570213},
    {"latitude": 29.577644, "longitude": -82.172468},
    {"latitude": 30.438702, "longitude": -82.631404},
    {"latitude": 30.148104, "longitude": -82.524319},
    {"latitude": 30.121644, "longitude": -82.264255},
    {"latitude": 30.174558, "longitude": -81.988894},
    {"latitude": 30.028976, "longitude": -82.203064},
    {"latitude": 29.909704, "longitude": -81.820617},
    {"latitude": 29.577644, "longitude": -81.912404},
    {"latitude": 29.670732, "longitude": -81.637043},
    {"latitude": 29.617549, "longitude": -81.453468},
    {"latitude": 29.497786, "longitude": -81.820617},
    {"latitude": 29.271181, "longitude": -82.019489},
    {"latitude": 29.003942, "longitude": -82.065383},
    {"latitude": 29.271181, "longitude": -81.835915},
    {"latitude": 29.137648, "longitude": -81.499362},
    {"latitude": 29.097555, "longitude": -81.835915},
    {"latitude": 28.896852, "longitude": -81.973596},
    {"latitude": 28.548048, "longitude": -81.988894},
    {"latitude": 28.292419, "longitude": -81.790021},
    {"latitude": 28.157630, "longitude": -81.606447},
    {"latitude": 28.066303, "longitude": -81.422551},
    {"latitude": 28.012578, "longitude": -81.257333},
    {"latitude": 27.951145, "longitude": -81.083420},
    {"latitude": 27.935782, "longitude": -81.379073},
    {"latitude": 27.920416, "longitude": -81.744290},
    {"latitude": 27.527851, "longitude": -81.639942},
    {"latitude": 27.481574, "longitude": -81.909508},
    {"latitude": 27.334902, "longitude": -81.944290},
    {"latitude": 27.303999, "longitude": -82.248638},
    {"latitude": 27.242167, "longitude": -82.074725},
    {"latitude": 27.175862, "longitude": -81.461201},
    {"latitude": 27.189757, "longitude": -81.195667},
    {"latitude": 27.264911, "longitude": -81.067270},
    {"latitude": 27.037494, "longitude": -81.176805},
    {"latitude": 26.796580, "longitude": -81.220619},
    {"latitude": 26.646564, "longitude": -81.206014},
    {"latitude": 26.522489, "longitude": -81.279037},
    {"latitude": 26.378655, "longitude": -81.454292},
    {"latitude": 26.195335, "longitude": -81.498106},
    {"latitude": 26.037974, "longitude": -81.468897},
    {"latitude": 26.051095, "longitude": -81.198712},
    {"latitude": 26.064215, "longitude": -80.957736},
    {"latitude": 26.319763, "longitude": -80.826294},
    {"latitude": 26.260840, "longitude": -80.629132},
    {"latitude": 26.110124, "longitude": -80.497691},
    {"latitude": 25.978909, "longitude": -80.541504},
    {"latitude": 25.840975, "longitude": -80.687551},
    {"latitude": 25.702879, "longitude": -80.745969},
    {"latitude": 25.919814, "longitude": -80.541504},
    {"latitude": 25.722617, "longitude": -80.556109},
    {"latitude": 25.630480, "longitude": -80.753271},
    {"latitude": 25.538271, "longitude": -80.833597},
    {"latitude": 25.426209, "longitude": -80.592621},
    {"latitude": 25.314042, "longitude": -80.541504},
    {"latitude": 25.818571, "longitude": -80.344273},
    {"latitude": 25.920899, "longitude": -80.361579},
    {"latitude": 26.038690, "longitude": -80.378885},
    {"latitude": 26.063122, "longitude": -80.304716},
    {"latitude": 26.158581, "longitude": -80.228075},
    {"latitude": 26.194080, "longitude": -80.186046},
    {"latitude": 26.327422, "longitude": -80.199521},
    {"latitude": 26.452348, "longitude": -80.185849},
    {"latitude": 26.415619, "longitude": -80.150300},
    {"latitude": 26.545343, "longitude": -80.177645},
    {"latitude": 26.689580, "longitude": -80.163973},
    {"latitude": 26.779940, "longitude": -80.188583},
    {"latitude": 26.914127, "longitude": -80.174911},
    {"latitude": 27.067636, "longitude": -80.267884},
    {"latitude": 27.194184, "longitude": -80.338981},
    {"latitude": 27.325447, "longitude": -80.478440},
    {"latitude": 27.451702, "longitude": -80.503051},
    {"latitude": 27.546299, "longitude": -80.538599},
    {"latitude": 27.589932, "longitude": -80.590555},
    {"latitude": 27.730407, "longitude": -80.672590},
    {"latitude": 27.880370, "longitude": -80.686262},
    {"latitude": 27.984256, "longitude": -80.724545},
    {"latitude": 28.044608, "longitude": -80.814784},
    {"latitude": 28.170033, "longitude": -80.754625},
    {"latitude": 28.467230, "longitude": -80.949765},
    {"latitude": 28.657637, "longitude": -81.044611},
    {"latitude": 28.930741, "longitude": -81.078484},
    {"latitude": 29.078866, "longitude": -81.410445},
    {"latitude": 29.356766, "longitude": -81.329149},
    {"latitude": 29.527859, "longitude": -81.417220},
    {"latitude": 29.610352, "longitude": -81.667884},
    {"latitude": 29.728083, "longitude": -81.457868},
    {"latitude": 29.869178, "longitude": -81.437544},
    {"latitude": 30.021805, "longitude": -81.816928},
    {"latitude": 30.215187, "longitude": -81.471418},
    {"latitude": 30.644946, "longitude": -81.820757}
]

        for data in latlang:
            # print(data['latitude'], data['longitude'])
            hotels = self.fetch_hotels_from_google(data['latitude'], data['longitude'])
            self.save_hotels_to_db(hotels)

        return JsonResponse({'message': 'Hotels fetched and saved successfully'})
            

        

    def fetch_hotels_from_google(self, lat, lng):
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&rankby=distance&type=lodging&key={settings.GOOGLE_API_KEY}"
        response = requests.get(url)
        results = response.json().get('results', [])

        hotels = []
        
        for result in results:
            print("Icon : ",result.get('icon'),result['icon'])
            hotel = {
                'place_id': result['place_id'],
                'name': result['name'],
                'address': result.get('vicinity', ''),
                'latitude': result['geometry']['location']['lat'],
                'longitude': result['geometry']['location']['lng'],
                'icon': result.get('icon')
            }
            hotels.append(hotel)

        return hotels

    def save_hotels_to_db(self, hotels):
        for hotel in hotels:
            Hotel.objects.get_or_create(
                place_id=hotel['place_id'],
                defaults={
                    'name': hotel['name'],
                    'address': hotel['address'],
                    'latitude': hotel['latitude'],
                    'longitude': hotel['longitude'],
                    'icon': hotel.get('icon') 
                }
            )
def getAllHotels(request):
    results = Hotel.objects.all().values('id','place_id','name','address','rating','latitude','longitude','icon')
    customers = []
    print('Result')
    print(len(results))
    for row in results:
        customers.append(json.dumps(row, default=str,))
    print(len(customers))
    return JsonResponse(customers, safe=False)
from django.http import JsonResponse

from shapely.geometry import Point, LineString

import requests
from django.http import JsonResponse
from django.conf import settings
from .models import Location, Viewport, Geometry, Photo, PlusCode, Hotel

def truncate_all_tables(request):
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA foreign_keys=OFF;")
        for table in connection.introspection.table_names():
            cursor.execute(f"DELETE FROM `{table}`;")
            cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}';")
        cursor.execute("PRAGMA foreign_keys=ON;")
        return JsonResponse([], safe=False)

def saveToDb(api_response):
    data = api_response
    
    for result in data['results']:
        if not Hotel.objects.filter(place_id=result['place_id']).exists():
            location_data = result['geometry']['location']
            location = Location.objects.create(
                lat=location_data['lat'],
                lng=location_data['lng']
            )

            viewport_data = result['geometry']['viewport']
            viewport = Viewport.objects.create(
                northeast_lat=viewport_data['northeast']['lat'],
                northeast_lng=viewport_data['northeast']['lng'],
                southwest_lat=viewport_data['southwest']['lat'],
                southwest_lng=viewport_data['southwest']['lng']
            )

            geometry = Geometry.objects.create(
                location=location,
                viewport=viewport

            )
            plus_code_data = result.get('plus_code', {})
            plus_code = PlusCode.objects.create(
                compound_code=plus_code_data.get('compound_code', ''),
                global_code=plus_code_data.get('global_code', '')
            )
            if result.get('user_ratings_total', {}):
                user_ratings_total=result.get('user_ratings_total', {})
            else:
                user_ratings_total=0
            hotel = Hotel.objects.create(
                business_status=result.get('business_status'),
                geometry=geometry,
                icon=result.get('icon'),
                icon_background_color=result['icon_background_color'],
                icon_mask_base_uri=result['icon_mask_base_uri'],
                name=result['name'],
                open_now=result.get('opening_hours', {}).get('open_now', False),
                place_id=result['place_id'],
                plus_code=plus_code,
                rating=result.get('rating'),
                reference=result['reference'],
                scope=result['scope'],
                types=','.join(result['types']),
                user_ratings_total=user_ratings_total,
                vicinity = result.get('vicinity', {}) if result.get('vicinity', {}) is not None else 0
            )

            for photo in result.get('photos', []):
                photo_obj = Photo.objects.create(
                    height=photo['height'],
                    width=photo['width'],
                    html_attributions=', '.join(photo['html_attributions']),
                    photo_reference=photo['photo_reference']
                )
                hotel.photos.add(photo_obj)

            hotel.save()
            print("Hotel ",hotel.id,'-->',hotel.name)

 

def saveHotel(request):
    typeList=[
        'hotel',
        'motel',
        'lodging'
    ]

    latlang=[
    {"latitude": 30.528997, "longitude": -85.884900},
    {"latitude": 30.467823, "longitude": -85.481728},
    {"latitude": 30.177115, "longitude": -85.285272},
    {"latitude": 30.395227, "longitude": -84.892362},
    {"latitude": 30.346799, "longitude": -84.331061},
    {"latitude": 30.274113, "longitude": -83.853955},
    {"latitude": 30.152850, "longitude": -83.404915},
    {"latitude": 30.201373, "longitude": -83.012004},
    {"latitude": 29.934201, "longitude": -83.124264},
    {"latitude": 29.934201, "longitude": -83.124264},
    {"latitude": 29.644144, "longitude": -82.891468},
    {"latitude": 29.564339, "longitude": -82.570213},
    {"latitude": 29.577644, "longitude": -82.172468},
    {"latitude": 30.438702, "longitude": -82.631404},
    {"latitude": 30.148104, "longitude": -82.524319},
    {"latitude": 30.121644, "longitude": -82.264255},
    {"latitude": 30.174558, "longitude": -81.988894},
    {"latitude": 30.028976, "longitude": -82.203064},
    {"latitude": 29.909704, "longitude": -81.820617},
    {"latitude": 29.577644, "longitude": -81.912404},
    {"latitude": 29.670732, "longitude": -81.637043},
    {"latitude": 29.617549, "longitude": -81.453468},
    {"latitude": 29.497786, "longitude": -81.820617},
    {"latitude": 29.271181, "longitude": -82.019489},
    {"latitude": 29.003942, "longitude": -82.065383},
    {"latitude": 29.271181, "longitude": -81.835915},
    {"latitude": 29.137648, "longitude": -81.499362},
    {"latitude": 29.097555, "longitude": -81.835915},
    {"latitude": 28.896852, "longitude": -81.973596},
    {"latitude": 28.548048, "longitude": -81.988894},
    {"latitude": 28.292419, "longitude": -81.790021},
    {"latitude": 28.157630, "longitude": -81.606447},
    {"latitude": 28.066303, "longitude": -81.422551},
    {"latitude": 28.012578, "longitude": -81.257333},
    {"latitude": 27.951145, "longitude": -81.083420},
    {"latitude": 27.935782, "longitude": -81.379073},
    {"latitude": 27.920416, "longitude": -81.744290},
    {"latitude": 27.527851, "longitude": -81.639942},
    {"latitude": 27.481574, "longitude": -81.909508},
    {"latitude": 27.334902, "longitude": -81.944290},
    {"latitude": 27.303999, "longitude": -82.248638},
    {"latitude": 27.242167, "longitude": -82.074725},
    {"latitude": 27.175862, "longitude": -81.461201},
    {"latitude": 27.189757, "longitude": -81.195667},
    {"latitude": 27.264911, "longitude": -81.067270},
    {"latitude": 27.037494, "longitude": -81.176805},
    {"latitude": 26.796580, "longitude": -81.220619},
    {"latitude": 26.646564, "longitude": -81.206014},
    {"latitude": 26.522489, "longitude": -81.279037},
    {"latitude": 26.378655, "longitude": -81.454292},
    {"latitude": 26.195335, "longitude": -81.498106},
    {"latitude": 26.037974, "longitude": -81.468897},
    {"latitude": 26.051095, "longitude": -81.198712},
    {"latitude": 26.064215, "longitude": -80.957736},
    {"latitude": 26.319763, "longitude": -80.826294},
    {"latitude": 26.260840, "longitude": -80.629132},
    {"latitude": 26.110124, "longitude": -80.497691},
    {"latitude": 25.978909, "longitude": -80.541504},
    {"latitude": 25.840975, "longitude": -80.687551},
    {"latitude": 25.702879, "longitude": -80.745969},
    {"latitude": 25.919814, "longitude": -80.541504},
    {"latitude": 25.722617, "longitude": -80.556109},
    {"latitude": 25.630480, "longitude": -80.753271},
    {"latitude": 25.538271, "longitude": -80.833597},
    {"latitude": 25.426209, "longitude": -80.592621},
    {"latitude": 25.314042, "longitude": -80.541504},
    {"latitude": 25.818571, "longitude": -80.344273},
    {"latitude": 25.920899, "longitude": -80.361579},
    {"latitude": 26.038690, "longitude": -80.378885},
    {"latitude": 26.063122, "longitude": -80.304716},
    {"latitude": 26.158581, "longitude": -80.228075},
    {"latitude": 26.194080, "longitude": -80.186046},
    {"latitude": 26.327422, "longitude": -80.199521},
    {"latitude": 26.452348, "longitude": -80.185849},
    {"latitude": 26.415619, "longitude": -80.150300},
    {"latitude": 26.545343, "longitude": -80.177645},
    {"latitude": 26.689580, "longitude": -80.163973},
    {"latitude": 26.779940, "longitude": -80.188583},
    {"latitude": 26.914127, "longitude": -80.174911},
    {"latitude": 27.067636, "longitude": -80.267884},
    {"latitude": 27.194184, "longitude": -80.338981},
    {"latitude": 27.325447, "longitude": -80.478440},
    {"latitude": 27.451702, "longitude": -80.503051},
    {"latitude": 27.546299, "longitude": -80.538599},
    {"latitude": 27.589932, "longitude": -80.590555},
    {"latitude": 27.730407, "longitude": -80.672590},
    {"latitude": 27.880370, "longitude": -80.686262},
    {"latitude": 27.984256, "longitude": -80.724545},
    {"latitude": 28.044608, "longitude": -80.814784},
    {"latitude": 28.170033, "longitude": -80.754625},
    {"latitude": 28.467230, "longitude": -80.949765},
    {"latitude": 28.657637, "longitude": -81.044611},
    {"latitude": 28.930741, "longitude": -81.078484},
    {"latitude": 29.078866, "longitude": -81.410445},
    {"latitude": 29.356766, "longitude": -81.329149},
    {"latitude": 29.527859, "longitude": -81.417220},
    {"latitude": 29.610352, "longitude": -81.667884},
    {"latitude": 29.728083, "longitude": -81.457868},
    {"latitude": 29.869178, "longitude": -81.437544},
    {"latitude": 30.021805, "longitude": -81.816928},
    {"latitude": 30.215187, "longitude": -81.471418},
    {"latitude": 30.644946, "longitude": -81.820757}
]
    for type in typeList:
        for data in latlang:
            lat = data['latitude']
            lng =  data['longitude']
            url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&rankby=distance&type={type}&key={settings.GOOGLE_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data=response.json()
                if not Hotel.objects.filter(place_id=data.get('place_id')).exists():
                    saveToDb(data)
                    next_page_token = data.get('next_page_token')
                    print('next_page_token = ',next_page_token)
                    while next_page_token:
                        newUrl = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={settings.GOOGLE_API_KEY}"
                        res = requests.get(newUrl)
                        newData=res.json()
                        next_page_token = newData.get('next_page_token')
                        # print('2nd calling next page url, Status = ',res.status_code)
                        if res.status_code == 200:
                            if not Hotel.objects.filter(place_id=data.get('place_id')).exists():
                                saveToDb(newData)
                        if not next_page_token:
                            break
                    else:
                        print('Hotel exists')


    return JsonResponse({'message': 'Hotels fetched and saved successfully'})
    
    
def fetch_latestHotels(request):
    hotels = Hotel.objects.all()
    results = []

    for hotel in hotels:
        result = {
            "business_status": hotel.business_status,
            "geometry": {
                "location": {
                    "lat": hotel.geometry.location.lat,
                    "lng": hotel.geometry.location.lng
                },
                "viewport": {
                    "northeast": {
                        "lat": hotel.geometry.viewport.northeast_lat,
                        "lng": hotel.geometry.viewport.northeast_lng
                    },
                    "southwest": {
                        "lat": hotel.geometry.viewport.southwest_lat,
                        "lng": hotel.geometry.viewport.southwest_lng
                    }
                }
            },
            "icon": hotel.icon,
            "icon_background_color": hotel.icon_background_color,
            "icon_mask_base_uri": hotel.icon_mask_base_uri,
            "name": hotel.name,
            "opening_hours": {
                "open_now": hotel.open_now
            },
            "photos": [{
                "height": photo.height,
                "html_attributions": photo.html_attributions.split(','),
                "photo_reference": photo.photo_reference,
                "width": photo.width
            } for photo in hotel.photos.all()],
            "place_id": hotel.place_id,
            "plus_code": {
                "compound_code": hotel.plus_code.compound_code,
                "global_code": hotel.plus_code.global_code
            },
            "rating": hotel.rating,
            "reference": hotel.reference,
            "scope": hotel.scope,
            "types": hotel.types.split(','),
            "user_ratings_total": hotel.user_ratings_total,
            "vicinity": hotel.vicinity
        }
        results.append(result)

    return JsonResponse(results, safe=False)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def is_distance_one(lat,lng, polyline,threshold_distance):
    for poly_point in polyline:
        distance = haversine(lat, lng, poly_point.lat, poly_point.lng)
        print('distance = ',distance)
        if distance <= threshold_distance:
            return True
    return False
def decode_poly(encoded):
    points = []
    index = 0
    lat = 0
    lng = 0

    while index < len(encoded):
        b, shift, result = 0, 0, 0
        while True:
            b = ord(encoded[index]) - 63
            index += 1
            result |= (b & 0x1F) << shift
            shift += 5
            if b < 0x20:
                break
        dlat = ~(result >> 1) if (result & 1) != 0 else (result >> 1)
        lat += dlat

        shift, result = 0, 0
        while True:
            b = ord(encoded[index]) - 63
            index += 1
            result |= (b & 0x1F) << shift
            shift += 5
            if b < 0x20:
                break
        dlng = ~(result >> 1) if (result & 1) != 0 else (result >> 1)
        lng += dlng

        lat_double = lat / 1E5
        lng_double = lng / 1E5
        position = LatLng(lat_double, lng_double)
        points.append(position)

    return points



def get_coordinates_along_polyline(request):
    # Get coordinates A and B from request
    lat1, lon1 = float(request.GET.get('lat1')), float(request.GET.get('lon1'))
    lat2, lon2 = float(request.GET.get('lat2')), float(request.GET.get('lon2'))
    south_lat = float(request.GET.get('south_lat'))
    west_lon = float(request.GET.get('west_lon'))
    north_lat = float(request.GET.get('north_lat'))
    east_lon = float(request.GET.get('east_lon'))
    
    # Create a bounding box using shapely
    bounding_box = box(west_lon, south_lat, east_lon, north_lat)

    print(lat1,lon1)
    print(lat2,lon2)
    
    # Create LineString from A to B
        # line = LineString([(lon1, lat1), (lon2, lat2)])
    decoded_points=[]
    
    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=50000&type=lodging&key={settings.GOOGLE_API_KEY}"
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={lat1},{lon1}&destination={lat2},{lon2}&key={settings.GOOGLE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data=response.json()
        decoded_points = decode_poly(data['routes'][0]['overview_polyline']['points'])
        # for point in decoded_points:
            # print(f"Lat: {point.lat}, Lng: {point.lng}")

    
    # Threshold distance for points to be considered 'alongside' the polyline
    
    threshold_distance = float(request.GET.get('threshold_distance'))
    hotels = Hotel.objects.all()
    results = []

    for hotel in hotels:
        result = {
            "business_status": hotel.business_status,
            "geometry": {
                "location": {
                    "lat": hotel.geometry.location.lat,
                    "lng": hotel.geometry.location.lng
                },
                "viewport": {
                    "northeast": {
                        "lat": hotel.geometry.viewport.northeast_lat,
                        "lng": hotel.geometry.viewport.northeast_lng
                    },
                    "southwest": {
                        "lat": hotel.geometry.viewport.southwest_lat,
                        "lng": hotel.geometry.viewport.southwest_lng
                    }
                }
            },
            "icon": hotel.icon,
            "icon_background_color": hotel.icon_background_color,
            "icon_mask_base_uri": hotel.icon_mask_base_uri,
            "name": hotel.name,
            "opening_hours": {
                "open_now": hotel.open_now
            },
            "photos": [{
                "height": photo.height,
                "html_attributions": photo.html_attributions.split(','),
                "photo_reference": photo.photo_reference,
                "width": photo.width
            } for photo in hotel.photos.all()],
            "place_id": hotel.place_id,
            "plus_code": {
                "compound_code": hotel.plus_code.compound_code,
                "global_code": hotel.plus_code.global_code
            },
            "rating": hotel.rating,
            "reference": hotel.reference,
            "scope": hotel.scope,
            "types": hotel.types.split(','),
            "user_ratings_total": hotel.user_ratings_total,
            "vicinity": hotel.vicinity
        }
        results.append(result)


    
    # Get all coordinates from the database
    # allHotelList = Hotel.objects.all().values('id','place_id','name','address','rating','latitude','longitude','icon')
    
    # Filter coordinates that are alongside the polyline
    result = []
    # for hotel in allHotelList:
    #     # print("latitude == ? mm",hotel['latitude'])
    #     point = Point(hotel['longitude'], hotel['latitude'])
    #     if line.distance(point) <= threshold_distance and bounding_box.contains(point):
    #         result.append(json.dumps(hotel, default=str,))
    for hotel in results:
        # print("latitude == ",hotel['geometry']['location']['lat'],hotel['geometry']['location']['lng'])
        point = Point(hotel['geometry']['location']['lng'], hotel['geometry']['location']['lat'])
        # print("distance from point == ",line.distance(point),bounding_box.contains(point))
        if is_distance_one(hotel['geometry']['location']['lat'],hotel['geometry']['location']['lng'], decoded_points,threshold_distance) and bounding_box.contains(point):
            print('inserting')
            result.append(hotel)
    print('Len', len(results))


    
    return JsonResponse(result, safe=False)



def handle_scraping(row, city_name, city_obj):
    """
    Scrapes data for various categories from a given URL, and inserts them into the corresponding model.

    Parameters:
    - row (dict): A dictionary containing details to be scraped. It must have keys 'url' and 'category'.
    - city_name (str): Name of the city for which the scraping is being done.

    Returns:
    - instance (model instance): An instance of the saved scraped data.
    - None: if the URL has already been scraped or if the scraping yields no data.

    Note:
    This function supports various categories like ATTRACTION, FOOD, etc., and based on the category,
    it saves the scraped data into the corresponding model. The function checks if the data for a URL
    has already been scraped to avoid duplication.
    """

    print(f"Scrapping Started For URL {row['url']}")

    # Mapping categories to their corresponding models
    category_to_model = {
        Constant.ATTRACTION: trip_models.Attraction,
        Constant.FOOD: trip_models.Food,
        Constant.WEIRDANDWACKY: trip_models.WeirdAndWacky,
        Constant.CAMPING: trip_models.Camp,
        Constant.NATIONAL_PARK: trip_models.Park,
        Constant.FAMILY_FUN: trip_models.FamilyFun,
        Constant.HISTORICAL_SITES: trip_models.HistoricalSite,
        Constant.EXTREME_SPORTS: trip_models.ExtremeSport,
        Constant.EVENT_CALENDAR: trip_models.Event,
    }

    category = trip_models.Category.get_instance({"name": row["category"]})
    model_name = category_to_model.get(category.name)

    # If URL has already been scraped, we avoid scraping it again
    if model_name and model_name.filter_instance(
        {"meta_data__scraped_from": row["url"]}
    ):
        return None

    # Scrape the data
    scrape_data = Scrape(city_obj.name, category, row["url"]).scrape_data()

    if isinstance(scrape_data, list):
        instances_to_insert = []
        for item in scrape_data:
            latitude = (
                city_obj.latitude if item["latitude"] is None else item["latitude"]
            )
            longitude = (
                city_obj.longitude if item["longitude"] is None else item["longitude"]
            )
            data = {
                "latitude": latitude,
                "longitude": longitude,
                "name": item["title"],
                "description": item.get("description", ""),
                "images": item.get("images", []),
                "meta_data": item.get("meta_data", {}),
                "city": city_obj,
            }
            instance = model_name(**data)
            instances_to_insert.append(instance)

        if instances_to_insert:
            instances = model_name.objects.bulk_create(instances_to_insert)
            return instances
        else:
            return []
    else:
        if scrape_data:
            if scrape_data["latitude"] is None or scrape_data["longitude"] is None:
                scrape_data.update(
                    {"latitude": city_obj.latitude, "longitude": city_obj.longitude}
                )
            scrape_data["city_id"] = city_obj.id
            instance = model_name.create_instance(scrape_data)
            return instance

    return None


class BulkUploadAPIView(APIView):
    """
    API View for bulk uploading an Excel file containing city, category, and URL data.

    The provided Excel file should have columns named 'city', 'category', and potentially others.
    After uploading the file, the 'city' and 'category' columns will be forward filled
    to replace NaN values. This API primarily serves as a preprocessing step before web scraping
    tasks are executed using the provided data.

    This endpoint requires Session Authentication and can only be accessed by SuperAdmin users.

    Attributes:
    - authentication_classes (list): List of authentication classes the view should use.
    - permission_classes (list): List of permission classes the view should use.

    Methods:
    - post(request, *args, **kwargs): Handles the POST request for uploading the Excel file.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for bulk data upload through an Excel file.

        The method reads the uploaded Excel, processes the 'city' and 'category' columns,
        and may trigger web scraping tasks based on the provided URLs in the file.

        Args:
        - request (Request): The DRF request object containing the uploaded file.
        - *args (tuple): Variable length argument list.
        - **kwargs (dict): Arbitrary keyword arguments.

        Returns:
        - HttpResponseRedirect: Redirects the user to the Django Admin index page with a feedback message.
        """
        try:
            # Convert the uploaded Excel file into a pandas DataFrame
            file_data = pd.read_excel(request.data["file"])

            # Extracting details of the first city for potential creation
            first_row = file_data.iloc[0]
            city_url, city_name = first_row["url"], first_row["city"]

            # Create city if it doesn't exist
            city = trip_models.City.get_instance_or_none({"name": city_name})
            if city and city.latitude is None:
                image_url, description = scrap_images(url=city_url)
                image_url = [image_url] if image_url else []
                latitude, longitude = get_geo_code(city_name)
                city.latitude = latitude
                city.longitude = longitude
                city.images = image_url
                city.description = description

            else:
                image_url, description = scrap_images(url=city_url)
                image_url = [image_url] if image_url else []
                latitude, longitude = get_geo_code(city_name)

                city_data = {
                    "name": city_name,
                    "country": None,
                    "latitude": latitude,
                    "longitude": longitude,
                    "images": image_url,
                    "description": description,
                }
                city = trip_models.City.create_instance(city_data)

            # Drop the first row and reset index
            file_data = file_data.drop(index=0).reset_index(drop=True)

            # Handle missing values: Forward fill NaNs for 'City' and 'Category', then drop rows with missing 'url'
            file_data["city"] = file_data["city"].ffill()
            file_data["category"] = file_data["category"].ffill()
            file_data = file_data.dropna(subset=["url"])
            file_data = file_data[file_data["url"] != ""]

            # Parallel web scraping using ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [
                    executor.submit(handle_scraping, row, city_name, city)
                    for _, row in file_data.iterrows()
                ]
                for future in as_completed(futures):
                    try:
                        result = future.result()
                    except Exception as e:
                        print(f"Error occurred during scraping: {e}")

            messages.success(request, "File uploaded and processed successfully!")

        except Exception as ex:
            # Provide feedback if any other error occurs during the file upload process
            messages.error(request, f"Web Scrapping Failed Due to - {ex}")

        # Redirect back to the admin panel
        return HttpResponseRedirect(reverse("admin:index"))


class AddHotelAPIView(APIView):
    """
    API view to scrape hotel details from a provided website URL and add the hotel to the system.

    Attributes:
    ----------
    authentication_classes :
        List of authentication classes. Here, only SessionAuthentication is used.
    permission_classes :
        List of permission classes. This endpoint requires the user to be a super admin.

    Methods:
    -------
    post(request, *args, **kwargs):
        Handle POST requests to add a hotel by scraping details from a provided URL.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests. Expects a 'hotel_link' in the request data.

        Parameters:
        ----------
        request : HttpRequest
            The request instance.

        Returns:
        -------
        HttpResponseRedirect
            Redirects back to the admin panel after processing.
        """
        try:
            website_url = request.data["hotel_link"]
            if not website_url:
                raise Exception("Invalid Link")
            ScrapeHotels(website_url).scrape_data()
            messages.success(request, "Hotel Added Successfully!")

        except Exception as ex:
            # Provide feedback if any error occurs during the scraping process
            messages.error(request, f"Web Scrapping Failed Due to - {ex}")

        # Redirect back to the admin panel
        return HttpResponseRedirect(reverse("admin:index"))

class SearchCityListAPIView(generics.ListAPIView):
    serializer_class = trip_serializer.CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class AddSiteAPIView(APIView):
    """
    API View to add data provided by the user: city, category, and URL.

    This endpoint requires Session Authentication and can only be accessed by SuperAdmin users.

    Attributes:
    - authentication_classes (list): List of authentication classes the view should use.
    - permission_classes (list): List of permission classes the view should use.

    Methods:
    - post(request, *args, **kwargs): Handles the POST request to add the provided data.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        # Extract data from the POST request
        city_name = request.data.get("city")
        data_url = request.data.get("data_url")
        category = request.data.get("category")

        # Validate the provided data
        if not city_name or not data_url or not category:
            messages.error(
                request, "Missing required data. City, URL, and Category are mandatory."
            )
            return HttpResponseRedirect(reverse("admin:index"))

        try:
            city_instance = trip_models.City.get_instance_or_none({"name": city_name})
            if not city_instance:
                trip_models.City.create_instance({"name": city_name})
            if city_instance and not city_instance.latitude:
                latitude, longitude = get_geo_code(city_name)
                city_instance.latitude = latitude
                city_instance.longitude = longitude
                city_instance.save()

            row = {"category": category, "url": data_url}
            handle_scraping(row, city_name, city_instance)
            messages.success(request, "Data added successfully!")

        except Exception as ex:
            messages.error(request, f"Error adding data: {ex}")

        # Redirect back to the admin panel
        return HttpResponseRedirect(reverse("admin:index"))


class CategoryWiseListAPIView(generics.ListCreateAPIView):
    """Get All the Category List Items"""

    pagination_class = pagination.DefaultPagination
    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    filter_backends = [SearchFilter]
    search_fields = ["name", "city__name"]

    def get_queryset(self, model=None, **kwargs):
        """_summary_

        Args:
            model (_type_, optional): gives models to be
            fetched from. Defaults to None.

        Returns:
            array of object: returns array of objects from the respective
            models
        """
        # Annotate the queryset with a value that indicates if the array field is null or not
        annotated_queryset = model.objects.annotate(
            is_null=Coalesce(
                models.Value(False),
                models.Value(True),
                output_field=models.BooleanField(),
            )
        )

        # Order the queryset by the array field and the is_null value
        ordered_queryset = annotated_queryset.order_by("-images", F("is_null"))

        return ordered_queryset

    @swagger_auto_schema(responses={200: schema.category_data_list_response})
    def get(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs: Get func to list out all the items which falls under respective
            categories, This will be returned as paginated response
            where user can send number page response
        """
        # Extract data for Get request
        category = self.request.query_params.get("category", None)
        category = trip_models.Category.get_instance({"name": category})
        city_name = self.request.query_params.get("city_name", None)

        # Switching Serializer Btw Hotel Cat. and Others
        if category.name == Constant.HOTEL:
            serializer_class_list = trip_serializer.HotelModelSerializer
        else:
            serializer_class_list = trip_serializer.AttractionModelSerializer
        if category:
            # Mapping the category
            model_name = ModelMap.category_to_model.get(category.name)

            filtered_queryset = self.filter_queryset(
                queryset=self.get_queryset(model=model_name, **kwargs)
            )
            if city_name:
                city_obj = trip_models.City.get_instance({"name": city_name})
                filtered_queryset = filtered_queryset.filter(city=city_obj)

            # Applying pagination on queryset level
            list_of_items = serializer_class_list(
                self.paginate_queryset(filtered_queryset), context={"request": request,
                                                                    "category":category.name}, many=True, **kwargs
            ).data

            # Applying pagination on response level
            return Response(
                data=self.get_paginated_response(list_of_items).data,
                status=status.HTTP_200_OK,
            )
        # Handling if Cat. Does Not Exist
        return Response(
            constants.ApplicationMessages.CATEGORY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )


class CategoryListAPIView(generics.ListCreateAPIView):
    """Get All the Categories"""

    pagination_class = pagination.DefaultPagination
    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    category_models = trip_models.Category
    serializer_class = trip_serializer.CategorySerializer

    def get_queryset(self, **kwargs):
        """_summary_
        Returns:
            array of object: returns array of objects from the respective
            models
        """
        return self.category_models.filter_instance(kwargs).order_by("-created_at")

    @swagger_auto_schema(responses={200: schema.category_list_response})
    def get(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs:
            This gives list of category objects, This will be returned as paginated response
            where user can send number page response
        """

        # Filter Queryset to fetch data
        filtered_queryset = self.filter_queryset(queryset=self.get_queryset())

        # Applying pagination on queryset level
        list_of_items = self.serializer_class(
            self.paginate_queryset(filtered_queryset), many=True, **kwargs
        ).data

        # Applying pagination on response level
        return Response(
            data=self.get_paginated_response(list_of_items).data,
            status=status.HTTP_200_OK,
        )


class CityListAPIView(generics.ListCreateAPIView):
    """Get All the Cities"""

    pagination_class = pagination.DefaultPagination
    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    city_model = trip_models.City
    serializer_class = trip_serializer.CitySerializer

    def get_queryset(self, **kwargs):
        """_summary_
        Returns:
            array of object: returns array of objects from the respective
            models
        """
        return self.city_model.filter_instance(kwargs).order_by("-created_at")

    @swagger_auto_schema(responses={200: schema.city_list_response})
    def get(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs:
            This gives list of category objects, This will be returned as paginated response
            where user can send number page response
        """

        # Filter Queryset to fetch data
        filtered_queryset = self.filter_queryset(queryset=self.get_queryset())

        # Applying pagination on queryset level
        list_of_items = self.serializer_class(
            self.paginate_queryset(filtered_queryset),
            many=True,
            context={"request": request},
            **kwargs,
        ).data

        # Applying pagination on response level
        return Response(
            data=self.get_paginated_response(list_of_items).data,
            status=status.HTTP_200_OK,
        )


class TripPlanListAPIView(generics.ListCreateAPIView):
    """Get All the Cities"""

    pagination_class = pagination.DefaultPagination
    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    serializer_class = trip_serializer.CommonSerializer

    def get_queryset(self, model=None, cities=None, search=None, **kwargs):
        """_summary_

        Args:
            model (_type_, optional): gives models to be
            fetched from. Defaults to None.

        Returns:
            array of object: returns array of objects from the respective
            models
        """
        if cities:
            kwargs.update({"city__in": cities})
        if search:
            kwargs.update({"name__icontains": search.lower()})

        return model.filter_instance(kwargs).order_by("-created_at")

    @swagger_auto_schema(responses={200: schema.trip_list_response})
    def get(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs:
            This gives list of category objects, This will be returned as paginated response
            where user can send number page response
        """
        # Extract data for Get request
        cities = request.query_params.getlist("cities", None)
        categories = request.query_params.getlist("categories", None)

        # Custom search on multiple Categories
        search = request.query_params.get("search", None)

        if categories:
            # Converting the string in to csv
            categories = categories[0].split(",")
            models = [ModelMap.category_to_model[key] for key in categories]

        if cities:
            # Converting the string in to csv
            cities = cities[0].split(",")
            city_objs = trip_models.City.filter_instance({"name__in": cities})

        component_list = []

        # iterating the list of Categories
        for item in models:
            # Filter Queryset to fetch data
            filtered_queryset = self.filter_queryset(
                queryset=self.get_queryset(model=item, cities=city_objs, search=search)
            )

            # Applying pagination on queryset level
            if filtered_queryset:
                list_of_items = self.serializer_class(
                    self.paginate_queryset(filtered_queryset), many=True, **kwargs
                ).data

                # Adding components to a list to get cumulative result
                component_list.append(
                    {"type": item._meta.model_name, "data": list_of_items}
                )

        return Response(
            data=self.get_paginated_response(component_list).data,
            status=status.HTTP_200_OK,
        )


class TripPlanAPIView(generics.CreateAPIView):
    """
    API View to fetch a trip route along with points of interest (POIs) based on user preferences.

    The user provides the starting and ending points, how long they wish to travel in a day, and the categories of
    places they are interested in. This view will then return a route and the places of interest along that route.
    """

    serializer_class = trip_serializer.TripPlanSerializer
    permission_classes = [
        permissions.IsUser | permissions.IsSuperAdmin,
    ]

    @swagger_auto_schema(responses={200: schema.plan_trip_response})
    def post(self, request, *args, **kwargs):
        at_start = datetime.datetime.now()
        # Deserialize and validate the incoming request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            # Fetch the best route between origin and destination
            origin, destination = data["origin"]["name"], data["destination"]["name"]
            route, rout_resp = get_route(origin, destination, GOOGLE_API_KEY)
            if route is None:
                raise Exception("Failed to fetch the route from Google Maps.")

            # Calculate estimated travel distance based on how many hours the user wants to travel in a day
            # hours = int(data["travel_time"].split()[0])
            # estimated_distance = hours * constants.Constant.AVERAGE_SPEED

            # Filter the steps of the route based on the estimated distance
            # filtered_steps = route[:estimated_distance]

            # Determine categories of places the user is interested in
            # categories_to_fetch = set(data["categories"] + ["Food", "Hotels"])
            categories_to_fetch = set(data["categories"])

            seen_places = set()  # Track places to avoid duplicates
            results = []

            # Prepare arguments list for the ThreadPoolExecutor
            args_list = [
                (cat, route, GOOGLE_API_KEY, seen_places, results, origin, destination, self.request.user)
                for cat in categories_to_fetch
            ]

            # Use ThreadPoolExecutor to fetch POIs concurrently for better response times
            with ThreadPoolExecutor() as executor:
                poi_results = executor.map(fetch_pois_for_category, args_list)

            # Collate results from all the threads
            for res in poi_results:
                results.extend(res)

            at_end = datetime.datetime.now()
            log_data = {
                "user": self.request.user,
                "origin": origin,
                "destination": destination,
                "travel_time": data.get("travel_time"),
                "categories": data.get("categories"),
                "discount_type": data.get("discount_type"),
            }
            helper.save_user_trip_info(log_data, at_start, at_end)
            # Send the collated results as the response
            return Response(
                {"route": rout_resp, "places": results}, status=status.HTTP_200_OK
            )

        except Exception as ex:
            raise ValidationError(str(ex), status.HTTP_400_BAD_REQUEST)


class TripSaveAPIView(generics.CreateAPIView):
    """
    API View to fetch a trip route along with points of interest (POIs) based on user preferences.

    The user provides the starting and ending points, how long they wish to travel in a day, and the categories of
    places they are interested in. This view will then return a route and the places of interest along that route.
    """

    serializer_class = trip_serializer.TripSaveSerializer

    @swagger_auto_schema(responses={200: schema.save_trip_response})
    def post(self, request, *args, **kwargs):
        # Deserialize and validate the incoming request data

        # Four different combinations of data
        # 1. origin, destination,  categories, map view
        # 2. origin, destination,  categories, list view
        # 3. near me, categories, map view
        # 4. near me, categories, list view
        # 5. destination, categories, map view
        # 6. destination, categories, list view

        # Deserialize and validate the incoming request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        view_type = request.data.get("view_type", None)
        discount_type = request.data.get("discount_type", None)
        limit = request.data.get("limit", None)

        if discount_type == "ALL":
            categories_to_fetch = Constant.DISCOUNT_TYPE_SAVE_MODULE_CHOICES
        else:
            categories_to_fetch = [discount_type]

        try:
            # Fetch the best route between origin and destination
            seen_places = set()  # Track places to avoid duplicates
            results = []
            route, rout_resp = None, None
            if not "destination" in data:  # near me and for my destination
                location = request.data.get("origin").get("location", None)
                if location is None:
                    raise Exception("Failed to fetch the location from Google Maps.")
                args_list = [
                    (cat, location, GOOGLE_API_KEY, seen_places, results)
                    for cat in categories_to_fetch
                ]

                # Use ThreadPoolExecutor to fetch POIs concurrently for better response times
                with ThreadPoolExecutor() as executor:
                    poi_results = executor.map(fetch_pois_save_for_location, args_list)

            elif "destination" in data:
                route, rout_resp = get_route(
                    data["origin"]["name"], data["destination"]["name"], GOOGLE_API_KEY
                )
                if route is None:
                    raise Exception("Failed to fetch the route from Google Maps.")

                # Prepare arguments list for the ThreadPoolExecutor
                # Determine categories of places the user is interested in
                args_list = [
                    (cat, route, GOOGLE_API_KEY, seen_places, results)
                    for cat in categories_to_fetch
                ]

                # Use ThreadPoolExecutor to fetch POIs concurrently for better response times
                with ThreadPoolExecutor() as executor:
                    poi_results = executor.map(fetch_pois_save_with_route, args_list)
                if view_type == "list_view":
                    rout_resp = []

            # categories_to_fetch = set(data["categories"] + ["Food", "Hotels"])
            final_results = []

            # Collate results from all the threads
            for res in poi_results:
                final_results.extend(res)
            if limit:
                filtered_data = defaultdict(list)
                for item in final_results:
                    category = item["category_name"]
                    if len(filtered_data[category]) < limit:
                        filtered_data[category].append(item)

                # Send the collated results as the response
                return Response(
                    {"route": rout_resp, "places": filtered_data},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"route": rout_resp, "places": final_results}, status=status.HTTP_200_OK
            )

        except Exception as ex:
            raise ValidationError(str(ex), status.HTTP_400_BAD_REQUEST)


class CityDetailAPIView(generics.ListCreateAPIView):
    """Get Details of a City"""

    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    city_model = trip_models.City
    serializer_class = trip_serializer.CityDetailSerializer

    @swagger_auto_schema(responses={200: schema.city_list_response})
    def get(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs:
            This gives list of category objects
        """

        # Get City ID for details
        city_id = request.query_params.get("city_id", None)
        city_obj = trip_models.City.get_instance_or_none({"id": city_id})

        if city_obj:
            # Serialize the data
            data = self.serializer_class(
                city_obj, context={"request": request}, **kwargs
            ).data

            # Applying response structure
            return Response(data=data, status=status.HTTP_200_OK)

        # Handling if City Does Not Exist
        return Response(
            constants.ApplicationMessages.CITY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, *args, **kwargs):
        """returns dict of objs in Json Format
        Returns:
            Dict Of Objs:
            Return Messages on the action
        """

        # Get City ID for details
        city_id = request.data.get("city_id", None)
        is_favorite = request.data.get("is_favorite", None)
        city_obj = trip_models.City.get_instance_or_none({"id": city_id})

        if city_obj:
            user_obj = User.objects.filter(id=self.request.user.id).first()
            # Assign variables
            if is_favorite:
                if "cities" in user_obj.meta_data.keys():
                    if str(city_obj.id) not in user_obj.meta_data["cities"]:
                        user_obj.meta_data["cities"].append(str(city_obj.id))
                else:
                    user_obj.meta_data = {"cities": [str(city_obj.id)]}
                user_obj.save()
            else:
                if str(city_obj.id) in user_obj.meta_data["cities"]:
                    user_obj.meta_data["cities"].remove(str(city_obj.id))
                    user_obj.save()

            # Applying response structure
            return Response(
                constants.ApplicationMessages.CITY_UPDATE_SUCCESSFULLY,
                status=status.HTTP_200_OK,
            )

        # Handling if City Does Not Exist
        return Response(
            constants.ApplicationMessages.CITY_DOES_NOT_EXIST,
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserLikeAPIView(generics.ListCreateAPIView):
    """Make objects as favorite objects"""

    permission_classes = (permissions.IsSuperAdmin | permissions.IsUser,)
    parser_classes = (parsers.JSONParser,)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    city_model = trip_models.City
    serializer_class = trip_serializer.CityDetailSerializer


    def post(self, request, *args, **kwargs):
        """Returns a dictionary of objects in JSON format.
        Returns:
            Dict Of Objs:
            Return Messages on the action
        """

        id = request.data.get("id", None)
        is_favorite = request.data.get("is_favorite", None)
        category = request.data.get("category", None)

        category_obj = trip_models.Category.get_instance({"name": category})
        model_name = ModelMap.category_to_model.get(category_obj.name)

        obj = model_name.objects.filter(id=id).first()

        if obj:
            user_profile, created = trip_models.UserLikes.objects.get_or_create(user=request.user)

            # Create a dictionary to map category names to their corresponding liked field
            category_to_field = {
                "Hotels": "liked_hotels",
                "Extreme Sports": "liked_extremesports",
                "Historical Sites": "liked_historicalsites",
                "Events Calendar": "liked_events",
                "Weird and Wacky": "liked_wierdandwacky",
                "National Park": "liked_parks",
                "Attractions": "liked_attractions",
            }

            # Get the corresponding liked field for the category
            liked_field = category_to_field.get(category_obj.name)

            if liked_field:
                # Get the liked field dynamically using getattr
                liked_items = getattr(user_profile, liked_field)

                if is_favorite:
                    liked_items.add(obj)
                else:
                    liked_items.remove(obj)

                # Applying response structure
                return Response(
                    constants.ApplicationMessages.CITY_UPDATE_SUCCESSFULLY,
                    status=status.HTTP_200_OK,
                )

        # Handling if the object does not exist
        return Response(
            constants.ApplicationMessages.DOES_NOT_EXISTS(category_obj.name),
            status=status.HTTP_400_BAD_REQUEST,
        )