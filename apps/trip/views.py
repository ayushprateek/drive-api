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


@api_view(['GET'])
def getAllCountry(request):
    countries = Country.objects.all().values(
        'id',
        'iso', 
        'name', 
        'nicename', 
        'iso3', 
        'numeric_code', 
        'phone_code'
    ).order_by('name')
    print(len(countries))
    country_list = list(countries)
    us_country = next((country for country in country_list if country['iso'] == 'US'), None)
    if us_country:
        country_list.remove(us_country)
        country_list.insert(0, us_country)
    return JsonResponse(country_list, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllPriority(request):
    priorities = Priority.objects.all().values(
        'id',
        'name'
    )
    print(len(priorities))
    priosity_list = list(priorities)
    return JsonResponse(priosity_list, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllTravelGoal(request):
    priorities = TravelGoal.objects.all().values(
        'id',
        'name'
    )
    print(len(priorities))
    priosity_list = list(priorities)
    return JsonResponse(priosity_list, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllMotivation(request):
    priorities = Motivation.objects.all().values(
        'id',
        'name',
        'emoji'
    )
    print(len(priorities))
    priosity_list = list(priorities)
    return JsonResponse(priosity_list, safe=False,status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllHotelBrand(request):
    hotelBrands = HotelBrand.objects.all().values(
        'id',
        'name'
    )
    print(len(hotelBrands))
    hotel_brand_list = list(hotelBrands)
    return JsonResponse(hotel_brand_list, safe=False,status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllAirlineBrand(request):
    airline_brands = AirlineBrand.objects.all().values(
        'id',
        'name'
    )
    print(len(airline_brands))
    airline_brand_list = list(airline_brands)
    return JsonResponse(airline_brand_list, safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllRestaurantBrand(request):
    restaurant_brands = RestaurantBrand.objects.all().values(
        'id',
        'name'
    )
    print(len(restaurant_brands))
    restaurant_brand_list = list(restaurant_brands)
    return JsonResponse(restaurant_brand_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def addTrip(request):
    print('Called')
    results=Category.objects.all()
    for row in results:
        # PlanCategory.objects.create(
        #     category=row
        # )
        print(row.id)
        if not TripCategory.objects.filter(category_id=row.id).exists():
            TripCategory.objects.create(
                category=row
            )
    # Category.objects.create(
    # name='Attractions',
    # image_url='static/AttractionsIcon.svg',
    # icon_url='static/AttractionsIcon.svg'
    # )
    # Category.objects.create(
    # name='Travel Info',
    # image_url='static/TravelInfoIcon.svg',
    # icon_url='static/TravelInfoIcon.svg'
    # )
    # Category.objects.create(
    # name='Cheap Gas',
    # image_url='static/CheapGasIcon.svg',
    # icon_url='static/CheapGasIcon.svg'
    # )
    # Category.objects.create(
    # name='Foodie',
    # image_url='static/FoodieIcon.svg',
    # icon_url='static/FoodieIcon.svg'
    # )
    # Category.objects.create(
    # name='Camping',
    # image_url='static/CampingIcon.svg',
    # icon_url='static/CampingIcon.svg'
    # )
    return JsonResponse({'message': 'Category Created'})

def addCountry(request):
    countries = [
    {'iso': 'AD', 'name': 'Andorra', 'nicename': 'Andorra', 'iso3': 'AND', 'numeric_code': '020', 'phone_code': '+376'},
    {'iso': 'AE', 'name': 'United Arab Emirates', 'nicename': 'United Arab Emirates', 'iso3': 'ARE', 'numeric_code': '784', 'phone_code': '+971'},
    {'iso': 'AF', 'name': 'Afghanistan', 'nicename': 'Afghanistan', 'iso3': 'AFG', 'numeric_code': '004', 'phone_code': '+93'},
    {'iso': 'AG', 'name': 'Antigua and Barbuda', 'nicename': 'Antigua and Barbuda', 'iso3': 'ATG', 'numeric_code': '028', 'phone_code': '+1268'},
    {'iso': 'AI', 'name': 'Anguilla', 'nicename': 'Anguilla', 'iso3': 'AIA', 'numeric_code': '660', 'phone_code': '+1264'},
    {'iso': 'AL', 'name': 'Albania', 'nicename': 'Albania', 'iso3': 'ALB', 'numeric_code': '008', 'phone_code': '+355'},
    {'iso': 'AM', 'name': 'Armenia', 'nicename': 'Armenia', 'iso3': 'ARM', 'numeric_code': '051', 'phone_code': '+374'},
    {'iso': 'AO', 'name': 'Angola', 'nicename': 'Angola', 'iso3': 'AGO', 'numeric_code': '024', 'phone_code': '+244'},
    {'iso': 'AR', 'name': 'Argentina', 'nicename': 'Argentina', 'iso3': 'ARG', 'numeric_code': '032', 'phone_code': '+54'},
    {'iso': 'AS', 'name': 'American Samoa', 'nicename': 'American Samoa', 'iso3': 'ASM', 'numeric_code': '016', 'phone_code': '+1684'},
    {'iso': 'AT', 'name': 'Austria', 'nicename': 'Austria', 'iso3': 'AUT', 'numeric_code': '040', 'phone_code': '+43'},
    {'iso': 'AU', 'name': 'Australia', 'nicename': 'Australia', 'iso3': 'AUS', 'numeric_code': '036', 'phone_code': '+61'},
    {'iso': 'AW', 'name': 'Aruba', 'nicename': 'Aruba', 'iso3': 'ABW', 'numeric_code': '533', 'phone_code': '+297'},
    {'iso': 'AX', 'name': 'Åland Islands', 'nicename': 'Åland Islands', 'iso3': 'ALA', 'numeric_code': '248', 'phone_code': '+35818'},
    {'iso': 'AZ', 'name': 'Azerbaijan', 'nicename': 'Azerbaijan', 'iso3': 'AZE', 'numeric_code': '031', 'phone_code': '+994'},
    {'iso': 'BA', 'name': 'Bosnia and Herzegovina', 'nicename': 'Bosnia and Herzegovina', 'iso3': 'BIH', 'numeric_code': '070', 'phone_code': '+387'},
    {'iso': 'BB', 'name': 'Barbados', 'nicename': 'Barbados', 'iso3': 'BRB', 'numeric_code': '052', 'phone_code': '+1246'},
    {'iso': 'BD', 'name': 'Bangladesh', 'nicename': 'Bangladesh', 'iso3': 'BGD', 'numeric_code': '050', 'phone_code': '+880'},
    {'iso': 'BE', 'name': 'Belgium', 'nicename': 'Belgium', 'iso3': 'BEL', 'numeric_code': '056', 'phone_code': '+32'},
    {'iso': 'BF', 'name': 'Burkina Faso', 'nicename': 'Burkina Faso', 'iso3': 'BFA', 'numeric_code': '854', 'phone_code': '+226'},
    {'iso': 'BG', 'name': 'Bulgaria', 'nicename': 'Bulgaria', 'iso3': 'BGR', 'numeric_code': '100', 'phone_code': '+359'},
    {'iso': 'BH', 'name': 'Bahrain', 'nicename': 'Bahrain', 'iso3': 'BHR', 'numeric_code': '048', 'phone_code': '+973'},
    {'iso': 'BI', 'name': 'Burundi', 'nicename': 'Burundi', 'iso3': 'BDI', 'numeric_code': '108', 'phone_code': '+257'},
    {'iso': 'BJ', 'name': 'Benin', 'nicename': 'Benin', 'iso3': 'BEN', 'numeric_code': '204', 'phone_code': '+229'},
    {'iso': 'BL', 'name': 'Saint Barthélemy', 'nicename': 'Saint Barthélemy', 'iso3': 'BLM', 'numeric_code': '652', 'phone_code': '+590'},
    {'iso': 'BM', 'name': 'Bermuda', 'nicename': 'Bermuda', 'iso3': 'BMU', 'numeric_code': '060', 'phone_code': '+1441'},
    {'iso': 'BN', 'name': 'Brunei Darussalam', 'nicename': 'Brunei Darussalam', 'iso3': 'BRN', 'numeric_code': '096', 'phone_code': '+673'},
    {'iso': 'BO', 'name': 'Bolivia', 'nicename': 'Bolivia', 'iso3': 'BOL', 'numeric_code': '068', 'phone_code': '+591'},
    {'iso': 'BQ', 'name': 'Bonaire, Sint Eustatius and Saba', 'nicename': 'Bonaire, Sint Eustatius and Saba', 'iso3': 'BES', 'numeric_code': '535', 'phone_code': '+599'},
    {'iso': 'BR', 'name': 'Brazil', 'nicename': 'Brazil', 'iso3': 'BRA', 'numeric_code': '076', 'phone_code': '+55'},
    {'iso': 'BS', 'name': 'Bahamas', 'nicename': 'Bahamas', 'iso3': 'BHS', 'numeric_code': '044', 'phone_code': '+1242'},
    {'iso': 'BT', 'name': 'Bhutan', 'nicename': 'Bhutan', 'iso3': 'BTN', 'numeric_code': '064', 'phone_code': '+975'},
    {'iso': 'BV', 'name': 'Bouvet Island', 'nicename': 'Bouvet Island', 'iso3': 'BVT', 'numeric_code': '074', 'phone_code': '+47'},
    {'iso': 'BW', 'name': 'Botswana', 'nicename': 'Botswana', 'iso3': 'BWA', 'numeric_code': '072', 'phone_code': '+267'},
    {'iso': 'BY', 'name': 'Belarus', 'nicename': 'Belarus', 'iso3': 'BLR', 'numeric_code': '112', 'phone_code': '+375'},
    {'iso': 'BZ', 'name': 'Belize', 'nicename': 'Belize', 'iso3': 'BLZ', 'numeric_code': '084', 'phone_code': '+501'},
    {'iso': 'CA', 'name': 'Canada', 'nicename': 'Canada', 'iso3': 'CAN', 'numeric_code': '124', 'phone_code': '+1'},
    {'iso': 'CC', 'name': 'Cocos (Keeling) Islands', 'nicename': 'Cocos (Keeling) Islands', 'iso3': 'CCK', 'numeric_code': '166', 'phone_code': '+61'},
    {'iso': 'CD', 'name': 'Congo', 'nicename': 'Congo', 'iso3': 'COD', 'numeric_code': '180', 'phone_code': '+243'},
    {'iso': 'CF', 'name': 'Central African Republic', 'nicename': 'Central African Republic', 'iso3': 'CAF', 'numeric_code': '140', 'phone_code': '+236'},
    {'iso': 'CG', 'name': 'Congo', 'nicename': 'Congo', 'iso3': 'COG', 'numeric_code': '178', 'phone_code': '+242'},
    {'iso': 'CH', 'name': 'Switzerland', 'nicename': 'Switzerland', 'iso3': 'CHE', 'numeric_code': '756', 'phone_code': '+41'},
    {'iso': 'CI', 'name': 'Ivory Coast', 'nicename': 'Ivory Coast', 'iso3': 'CIV', 'numeric_code': '384', 'phone_code': '+225'},
    {'iso': 'CK', 'name': 'Cook Islands', 'nicename': 'Cook Islands', 'iso3': 'COK', 'numeric_code': '184', 'phone_code': '+682'},
    {'iso': 'CL', 'name': 'Chile', 'nicename': 'Chile', 'iso3': 'CHL', 'numeric_code': '152', 'phone_code': '+56'},
    {'iso': 'CM', 'name': 'Cameroon', 'nicename': 'Cameroon', 'iso3': 'CMR', 'numeric_code': '120', 'phone_code': '+237'},
    {'iso': 'CN', 'name': 'China', 'nicename': 'China', 'iso3': 'CHN', 'numeric_code': '156', 'phone_code': '+86'},
    {'iso': 'CO', 'name': 'Colombia', 'nicename': 'Colombia', 'iso3': 'COL', 'numeric_code': '170', 'phone_code': '+57'},
    {'iso': 'CR', 'name': 'Costa Rica', 'nicename': 'Costa Rica', 'iso3': 'CRI', 'numeric_code': '188', 'phone_code': '+506'},
    {'iso': 'CU', 'name': 'Cuba', 'nicename': 'Cuba', 'iso3': 'CUB', 'numeric_code': '192', 'phone_code': '+53'},
    {'iso': 'CV', 'name': 'Cape Verde', 'nicename': 'Cape Verde', 'iso3': 'CPV', 'numeric_code': '132', 'phone_code': '+238'},
    {'iso': 'CW', 'name': 'Curaçao', 'nicename': 'Curaçao', 'iso3': 'CUW', 'numeric_code': '531', 'phone_code': '+599'},
    {'iso': 'CX', 'name': 'Christmas Island', 'nicename': 'Christmas Island', 'iso3': 'CXR', 'numeric_code': '162', 'phone_code': '+61'},
    {'iso': 'CY', 'name': 'Cyprus', 'nicename': 'Cyprus', 'iso3': 'CYP', 'numeric_code': '196', 'phone_code': '+357'},
    {'iso': 'CZ', 'name': 'Czech Republic', 'nicename': 'Czech Republic', 'iso3': 'CZE', 'numeric_code': '203', 'phone_code': '+420'},
    {'iso': 'DE', 'name': 'Germany', 'nicename': 'Germany', 'iso3': 'DEU', 'numeric_code': '276', 'phone_code': '+49'},
    {'iso': 'DJ', 'name': 'Djibouti', 'nicename': 'Djibouti', 'iso3': 'DJI', 'numeric_code': '262', 'phone_code': '+253'},
    {'iso': 'DK', 'name': 'Denmark', 'nicename': 'Denmark', 'iso3': 'DNK', 'numeric_code': '208', 'phone_code': '+45'},
    {'iso': 'DM', 'name': 'Dominica', 'nicename': 'Dominica', 'iso3': 'DMA', 'numeric_code': '212', 'phone_code': '+1767'},
    {'iso': 'DO', 'name': 'Dominican Republic', 'nicename': 'Dominican Republic', 'iso3': 'DOM', 'numeric_code': '214', 'phone_code': '+1809'},
    {'iso': 'DZ', 'name': 'Algeria', 'nicename': 'Algeria', 'iso3': 'DZA', 'numeric_code': '012', 'phone_code': '+213'},
    {'iso': 'EC', 'name': 'Ecuador', 'nicename': 'Ecuador', 'iso3': 'ECU', 'numeric_code': '218', 'phone_code': '+593'},
    {'iso': 'EE', 'name': 'Estonia', 'nicename': 'Estonia', 'iso3': 'EST', 'numeric_code': '233', 'phone_code': '+372'},
    {'iso': 'EG', 'name': 'Egypt', 'nicename': 'Egypt', 'iso3': 'EGY', 'numeric_code': '818', 'phone_code': '+20'},
    {'iso': 'EH', 'name': 'Western Sahara', 'nicename': 'Western Sahara', 'iso3': 'ESH', 'numeric_code': '732', 'phone_code': '+212'},
    {'iso': 'ER', 'name': 'Eritrea', 'nicename': 'Eritrea', 'iso3': 'ERI', 'numeric_code': '232', 'phone_code': '+291'},
    {'iso': 'ES', 'name': 'Spain', 'nicename': 'Spain', 'iso3': 'ESP', 'numeric_code': '724', 'phone_code': '+34'},
    {'iso': 'ET', 'name': 'Ethiopia', 'nicename': 'Ethiopia', 'iso3': 'ETH', 'numeric_code': '231', 'phone_code': '+251'},
    {'iso': 'FI', 'name': 'Finland', 'nicename': 'Finland', 'iso3': 'FIN', 'numeric_code': '246', 'phone_code': '+358'},
    {'iso': 'FJ', 'name': 'Fiji', 'nicename': 'Fiji', 'iso3': 'FJI', 'numeric_code': '242', 'phone_code': '+679'},
    {'iso': 'FM', 'name': 'Micronesia', 'nicename': 'Micronesia', 'iso3': 'FSM', 'numeric_code': '583', 'phone_code': '+691'},
    {'iso': 'FO', 'name': 'Faroe Islands', 'nicename': 'Faroe Islands', 'iso3': 'FRO', 'numeric_code': '234', 'phone_code': '+298'},
    {'iso': 'FR', 'name': 'France', 'nicename': 'France', 'iso3': 'FRA', 'numeric_code': '250', 'phone_code': '+33'},
    {'iso': 'GA', 'name': 'Gabon', 'nicename': 'Gabon', 'iso3': 'GAB', 'numeric_code': '266', 'phone_code': '+241'},
    {'iso': 'GB', 'name': 'United Kingdom', 'nicename': 'United Kingdom', 'iso3': 'GBR', 'numeric_code': '826', 'phone_code': '+44'},
    {'iso': 'GD', 'name': 'Grenada', 'nicename': 'Grenada', 'iso3': 'GRD', 'numeric_code': '308', 'phone_code': '+1473'},
    {'iso': 'GE', 'name': 'Georgia', 'nicename': 'Georgia', 'iso3': 'GEO', 'numeric_code': '268', 'phone_code': '+995'},
    {'iso': 'GF', 'name': 'French Guiana', 'nicename': 'French Guiana', 'iso3': 'GUF', 'numeric_code': '254', 'phone_code': '+594'},
    {'iso': 'GG', 'name': 'Guernsey', 'nicename': 'Guernsey', 'iso3': 'GGY', 'numeric_code': '831', 'phone_code': '+441481'},
    {'iso': 'GH', 'name': 'Ghana', 'nicename': 'Ghana', 'iso3': 'GHA', 'numeric_code': '288', 'phone_code': '+233'},
    {'iso': 'GI', 'name': 'Gibraltar', 'nicename': 'Gibraltar', 'iso3': 'GIB', 'numeric_code': '292', 'phone_code': '+350'},
    {'iso': 'GL', 'name': 'Greenland', 'nicename': 'Greenland', 'iso3': 'GRL', 'numeric_code': '304', 'phone_code': '+299'},
    {'iso': 'GM', 'name': 'Gambia', 'nicename': 'Gambia', 'iso3': 'GMB', 'numeric_code': '270', 'phone_code': '+220'},
    {'iso': 'GN', 'name': 'Guinea', 'nicename': 'Guinea', 'iso3': 'GIN', 'numeric_code': '324', 'phone_code': '+224'},
    {'iso': 'GP', 'name': 'Guadeloupe', 'nicename': 'Guadeloupe', 'iso3': 'GLP', 'numeric_code': '312', 'phone_code': '+590'},
    {'iso': 'GQ', 'name': 'Equatorial Guinea', 'nicename': 'Equatorial Guinea', 'iso3': 'GNQ', 'numeric_code': '226', 'phone_code': '+240'},
    {'iso': 'GR', 'name': 'Greece', 'nicename': 'Greece', 'iso3': 'GRC', 'numeric_code': '300', 'phone_code': '+30'},
    {'iso': 'GT', 'name': 'Guatemala', 'nicename': 'Guatemala', 'iso3': 'GTM', 'numeric_code': '320', 'phone_code': '+502'},
    {'iso': 'GU', 'name': 'Guam', 'nicename': 'Guam', 'iso3': 'GUM', 'numeric_code': '316', 'phone_code': '+1671'},
    {'iso': 'GW', 'name': 'Guinea-Bissau', 'nicename': 'Guinea-Bissau', 'iso3': 'GNB', 'numeric_code': '624', 'phone_code': '+245'},
    {'iso': 'GY', 'name': 'Guyana', 'nicename': 'Guyana', 'iso3': 'GUY', 'numeric_code': '328', 'phone_code': '+592'},
    {'iso': 'HK', 'name': 'Hong Kong', 'nicename': 'Hong Kong', 'iso3': 'HKG', 'numeric_code': '344', 'phone_code': '+852'},
    {'iso': 'HM', 'name': 'Heard Island and McDonald Islands', 'nicename': 'Heard Island and McDonald Islands', 'iso3': 'HMD', 'numeric_code': '334', 'phone_code': '+61'},
    {'iso': 'HN', 'name': 'Honduras', 'nicename': 'Honduras', 'iso3': 'HND', 'numeric_code': '340', 'phone_code': '+504'},
    {'iso': 'HR', 'name': 'Croatia', 'nicename': 'Croatia', 'iso3': 'HRV', 'numeric_code': '191', 'phone_code': '+385'},
    {'iso': 'HT', 'name': 'Haiti', 'nicename': 'Haiti', 'iso3': 'HTI', 'numeric_code': '332', 'phone_code': '+509'},
    {'iso': 'HU', 'name': 'Hungary', 'nicename': 'Hungary', 'iso3': 'HUN', 'numeric_code': '348', 'phone_code': '+36'},
    {'iso': 'ID', 'name': 'Indonesia', 'nicename': 'Indonesia', 'iso3': 'IDN', 'numeric_code': '360', 'phone_code': '+62'},
    {'iso': 'IE', 'name': 'Ireland', 'nicename': 'Ireland', 'iso3': 'IRL', 'numeric_code': '372', 'phone_code': '+353'},
    {'iso': 'IL', 'name': 'Israel', 'nicename': 'Israel', 'iso3': 'ISR', 'numeric_code': '376', 'phone_code': '+972'},
    {'iso': 'IM', 'name': 'Isle of Man', 'nicename': 'Isle of Man', 'iso3': 'IMN', 'numeric_code': '833', 'phone_code': '+441624'},
    {'iso': 'IN', 'name': 'India', 'nicename': 'India', 'iso3': 'IND', 'numeric_code': '356', 'phone_code': '+91'},
    {'iso': 'IO', 'name': 'British Indian Ocean Territory', 'nicename': 'British Indian Ocean Territory', 'iso3': 'IOT', 'numeric_code': '086', 'phone_code': '+246'},
    {'iso': 'IQ', 'name': 'Iraq', 'nicename': 'Iraq', 'iso3': 'IRQ', 'numeric_code': '368', 'phone_code': '+964'},
    {'iso': 'IR', 'name': 'Iran', 'nicename': 'Iran', 'iso3': 'IRN', 'numeric_code': '364', 'phone_code': '+98'},
    {'iso': 'IS', 'name': 'Iceland', 'nicename': 'Iceland', 'iso3': 'ISL', 'numeric_code': '352', 'phone_code': '+354'},
    {'iso': 'IT', 'name': 'Italy', 'nicename': 'Italy', 'iso3': 'ITA', 'numeric_code': '380', 'phone_code': '+39'},
    {'iso': 'JE', 'name': 'Jersey', 'nicename': 'Jersey', 'iso3': 'JEY', 'numeric_code': '832', 'phone_code': '+441534'},
    {'iso': 'JM', 'name': 'Jamaica', 'nicename': 'Jamaica', 'iso3': 'JAM', 'numeric_code': '388', 'phone_code': '+1876'},
    {'iso': 'JO', 'name': 'Jordan', 'nicename': 'Jordan', 'iso3': 'JOR', 'numeric_code': '400', 'phone_code': '+962'},
    {'iso': 'JP', 'name': 'Japan', 'nicename': 'Japan', 'iso3': 'JPN', 'numeric_code': '392', 'phone_code': '+81'},
    {'iso': 'KE', 'name': 'Kenya', 'nicename': 'Kenya', 'iso3': 'KEN', 'numeric_code': '404', 'phone_code': '+254'},
    {'iso': 'KG', 'name': 'Kyrgyzstan', 'nicename': 'Kyrgyzstan', 'iso3': 'KGZ', 'numeric_code': '417', 'phone_code': '+996'},
    {'iso': 'KH', 'name': 'Cambodia', 'nicename': 'Cambodia', 'iso3': 'KHM', 'numeric_code': '116', 'phone_code': '+855'},
    {'iso': 'KI', 'name': 'Kiribati', 'nicename': 'Kiribati', 'iso3': 'KIR', 'numeric_code': '296', 'phone_code': '+686'},
    {'iso': 'KM', 'name': 'Comoros', 'nicename': 'Comoros', 'iso3': 'COM', 'numeric_code': '174', 'phone_code': '+269'},
    {'iso': 'KN', 'name': 'Saint Kitts and Nevis', 'nicename': 'Saint Kitts and Nevis', 'iso3': 'KNA', 'numeric_code': '659', 'phone_code': '+1869'},
    {'iso': 'KP', 'name': 'North Korea', 'nicename': 'North Korea', 'iso3': 'PRK', 'numeric_code': '408', 'phone_code': '+850'},
    {'iso': 'KR', 'name': 'South Korea', 'nicename': 'South Korea', 'iso3': 'KOR', 'numeric_code': '410', 'phone_code': '+82'},
    {'iso': 'KW', 'name': 'Kuwait', 'nicename': 'Kuwait', 'iso3': 'KWT', 'numeric_code': '414', 'phone_code': '+965'},
    {'iso': 'KY', 'name': 'Cayman Islands', 'nicename': 'Cayman Islands', 'iso3': 'CYM', 'numeric_code': '136', 'phone_code': '+1345'},
    {'iso': 'KZ', 'name': 'Kazakhstan', 'nicename': 'Kazakhstan', 'iso3': 'KAZ', 'numeric_code': '398', 'phone_code': '+7'},
    {'iso': 'LA', 'name': 'Laos', 'nicename': 'Laos', 'iso3': 'LAO', 'numeric_code': '418', 'phone_code': '+856'},
    {'iso': 'LB', 'name': 'Lebanon', 'nicename': 'Lebanon', 'iso3': 'LBN', 'numeric_code': '422', 'phone_code': '+961'},
    {'iso': 'LC', 'name': 'Saint Lucia', 'nicename': 'Saint Lucia', 'iso3': 'LCA', 'numeric_code': '662', 'phone_code': '+1758'},
    {'iso': 'LI', 'name': 'Liechtenstein', 'nicename': 'Liechtenstein', 'iso3': 'LIE', 'numeric_code': '438', 'phone_code': '+423'},
    {'iso': 'LK', 'name': 'Sri Lanka', 'nicename': 'Sri Lanka', 'iso3': 'LKA', 'numeric_code': '144', 'phone_code': '+94'},
    {'iso': 'LR', 'name': 'Liberia', 'nicename': 'Liberia', 'iso3': 'LBR', 'numeric_code': '430', 'phone_code': '+231'},
    {'iso': 'LS', 'name': 'Lesotho', 'nicename': 'Lesotho', 'iso3': 'LSO', 'numeric_code': '426', 'phone_code': '+266'},
    {'iso': 'LT', 'name': 'Lithuania', 'nicename': 'Lithuania', 'iso3': 'LTU', 'numeric_code': '440', 'phone_code': '+370'},
    {'iso': 'LU', 'name': 'Luxembourg', 'nicename': 'Luxembourg', 'iso3': 'LUX', 'numeric_code': '442', 'phone_code': '+352'},
    {'iso': 'LV', 'name': 'Latvia', 'nicename': 'Latvia', 'iso3': 'LVA', 'numeric_code': '428', 'phone_code': '+371'},
    {'iso': 'LY', 'name': 'Libya', 'nicename': 'Libya', 'iso3': 'LBY', 'numeric_code': '434', 'phone_code': '+218'},
    {'iso': 'MA', 'name': 'Morocco', 'nicename': 'Morocco', 'iso3': 'MAR', 'numeric_code': '504', 'phone_code': '+212'},
    {'iso': 'MC', 'name': 'Monaco', 'nicename': 'Monaco', 'iso3': 'MCO', 'numeric_code': '492', 'phone_code': '+377'},
    {'iso': 'MD', 'name': 'Moldova', 'nicename': 'Moldova', 'iso3': 'MDA', 'numeric_code': '498', 'phone_code': '+373'},
    {'iso': 'ME', 'name': 'Montenegro', 'nicename': 'Montenegro', 'iso3': 'MNE', 'numeric_code': '499', 'phone_code': '+382'},
    {'iso': 'MF', 'name': 'Saint Martin', 'nicename': 'Saint Martin', 'iso3': 'MAF', 'numeric_code': '663', 'phone_code': '+590'},
    {'iso': 'MG', 'name': 'Madagascar', 'nicename': 'Madagascar', 'iso3': 'MDG', 'numeric_code': '450', 'phone_code': '+261'},
    {'iso': 'MH', 'name': 'Marshall Islands', 'nicename': 'Marshall Islands', 'iso3': 'MHL', 'numeric_code': '584', 'phone_code': '+692'},
    {'iso': 'MK', 'name': 'North Macedonia', 'nicename': 'North Macedonia', 'iso3': 'MKD', 'numeric_code': '807', 'phone_code': '+389'},
    {'iso': 'ML', 'name': 'Mali', 'nicename': 'Mali', 'iso3': 'MLI', 'numeric_code': '466', 'phone_code': '+223'},
    {'iso': 'MM', 'name': 'Myanmar', 'nicename': 'Myanmar', 'iso3': 'MMR', 'numeric_code': '104', 'phone_code': '+95'},
    {'iso': 'MN', 'name': 'Mongolia', 'nicename': 'Mongolia', 'iso3': 'MNG', 'numeric_code': '496', 'phone_code': '+976'},
    {'iso': 'MO', 'name': 'Macau', 'nicename': 'Macau', 'iso3': 'MAC', 'numeric_code': '446', 'phone_code': '+853'},
    {'iso': 'MP', 'name': 'Northern Mariana Islands', 'nicename': 'Northern Mariana Islands', 'iso3': 'MNP', 'numeric_code': '580', 'phone_code': '+1670'},
    {'iso': 'MQ', 'name': 'Martinique', 'nicename': 'Martinique', 'iso3': 'MTQ', 'numeric_code': '474', 'phone_code': '+596'},
    {'iso': 'MR', 'name': 'Mauritania', 'nicename': 'Mauritania', 'iso3': 'MRT', 'numeric_code': '478', 'phone_code': '+222'},
    {'iso': 'MS', 'name': 'Montserrat', 'nicename': 'Montserrat', 'iso3': 'MSR', 'numeric_code': '500', 'phone_code': '+1664'},
    {'iso': 'MT', 'name': 'Malta', 'nicename': 'Malta', 'iso3': 'MLT', 'numeric_code': '470', 'phone_code': '+356'},
    {'iso': 'MU', 'name': 'Mauritius', 'nicename': 'Mauritius', 'iso3': 'MUS', 'numeric_code': '480', 'phone_code': '+230'},
    {'iso': 'MV', 'name': 'Maldives', 'nicename': 'Maldives', 'iso3': 'MDV', 'numeric_code': '462', 'phone_code': '+960'},
    {'iso': 'MW', 'name': 'Malawi', 'nicename': 'Malawi', 'iso3': 'MWI', 'numeric_code': '454', 'phone_code': '+265'},
    {'iso': 'MX', 'name': 'Mexico', 'nicename': 'Mexico', 'iso3': 'MEX', 'numeric_code': '484', 'phone_code': '+52'},
    {'iso': 'MY', 'name': 'Malaysia', 'nicename': 'Malaysia', 'iso3': 'MYS', 'numeric_code': '458', 'phone_code': '+60'},
    {'iso': 'MZ', 'name': 'Mozambique', 'nicename': 'Mozambique', 'iso3': 'MOZ', 'numeric_code': '508', 'phone_code': '+258'},
    {'iso': 'NA', 'name': 'Namibia', 'nicename': 'Namibia', 'iso3': 'NAM', 'numeric_code': '516', 'phone_code': '+264'},
    {'iso': 'NC', 'name': 'New Caledonia', 'nicename': 'New Caledonia', 'iso3': 'NCL', 'numeric_code': '540', 'phone_code': '+687'},
    {'iso': 'NE', 'name': 'Niger', 'nicename': 'Niger', 'iso3': 'NER', 'numeric_code': '562', 'phone_code': '+227'},
    {'iso': 'NF', 'name': 'Norfolk Island', 'nicename': 'Norfolk Island', 'iso3': 'NFK', 'numeric_code': '574', 'phone_code': '+672'},
    {'iso': 'NG', 'name': 'Nigeria', 'nicename': 'Nigeria', 'iso3': 'NGA', 'numeric_code': '566', 'phone_code': '+234'},
    {'iso': 'NI', 'name': 'Nicaragua', 'nicename': 'Nicaragua', 'iso3': 'NIC', 'numeric_code': '558', 'phone_code': '+505'},
    {'iso': 'NL', 'name': 'Netherlands', 'nicename': 'Netherlands', 'iso3': 'NLD', 'numeric_code': '528', 'phone_code': '+31'},
    {'iso': 'NO', 'name': 'Norway', 'nicename': 'Norway', 'iso3': 'NOR', 'numeric_code': '578', 'phone_code': '+47'},
    {'iso': 'NP', 'name': 'Nepal', 'nicename': 'Nepal', 'iso3': 'NPL', 'numeric_code': '524', 'phone_code': '+977'},
    {'iso': 'NR', 'name': 'Nauru', 'nicename': 'Nauru', 'iso3': 'NRU', 'numeric_code': '520', 'phone_code': '+674'},
    {'iso': 'NU', 'name': 'Niue', 'nicename': 'Niue', 'iso3': 'NIU', 'numeric_code': '570', 'phone_code': '+683'},
    {'iso': 'NZ', 'name': 'New Zealand', 'nicename': 'New Zealand', 'iso3': 'NZL', 'numeric_code': '554', 'phone_code': '+64'},
    {'iso': 'OM', 'name': 'Oman', 'nicename': 'Oman', 'iso3': 'OMN', 'numeric_code': '512', 'phone_code': '+968'},
    {'iso': 'PA', 'name': 'Panama', 'nicename': 'Panama', 'iso3': 'PAN', 'numeric_code': '591', 'phone_code': '+507'},
    {'iso': 'PE', 'name': 'Peru', 'nicename': 'Peru', 'iso3': 'PER', 'numeric_code': '604', 'phone_code': '+51'},
    {'iso': 'PF', 'name': 'French Polynesia', 'nicename': 'French Polynesia', 'iso3': 'PYF', 'numeric_code': '258', 'phone_code': '+689'},
    {'iso': 'PG', 'name': 'Papua New Guinea', 'nicename': 'Papua New Guinea', 'iso3': 'PNG', 'numeric_code': '598', 'phone_code': '+675'},
    {'iso': 'PH', 'name': 'Philippines', 'nicename': 'Philippines', 'iso3': 'PHL', 'numeric_code': '608', 'phone_code': '+63'},
    {'iso': 'PK', 'name': 'Pakistan', 'nicename': 'Pakistan', 'iso3': 'PAK', 'numeric_code': '586', 'phone_code': '+92'},
    {'iso': 'PL', 'name': 'Poland', 'nicename': 'Poland', 'iso3': 'POL', 'numeric_code': '616', 'phone_code': '+48'},
    {'iso': 'PM', 'name': 'Saint Pierre and Miquelon', 'nicename': 'Saint Pierre and Miquelon', 'iso3': 'SPM', 'numeric_code': '666', 'phone_code': '+508'},
    {'iso': 'PN', 'name': 'Pitcairn Islands', 'nicename': 'Pitcairn Islands', 'iso3': 'PCN', 'numeric_code': '612', 'phone_code': '+872'},
    {'iso': 'PR', 'name': 'Puerto Rico', 'nicename': 'Puerto Rico', 'iso3': 'PRI', 'numeric_code': '630', 'phone_code': '+1787'},
    {'iso': 'PT', 'name': 'Portugal', 'nicename': 'Portugal', 'iso3': 'PRT', 'numeric_code': '620', 'phone_code': '+351'},
    {'iso': 'PW', 'name': 'Palau', 'nicename': 'Palau', 'iso3': 'PLW', 'numeric_code': '585', 'phone_code': '+680'},
    {'iso': 'PY', 'name': 'Paraguay', 'nicename': 'Paraguay', 'iso3': 'PRY', 'numeric_code': '600', 'phone_code': '+595'},
    {'iso': 'QA', 'name': 'Qatar', 'nicename': 'Qatar', 'iso3': 'QAT', 'numeric_code': '634', 'phone_code': '+974'},
    {'iso': 'RE', 'name': 'Réunion', 'nicename': 'Réunion', 'iso3': 'REU', 'numeric_code': '638', 'phone_code': '+262'},
    {'iso': 'RO', 'name': 'Romania', 'nicename': 'Romania', 'iso3': 'ROU', 'numeric_code': '642', 'phone_code': '+40'},
    {'iso': 'RS', 'name': 'Serbia', 'nicename': 'Serbia', 'iso3': 'SRB', 'numeric_code': '688', 'phone_code': '+381'},
    {'iso': 'RU', 'name': 'Russia', 'nicename': 'Russia', 'iso3': 'RUS', 'numeric_code': '643', 'phone_code': '+7'},
    {'iso': 'RW', 'name': 'Rwanda', 'nicename': 'Rwanda', 'iso3': 'RWA', 'numeric_code': '646', 'phone_code': '+250'},
    {'iso': 'SA', 'name': 'Saudi Arabia', 'nicename': 'Saudi Arabia', 'iso3': 'SAU', 'numeric_code': '682', 'phone_code': '+966'},
    {'iso': 'SB', 'name': 'Solomon Islands', 'nicename': 'Solomon Islands', 'iso3': 'SLB', 'numeric_code': '090', 'phone_code': '+677'},
    {'iso': 'SC', 'name': 'Seychelles', 'nicename': 'Seychelles', 'iso3': 'SYC', 'numeric_code': '690', 'phone_code': '+248'},
    {'iso': 'SD', 'name': 'Sudan', 'nicename': 'Sudan', 'iso3': 'SDN', 'numeric_code': '729', 'phone_code': '+249'},
    {'iso': 'SE', 'name': 'Sweden', 'nicename': 'Sweden', 'iso3': 'SWE', 'numeric_code': '752', 'phone_code': '+46'},
    {'iso': 'SG', 'name': 'Singapore', 'nicename': 'Singapore', 'iso3': 'SGP', 'numeric_code': '702', 'phone_code': '+65'},
    {'iso': 'SH', 'name': 'Saint Helena', 'nicename': 'Saint Helena', 'iso3': 'SHN', 'numeric_code': '654', 'phone_code': '+290'},
    {'iso': 'SI', 'name': 'Slovenia', 'nicename': 'Slovenia', 'iso3': 'SVN', 'numeric_code': '705', 'phone_code': '+386'},
    {'iso': 'SJ', 'name': 'Svalbard and Jan Mayen', 'nicename': 'Svalbard and Jan Mayen', 'iso3': 'SJM', 'numeric_code': '744', 'phone_code': '+47'},
    {'iso': 'SK', 'name': 'Slovakia', 'nicename': 'Slovakia', 'iso3': 'SVK', 'numeric_code': '703', 'phone_code': '+421'},
    {'iso': 'SL', 'name': 'Sierra Leone', 'nicename': 'Sierra Leone', 'iso3': 'SLE', 'numeric_code': '694', 'phone_code': '+232'},
    {'iso': 'SM', 'name': 'San Marino', 'nicename': 'San Marino', 'iso3': 'SMR', 'numeric_code': '674', 'phone_code': '+378'},
    {'iso': 'SN', 'name': 'Senegal', 'nicename': 'Senegal', 'iso3': 'SEN', 'numeric_code': '686', 'phone_code': '+221'},
    {'iso': 'SO', 'name': 'Somalia', 'nicename': 'Somalia', 'iso3': 'SOM', 'numeric_code': '706', 'phone_code': '+252'},
    {'iso': 'SR', 'name': 'Suriname', 'nicename': 'Suriname', 'iso3': 'SUR', 'numeric_code': '740', 'phone_code': '+597'},
    {'iso': 'SS', 'name': 'South Sudan', 'nicename': 'South Sudan', 'iso3': 'SSD', 'numeric_code': '728', 'phone_code': '+211'},
    {'iso': 'ST', 'name': 'São Tomé and Príncipe', 'nicename': 'São Tomé and Príncipe', 'iso3': 'STP', 'numeric_code': '678', 'phone_code': '+239'},
    {'iso': 'SV', 'name': 'El Salvador', 'nicename': 'El Salvador', 'iso3': 'SLV', 'numeric_code': '222', 'phone_code': '+503'},
    {'iso': 'SX', 'name': 'Sint Maarten', 'nicename': 'Sint Maarten', 'iso3': 'SXM', 'numeric_code': '534', 'phone_code': '+1721'},
    {'iso': 'SY', 'name': 'Syria', 'nicename': 'Syria', 'iso3': 'SYR', 'numeric_code': '760', 'phone_code': '+963'},
    {'iso': 'SZ', 'name': 'Eswatini', 'nicename': 'Eswatini', 'iso3': 'SWZ', 'numeric_code': '748', 'phone_code': '+268'},
    {'iso': 'TC', 'name': 'Turks and Caicos Islands', 'nicename': 'Turks and Caicos Islands', 'iso3': 'TCA', 'numeric_code': '796', 'phone_code': '+1649'},
    {'iso': 'TD', 'name': 'Chad', 'nicename': 'Chad', 'iso3': 'TCD', 'numeric_code': '148', 'phone_code': '+235'},
    {'iso': 'TF', 'name': 'French Southern Territories', 'nicename': 'French Southern Territories', 'iso3': 'ATF', 'numeric_code': '260', 'phone_code': '+262'},
    {'iso': 'TG', 'name': 'Togo', 'nicename': 'Togo', 'iso3': 'TGO', 'numeric_code': '768', 'phone_code': '+228'},
    {'iso': 'TH', 'name': 'Thailand', 'nicename': 'Thailand', 'iso3': 'THA', 'numeric_code': '764', 'phone_code': '+66'},
    {'iso': 'TJ', 'name': 'Tajikistan', 'nicename': 'Tajikistan', 'iso3': 'TJK', 'numeric_code': '762', 'phone_code': '+992'},
    {'iso': 'TK', 'name': 'Tokelau', 'nicename': 'Tokelau', 'iso3': 'TKL', 'numeric_code': '772', 'phone_code': '+690'},
    {'iso': 'TL', 'name': 'Timor-Leste', 'nicename': 'Timor-Leste', 'iso3': 'TLS', 'numeric_code': '626', 'phone_code': '+670'},
    {'iso': 'TM', 'name': 'Turkmenistan', 'nicename': 'Turkmenistan', 'iso3': 'TKM', 'numeric_code': '795', 'phone_code': '+993'},
    {'iso': 'TN', 'name': 'Tunisia', 'nicename': 'Tunisia', 'iso3': 'TUN', 'numeric_code': '788', 'phone_code': '+216'},
    {'iso': 'TO', 'name': 'Tonga', 'nicename': 'Tonga', 'iso3': 'TON', 'numeric_code': '776', 'phone_code': '+676'},
    {'iso': 'TR', 'name': 'Turkey', 'nicename': 'Turkey', 'iso3': 'TUR', 'numeric_code': '792', 'phone_code': '+90'},
    {'iso': 'TT', 'name': 'Trinidad and Tobago', 'nicename': 'Trinidad and Tobago', 'iso3': 'TTO', 'numeric_code': '780', 'phone_code': '+1868'},
    {'iso': 'TV', 'name': 'Tuvalu', 'nicename': 'Tuvalu', 'iso3': 'TUV', 'numeric_code': '798', 'phone_code': '+688'},
    {'iso': 'TZ', 'name': 'Tanzania', 'nicename': 'Tanzania', 'iso3': 'TZA', 'numeric_code': '834', 'phone_code': '+255'},
    {'iso': 'UA', 'name': 'Ukraine', 'nicename': 'Ukraine', 'iso3': 'UKR', 'numeric_code': '804', 'phone_code': '+380'},
    {'iso': 'UG', 'name': 'Uganda', 'nicename': 'Uganda', 'iso3': 'UGA', 'numeric_code': '800', 'phone_code': '+256'},
    # {'iso': 'UM', 'name': 'United States Minor Outlying Islands', 'nicename': 'United States Minor Outlying Islands', 'iso3': 'UMI', 'numeric_code': '581', 'phone_code': '+1-'},
    {'iso': 'US', 'name': 'United States', 'nicename': 'United States', 'iso3': 'USA', 'numeric_code': '840', 'phone_code': '+1'},
    {'iso': 'UY', 'name': 'Uruguay', 'nicename': 'Uruguay', 'iso3': 'URY', 'numeric_code': '858', 'phone_code': '+598'},
    {'iso': 'UZ', 'name': 'Uzbekistan', 'nicename': 'Uzbekistan', 'iso3': 'UZB', 'numeric_code': '860', 'phone_code': '+998'},
    {'iso': 'VA', 'name': 'Vatican City', 'nicename': 'Vatican City', 'iso3': 'VAT', 'numeric_code': '336', 'phone_code': '+379'},
    {'iso': 'VC', 'name': 'Saint Vincent and the Grenadines', 'nicename': 'Saint Vincent and the Grenadines', 'iso3': 'VCT', 'numeric_code': '670', 'phone_code': '+1784'},
    {'iso': 'VE', 'name': 'Venezuela', 'nicename': 'Venezuela', 'iso3': 'VEN', 'numeric_code': '862', 'phone_code': '+58'},
    {'iso': 'VG', 'name': 'British Virgin Islands', 'nicename': 'British Virgin Islands', 'iso3': 'VGB', 'numeric_code': '092', 'phone_code': '+1284'},
    {'iso': 'VI', 'name': 'United States Virgin Islands', 'nicename': 'United States Virgin Islands', 'iso3': 'VIR', 'numeric_code': '850', 'phone_code': '+1340'},
    {'iso': 'VN', 'name': 'Vietnam', 'nicename': 'Vietnam', 'iso3': 'VNM', 'numeric_code': '704', 'phone_code': '+84'},
    {'iso': 'VU', 'name': 'Vanuatu', 'nicename': 'Vanuatu', 'iso3': 'VUT', 'numeric_code': '548', 'phone_code': '+678'},
    {'iso': 'WF', 'name': 'Wallis and Futuna', 'nicename': 'Wallis and Futuna', 'iso3': 'WLF', 'numeric_code': '876', 'phone_code': '+681'},
    {'iso': 'WS', 'name': 'Samoa', 'nicename': 'Samoa', 'iso3': 'WSM', 'numeric_code': '882', 'phone_code': '+685'},
    {'iso': 'YE', 'name': 'Yemen', 'nicename': 'Yemen', 'iso3': 'YEM', 'numeric_code': '887', 'phone_code': '+967'},
    {'iso': 'YT', 'name': 'Mayotte', 'nicename': 'Mayotte', 'iso3': 'MYT', 'numeric_code': '175', 'phone_code': '+262'},
    {'iso': 'ZA', 'name': 'South Africa', 'nicename': 'South Africa', 'iso3': 'ZAF', 'numeric_code': '710', 'phone_code': '+27'},
    {'iso': 'ZM', 'name': 'Zambia', 'nicename': 'Zambia', 'iso3': 'ZMB', 'numeric_code': '894', 'phone_code': '+260'},
    {'iso': 'ZW', 'name': 'Zimbabwe', 'nicename': 'Zimbabwe', 'iso3': 'ZWE', 'numeric_code': '716', 'phone_code': '+263'}
]

    for country in countries:
        Country.objects.create(**country)
    # Country.objects.create(
    #     iso = '',
    # name = 'India',
    # nicename = 'IN',
    # iso3 = 'IN',
    # numeric_code = '91',
    # phone_code = '+91',
    # )
    # Country.objects.create(
    #     iso = '',
    # name = 'America',
    # nicename = 'US',
    # iso3 = 'US',
    # numeric_code = '1',
    # phone_code = '+1'
    # )
    # priorityList=[
    #     'Planning a vacation',
    #     'Taking a road trip',
    #     'Save Money',
    # ]
    # for priorityName in priorityList:
    #     Priority.objects.create(
    #         name=priorityName
    #     )
    # travelGoalList=[
    #     '✈️ Travel abroad',
    #     '✴️ Diverse cultures',
    #     '🎓 Education',
    #     '👁️ Spectacular views',
    #     '🌲 Seeing wildlife',
    #     '🏴 Metropolitan',
    #     '🥘 Trying new food',
    #     '🤠 Adventure',
    #     '🤝 Events',
    #     '🏖️Tropical',
    #     '📴 Off-grid',
    #     '🌊 Water',
    # ]
    # for goalName in travelGoalList:
    #     TravelGoal.objects.create(
    #         name=goalName
    #     )
    # Motivation.objects.create(
    #     name='Price',
    #     emoji='🤑'
    # )
    # Motivation.objects.create(
    #     name='Comfort',
    #     emoji='😌'
    # )
    # Motivation.objects.create(
    #     name='Convenience',
    #     emoji='😇'
    # )
    # Motivation.objects.create(
    #     name='Loyalty Miles',
    #     emoji='🤩'
    # )
    # Motivation.objects.create(
    #     name='Speed',
    #     emoji='😎'
    # )
    # AirlineBrand.objects.create(
    #     name='Delta'
    # )
    # AirlineBrand.objects.create(
    #     name='Air India'
    # )
    # HotelBrand.objects.create(
    #     name='Marriott'
    # )
    # HotelBrand.objects.create(
    #     name='Hilton Hotels & Resorts'
    # )
    # RestaurantBrand.objects.create(
    #     name='KFC'
    # )
    # RestaurantBrand.objects.create(
    #     name='Pizza Hut'
    # )
    
    
    return JsonResponse({'message': 'Country added'})
    
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

    City.objects.create(
      name='Miami',
      country='US',
      latitude=25.761670,
      longitude=-80.22534,
      images=['static/Miami.jpeg'],
      description='Miami, officially the City of Miami, is a coastal city in the U.S. state of Florida and the seat of Miami-Dade County in South Florida'
    )
    
    City.objects.create(
      name='Jacksonville',
      country='US',
      latitude=30.387233,
      longitude=-81.670820,
      images=['static/Jacksonville.jpeg','static/Jacksonville2.jpeg'],
      description='Jacksonville is the most populous city proper in the U.S. state of Florida, located on the Atlantic coast of northeastern Florida. It is the seat of Duval County, with which the City of Jacksonville consolidated in 1968. It was the largest city by area in the contiguous United States as of 2020'
    )
    return JsonResponse({'message': 'City fetched and saved successfully'})


def historicalSitesScrape(request):
    miami=City.objects.filter(id='0e872ebf-e377-41e5-a9d1-36297c2dea6b').first()
    jacksonville=City.objects.filter(id='8a8da460-2ec4-496e-82de-58f2f1726257').first()
    HistoricalSite.objects.create(
        name='Vizcaya',
        description='This beautiful estate was built by industrialist James Deering in the early 20th century. It features a stunning Italian Renaissance-style villa',
        images=['static/Vizcaya.png'],
        city=miami,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    HistoricalSite.objects.create(
        name='Jacksonville',
        description='This beautiful estate was built by industrialist James Deering in the early 20th century. It features a stunning Italian Renaissance-style villa',
        images=['static/Jacksonville.jpeg'],
        city=jacksonville,
        latitude=miami.latitude,
        longitude=miami.longitude,
    )
    return JsonResponse({'message': 'HistoricalSite fetched and saved successfully'})


def weird(request):
    miami=City.objects.filter(id='0e872ebf-e377-41e5-a9d1-36297c2dea6b').first()
    jacksonville=City.objects.filter(id='8a8da460-2ec4-496e-82de-58f2f1726257').first()
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
    planModel=Plan.objects.filter(id=data['plan_id']).first()
    
    userdata=User.objects.filter(id=data['user_id']).first()
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
    else :
        user_likes = UserLikes.objects.create(user=userdata)
    
    if HistoricalSite.objects.filter(id=data['like_id']).exists():
        historicalsite = HistoricalSite.objects.get(id=data['like_id'])
        UserLikesHistoricalSite.objects.create(
            userlikes=user_likes,
            historicalsite=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Historical Site'})
    
    # if HistoricalSite.objects.filter(id=data['like_id']).exists():
    #     historicalsites=HistoricalSite.objects.get(id=data['like_id'])
    #     user_likes.liked_historicalsites.add(historicalsites)
    #     return JsonResponse({'message': 'User Liked Historical Site'})
        
    # if Hotel.objects.filter(id=data['like_id']).exists():
    #     hotel = Hotel.objects.get(id=data['like_id'])
    #     user_likes.liked_hotels.add(hotel)
    #     return JsonResponse({'message': 'User Liked Hotel'})
    
    if Hotel.objects.filter(id=data['like_id']).exists():
        historicalsite = Hotel.objects.get(id=data['like_id'])
        UserLikesHotel.objects.create(
            userlikes=user_likes,
            hotel=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Hotel'})
        
    # if ExtremeSport.objects.filter(id=data['like_id']).exists():
    #     extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
    #     user_likes.liked_extremesports.add(extreme_sport)
    #     return JsonResponse({'message': 'User Liked Extreme Sport'})
    
    if ExtremeSport.objects.filter(id=data['like_id']).exists():
        historicalsite = ExtremeSport.objects.get(id=data['like_id'])
        UserLikesExtremeSport.objects.create(
            userlikes=user_likes,
            extremesport=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Extreme Sport'})
        
    # if Event.objects.filter(id=data['like_id']).exists():
    #     event = Event.objects.get(id=data['like_id'])
    #     user_likes.liked_events.add(event)
    #     return JsonResponse({'message': 'User Liked Event'})
    
    if Event.objects.filter(id=data['like_id']).exists():
        historicalsite = Event.objects.get(id=data['like_id'])
        UserLikesEvent.objects.create(
            userlikes=user_likes,
            event=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Event'})
        
    # if WeirdAndWacky.objects.filter(id=data['like_id']).exists():
    #     weird_and_wacky = WeirdAndWacky.objects.get(id=data['like_id'])
    #     user_likes.liked_wierdandwacky.add(weird_and_wacky)
    #     return JsonResponse({'message': 'User Liked Weird And Wacky'})
    
    if WeirdAndWacky.objects.filter(id=data['like_id']).exists():
        historicalsite = WeirdAndWacky.objects.get(id=data['like_id'])
        UserLikesWeirdAndWacky.objects.create(
            userlikes=user_likes,
            weirdandwacky=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Weird And Wacky'})
        
    # if Park.objects.filter(id=data['like_id']).exists():
    #     park = Park.objects.get(id=data['like_id'])
    #     user_likes.liked_parks.add(park)
    #     return JsonResponse({'message': 'User Liked Park'})
    
    if Park.objects.filter(id=data['like_id']).exists():
        historicalsite = Park.objects.get(id=data['like_id'])
        UserLikesPark.objects.create(
            userlikes=user_likes,
            park=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Park'})
    
    # if Attraction.objects.filter(id=data['like_id']).exists():
    #     attraction = Attraction.objects.get(id=data['like_id'])
    #     user_likes.liked_attractions.add(attraction)
    #     return JsonResponse({'message': 'User Liked Attraction'})
    
    if Attraction.objects.filter(id=data['like_id']).exists():
        historicalsite = Attraction.objects.get(id=data['like_id'])
        UserLikesAttraction.objects.create(
            userlikes=user_likes,
            attraction=historicalsite,
            plan=planModel
            ) 
        return JsonResponse({'message': 'User Liked Attraction'})
    
    
@api_view(['POST'])
def isPlaceLiked(request):
    data = json.loads(request.body)
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
        if user_likes and user_likes.liked_historicalsites_new.filter(id=data['like_id']).exists():
            # historicalsites=HistoricalSite.objects.filter(id=data['like_id']).first()
            
            return JsonResponse({'message': 'User Liked Historical Site',
                                 'liked':True})
        
        if user_likes and user_likes.liked_hotels_new.filter(id=data['like_id']).exists():
            # hotel = Hotel.objects.get(id=data['like_id'])
            # user_likes.liked_hotels.add(hotel)
            return JsonResponse({'message': 'User Liked Hotel',
                                 'liked':True})

        if user_likes and user_likes.liked_extremesports_new.filter(id=data['like_id']).exists():
            # extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
            # user_likes.liked_extremesports.add(extreme_sport)
            return JsonResponse({'message': 'User Liked Extreme Sport',
                                 'liked':True})

        if user_likes and user_likes.liked_events_new.filter(id=data['like_id']).exists():
            # event = Event.objects.get(id=data['like_id'])
            # user_likes.liked_events.add(event)
            return JsonResponse({'message': 'User Liked Event',
                                 'liked':True})

        if user_likes and user_likes.liked_wierdandwacky_new.filter(id=data['like_id']).exists():
            return JsonResponse({'message': 'User Liked Weird And Wacky',
                                 'liked':True})

        if user_likes and user_likes.liked_parks_new.filter(id=data['like_id']).exists():
            # park = Park.objects.get(id=data['like_id'])
            # user_likes.liked_parks.add(park)
            return JsonResponse({'message': 'User Liked Park','liked':True})

        if user_likes and user_likes.liked_attractions_new.filter(id=data['like_id']).exists():
            # attraction = Attraction.objects.get(id=data['like_id'])
            # user_likes.liked_attractions.add(attraction)
            return JsonResponse({'message': 'User Liked Attraction','liked':True})
        
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
    else :
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
        
        

@api_view(['POST'])
def isPlaceLikedInPlan(request):
    data = json.loads(request.body)
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()

    
        
        if user_likes and UserLikesHistoricalSite.objects.filter(historicalsite_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            return JsonResponse({'message': 'User Liked Historical Site',
                                 'liked':True})
        
        if user_likes and UserLikesHotel.objects.filter(hotel_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            # hotel = Hotel.objects.get(id=data['like_id'])
            # user_likes.liked_hotels.add(hotel)
            return JsonResponse({'message': 'User Liked Hotel',
                                 'liked':True})

        if user_likes and UserLikesExtremeSport.objects.filter(extremesport_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            # extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
            # user_likes.liked_extremesports.add(extreme_sport)
            return JsonResponse({'message': 'User Liked Extreme Sport',
                                 'liked':True})

        if user_likes and UserLikesEvent.objects.filter(event_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            # event = Event.objects.get(id=data['like_id'])
            # user_likes.liked_events.add(event)
            return JsonResponse({'message': 'User Liked Event',
                                 'liked':True})

        if user_likes and UserLikesWeirdAndWacky.objects.filter(weirdandwacky_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            return JsonResponse({'message': 'User Liked Weird And Wacky',
                                 'liked':True})

        if user_likes and UserLikesPark.objects.filter(park_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            # park = Park.objects.get(id=data['like_id'])
            # user_likes.liked_parks.add(park)
            return JsonResponse({'message': 'User Liked Park','liked':True})

        if user_likes and UserLikesAttraction.objects.filter(attraction_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            # attraction = Attraction.objects.get(id=data['like_id'])
            # user_likes.liked_attractions.add(attraction)
            return JsonResponse({'message': 'User Liked Attraction','liked':True})
        
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
    else :
        return JsonResponse({
            'message': 'User Did not like',
            'liked':False})
        
@api_view(['POST'])
def unlikePlace(request):
    data = json.loads(request.body)
    
    if UserLikes.objects.filter(user_id=data['user_id']).exists():
        user_likes = UserLikes.objects.filter(user_id=data['user_id']).first()
        
        if user_likes and UserLikesHistoricalSite.objects.filter(historicalsite_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesHistoricalSite.objects.filter(historicalsite_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            return JsonResponse({'message': 'User Unliked Historical Site',
                                 'liked':False})
            
       
        
        if user_likes and  UserLikesHotel.objects.filter(hotel_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesHotel.objects.filter(hotel_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            
            return JsonResponse({'message': 'User Unliked Hotel',
                                 'liked':False})
            
        # if user_likes and user_likes.liked_hotels_new.filter(id=data['like_id']).exists():
        #     # hotel = Hotel.objects.get(id=data['like_id'])
        #     # user_likes.liked_hotels.add(hotel)
        #     return JsonResponse({'message': 'User Liked Hotel',
        #                          'liked':False})
        
        if user_likes and  UserLikesExtremeSport.objects.filter(extremesport_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesExtremeSport.objects.filter(extremesport_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            
            return JsonResponse({'message': 'User Unliked Extreme Sport',
                                 'liked':False})

        # if user_likes and user_likes.liked_extremesports_new.filter(id=data['like_id']).exists():
        #     # extreme_sport = ExtremeSport.objects.get(id=data['like_id'])
        #     # user_likes.liked_extremesports.add(extreme_sport)
        #     return JsonResponse({'message': 'User Liked Extreme Sport',
        #                          'liked':False})
        
       
        
        if user_likes and  UserLikesEvent.objects.filter(event_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesEvent.objects.filter(event_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
        
            return JsonResponse({'message': 'User Unliked Event',
                                 'liked':False})

        # if user_likes and user_likes.liked_events_new.filter(id=data['like_id']).exists():
        #     # event = Event.objects.get(id=data['like_id'])
        #     # user_likes.liked_events.add(event)
        #     return JsonResponse({'message': 'User Liked Event',
        #                          'liked':False})



        if user_likes and UserLikesWeirdAndWacky.objects.filter(weirdandwacky_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesWeirdAndWacky.objects.filter(weirdandwacky_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            
            return JsonResponse({'message': 'User Unliked Weird And Wacky',
                                 'liked':False})
            
        # if user_likes and user_likes.liked_wierdandwacky_new.filter(id=data['like_id']).exists():
        #     return JsonResponse({'message': 'User Liked Weird And Wacky',
        #                          'liked':False})



        if user_likes and UserLikesPark.objects.filter(park_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesPark.objects.filter(park_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            
            return JsonResponse({'message': 'User Unliked Park',
                                 'liked':False})
            
        # if user_likes and user_likes.liked_parks_new.filter(id=data['like_id']).exists():
        #     # park = Park.objects.get(id=data['like_id'])
        #     # user_likes.liked_parks.add(park)
        #     return JsonResponse({'message': 'User Liked Park','liked':False})
        
        if user_likes and UserLikesAttraction.objects.filter(park_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).exists():
            UserLikesAttraction.objects.filter(park_id=data['like_id'],plan_id=data['plan_id'],userlikes_id=user_likes.id).delete()
            
            return JsonResponse({'message': 'User Unliked Attractions',
                                 'liked':False})

        # if user_likes and user_likes.liked_attractions_new.filter(id=data['like_id']).exists():
        #     # attraction = Attraction.objects.get(id=data['like_id'])
        #     # user_likes.liked_attractions.add(attraction)
        #     return JsonResponse({'message': 'User Liked Attraction','liked':False})
        
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
    plan=Plan(
    name = data['name'],
    description = data['description'],
    start_date = data['start_date'],
    end_date = data['end_date'],
    city=city,
    
    created_at=date.today().strftime('%Y-%m-%d %H:%M:%S') 
    )
    plan.save()
    PlanUser.objects.create(
        plan=plan,
        user=user
    )
    
    if not Plan.objects.filter(id=plan.id).exists():
        return JsonResponse({'message': 'Plan does not exist'},safe=False, status=status.HTTP_404_NOT_FOUND)
    
    plans = Plan.objects.filter(id=plan.id).select_related('city').values(
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
def addUserToPlan(request):
    print('createPlan called')
    data = json.loads(request.body)
    if not User.objects.filter(id=data['user_id']).exists():
        return JsonResponse({'message': 'User does not exist'},safe=False, status=400)
    
    if not Plan.objects.filter(id=data['plan_id']).exists():
        return JsonResponse({'message': 'Plan does not exist'},safe=False, status=400)
    
    if not PlanUser.objects.filter(plan_id=data['plan_id'], user_id=data['user_id']).exists():
        plan=Plan.objects.filter(id=data['plan_id']).first()
        user=User.objects.filter(id=data['user_id']).first()
        PlanUser.objects.create(
            plan=plan,
            user=user
        )
        return JsonResponse({'message': 'User Added'},safe=False, status=200)
    else:
        return JsonResponse({'message': 'User already added'},safe=False, status=400)


@api_view(['POST'])
def getTripPlan(request):
    data = json.loads(request.body)
    
    # Check if PlanUser with given user_id exists
    if not PlanUser.objects.filter(user_id=data['user_id']).exists():
        return JsonResponse([], safe=False, status=status.HTTP_200_OK)
    
    # Retrieve all PlanUser objects for the given user_id
    planUserList = PlanUser.objects.filter(user_id=data['user_id'])
    
    plans_list = []
    for planUser in planUserList:
        # Correctly access plan_id attribute
        plans = list(Plan.objects.filter(id=planUser.plan_id).select_related('city').values(
            'id', 'name', 'city__id', 'city__name', 'city__images'
        ))
        
        # Each plan is a dictionary, append each to plans_list
        plans_list.extend(plans)
    
    # Flatten the list of dictionaries
    for plan in plans_list:
        plan['city_name'] = plan.pop('city__name')
        plan['city_images'] = plan.pop('city__images')
        plan['city_id'] = plan.pop('city__id')
    
    return JsonResponse(plans_list, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def getTripViaId(request, id=None):
    
    if not Plan.objects.filter(id=id).exists():
        return JsonResponse({'message': 'Plan does not exist'},safe=False, status=status.HTTP_404_NOT_FOUND)
    
    plans = Plan.objects.filter(id=id).select_related('city').values(
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
def getExperienceSites(request):
    data = json.loads(request.body)
    plans = HistoricalSite.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getHotelSites(request):
    data = json.loads(request.body)
    plans = Hotel.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getParkSites(request):
    data = json.loads(request.body)
    plans = Park.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getEventSites(request):
    data = json.loads(request.body)
    plans = Event.objects.filter(city_id=data['city_id']).all().values(
        'id', 'name', 
        'description', 'images',
    )
    print(len(plans))
    plans_list = list(plans)
    
    return JsonResponse(plans_list, safe=False,status=status.HTTP_200_OK)

def getUsersForLikes(plan_id):
    imageList=[]
    userList =UserLikesHistoricalSite.objects.filter(plan_id=plan_id).all()\
                .values('historicalsite_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('historicalsite_id','id','userlikes_id','user_id')
            
            
    for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).values(
    'profile_pic_id', profile_picture=F('profile_pic__media_url')
)
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
    return imageList


@api_view(['POST'])
def getUserAssignedToPlan(request):
    data=json.loads(request.body)
    plan_id=data['plan_id']
    imageList=[]
    userList =PlanUser.objects.filter(plan_id=plan_id).all()\
               .values('id','user_id')
    print("userList = ",len(userList))
               
    for users in userList:
               profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                   values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
               for pic in profile_pic:
                   imageList.append({
                   "user_id":users['user_id'],
                   "profile_pic_id":pic['profile_pic_id'],
                   "profile_picture":pic['profile_picture'],
               })
                   users["profile_pic_id"]=pic['profile_pic_id']
                   users["profile_picture"]=pic['profile_picture']
               print('profile_pic = ',profile_pic)
    # for plan in userList:
    #              plan['users']=list(imageList)
    return JsonResponse(list(userList) ,safe=False,status=status.HTTP_200_OK)

@api_view(['GET'])
def getTripPlanCategory(request):
    results=TripCategory.objects.all().values('id','category_id')\
    .annotate(name=F('category__name'),icon_url=F('category__icon_url'))\
        .values('id','category_id','name','icon_url')
    
    return JsonResponse(list(results) ,safe=False,status=status.HTTP_200_OK)
@api_view(['POST'])
def getTripFilter(request):
    data = json.loads(request.body)
    plan_id=data['plan_id']
    cityList=[]
    categoryList=[]
    uniqueCities = set()
    uniqueCategories = set()
    historicalSiteList=[]
    eventList=[]
    parkList=[]
    hotelList=[]
    extremeSportList=[]
    weirdAndWackyList=[]
    attractionList=[]
    
    userLikesHistoricalSite=UserLikesHistoricalSite.objects.filter(plan_id=plan_id).all().values('historicalsite_id','id')
    userLikesEvent=UserLikesEvent.objects.filter(plan_id=plan_id).all().values('event_id','id')
    userLikesPark=UserLikesPark.objects.filter(plan_id=plan_id).all().values('park_id','id')
    userLikesHotel=UserLikesHotel.objects.filter(plan_id=plan_id).all().values('hotel_id','id')
    userLikesExtremeSport=UserLikesExtremeSport.objects.filter(plan_id=plan_id).all().values('extremesport_id','id')
    userLikesWeirdAndWacky=UserLikesWeirdAndWacky.objects.filter(plan_id=plan_id).all().values('weirdandwacky_id','id')
    userLikesAttraction=UserLikesAttraction.objects.filter(plan_id=plan_id).all().values('attraction_id','id')
    
    
    
    if userLikesHistoricalSite:
        userLikesHistoricalSiteData = userLikesHistoricalSite[0]
        if HistoricalSite.objects.filter(id=userLikesHistoricalSiteData['historicalsite_id']).exists():
            plans = HistoricalSite.objects.filter(id=userLikesHistoricalSiteData['historicalsite_id']).all().values(
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            historicalSiteList.append(list(plans))
            
    if userLikesEvent:
        userLikesEventData = userLikesEvent[0]
        if Event.objects.filter(id=userLikesEventData['event_id']).exists():
            plans = Event.objects.filter(id=userLikesEventData['event_id']).all().values(
            
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            eventList.append(list(plans))
    
    if userLikesPark:
        userLikesParkData = userLikesPark[0]
        if Park.objects.filter(id=userLikesParkData['park_id']).exists():
            plans = Park.objects.filter(id=userLikesParkData['park_id']).all().values(
           
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            parkList.append(list(plans))
    
    if userLikesHotel:
        userLikesHotelData = userLikesHotel[0]
        if Hotel.objects.filter(id=userLikesHotelData['hotel_id']).exists():
            plans = Hotel.objects.filter(id=userLikesHotelData['hotel_id']).all().values(
            
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            hotelList.append(list(plans))
    
    if userLikesWeirdAndWacky:
        userLikesWeirdAndWackyData = userLikesWeirdAndWacky[0]
        if WeirdAndWacky.objects.filter(id=userLikesWeirdAndWackyData['weirdandwacky_id']).exists():
            plans = WeirdAndWacky.objects.filter(id=userLikesWeirdAndWackyData['weirdandwacky_id']).all().values(
            
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
           'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            weirdAndWackyList.append(list(plans))
            # plans_list.append({"WeirdAndWacky":list(plans)})
            
    if userLikesExtremeSport:
        
        userLikesExtremeSportData = userLikesExtremeSport[0]
        if ExtremeSport.objects.filter(id=userLikesExtremeSportData['extremesport_id']).exists():
            plans = ExtremeSport.objects.filter(id=userLikesExtremeSportData['extremesport_id']).all().values(
            
            'city_id',
            'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            extremeSportList.append(list(plans))
    
    if userLikesAttraction:
        
        userLikesAttractionData = userLikesAttraction[0]
        if Attraction.objects.filter(id=userLikesAttractionData['attraction_id']).exists():
            plans = Attraction.objects.filter(id=userLikesAttractionData['attraction_id']).all().values(
           'city_id',
           'category_id'
            ).annotate(city_name=F('city__name')).annotate(category_name=F('category__name')).values(
            'category_id',
            'category_name',
            'city_id',
            'city_name'
            )
            for plan in plans:
                if plan['city_id'] and plan['city_id'] not in uniqueCities:
                    uniqueCities.add(plan['city_id'])
                    cityList.append({
                        "city_id":plan['city_id'],
                        "city_name":plan['city_name'],
                    })
                if plan['category_id'] and plan['category_id']  not in uniqueCategories:
                    uniqueCategories.add(plan['category_id'])
                    categoryList.append({
                        "category_id":plan['category_id'],
                        "category_name":plan['category_name'],
                    })
            attractionList.append(list(plans))
    
    
    return JsonResponse({
        "city":list(cityList),
        "category":list(categoryList),
        } ,safe=False,status=status.HTTP_200_OK)

@api_view(['POST'])
def getUserAssignedToPlan(request):
    data=json.loads(request.body)
    plan_id=data['plan_id']
    imageList=[]
    userList =PlanUser.objects.filter(plan_id=plan_id).all()\
               .values('id','user_id')
    print("userList = ",len(userList))
               
    for users in userList:
               profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                   values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
               for pic in profile_pic:
                   imageList.append({
                   "user_id":users['user_id'],
                   "profile_pic_id":pic['profile_pic_id'],
                   "profile_picture":pic['profile_picture'],
               })
                   users["profile_pic_id"]=pic['profile_pic_id']
                   users["profile_picture"]=pic['profile_picture']
               print('profile_pic = ',profile_pic)
    # for plan in userList:
    #              plan['users']=list(imageList)
    return JsonResponse(list(userList) ,safe=False,status=status.HTTP_200_OK)
@api_view(['POST'])
def getLikedSitesViaPlan(request):
    data = json.loads(request.body)
    plan_id=data['plan_id']
    selectedCity=data['selected_cities']
    selectedCategory=data['selected_categories']
    
    plans_list=[]
    historicalSiteList=[]
    eventList=[]
    parkList=[]
    hotelList=[]
    extremeSportList=[]
    weirdAndWackyList=[]
    attractionList=[]
    
    userLikesHistoricalSite=UserLikesHistoricalSite.objects.filter(plan_id=plan_id).all().values('historicalsite_id','id')
    userLikesEvent=UserLikesEvent.objects.filter(plan_id=plan_id).all().values('event_id','id')
    userLikesPark=UserLikesPark.objects.filter(plan_id=plan_id).all().values('park_id','id')
    userLikesHotel=UserLikesHotel.objects.filter(plan_id=plan_id).all().values('hotel_id','id')
    userLikesExtremeSport=UserLikesExtremeSport.objects.filter(plan_id=plan_id).all().values('extremesport_id','id')
    userLikesWeirdAndWacky=UserLikesWeirdAndWacky.objects.filter(plan_id=plan_id).all().values('weirdandwacky_id','id')
    userLikesAttraction=UserLikesAttraction.objects.filter(plan_id=plan_id).all().values('attraction_id','id')
    
    
    
    if userLikesHistoricalSite:
        userLikesHistoricalSiteData = userLikesHistoricalSite[0]
        if HistoricalSite.objects.filter(id=userLikesHistoricalSiteData['historicalsite_id']).exists():
            if selectedCity:
                fetch=HistoricalSite.objects.filter(id=userLikesHistoricalSiteData['historicalsite_id']).filter(city_id__in=selectedCity)
            else:
                fetch=HistoricalSite.objects.filter(id=userLikesHistoricalSiteData['historicalsite_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            imageList=[]
            userList =UserLikesHistoricalSite.objects.filter(plan_id=plan_id).all()\
                .values('historicalsite_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('historicalsite_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                # print('profile_pic = ',profile_pic)
            
            for plan in plans:
                print('plan = ',plan)
                plan['user_count']=len(userLikesHistoricalSite)
                plan['users']=list(imageList)
                historicalSiteList.append(plan)
            
    if userLikesEvent:
        userLikesEventData = userLikesEvent[0]
        if Event.objects.filter(id=userLikesEventData['event_id']).exists():
            if selectedCity:
                fetch=Event.objects.filter(id=userLikesEventData['event_id']).filter(city_id__in=selectedCity)
            else:
                fetch=Event.objects.filter(id=userLikesEventData['event_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            
            imageList=[]
            userList =UserLikesEvent.objects.filter(plan_id=plan_id).all()\
                .values('event_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('event_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            
            for plan in plans:
                plan['user_count']=len(userLikesEvent)
                plan['users']=list(imageList)
            # plans_list.append({"Event":list(plans)})
                eventList.append(plan)
    
    if userLikesPark:
        userLikesParkData = userLikesPark[0]
        if Park.objects.filter(id=userLikesParkData['park_id']).exists():
            if selectedCity:
                fetch=Park.objects.filter(id=userLikesParkData['park_id']).filter(city_id__in=selectedCity)
            else:
                fetch=Park.objects.filter(id=userLikesParkData['park_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            
            imageList=[]
            userList =UserLikesPark.objects.filter(plan_id=plan_id).all()\
                .values('park_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('park_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            for plan in plans:
                plan['user_count']=len(userLikesPark)
                plan['users']=list(imageList)
                parkList.append(plan)
    
    if userLikesHotel:
        userLikesHotelData = userLikesHotel[0]
        if Hotel.objects.filter(id=userLikesHotelData['hotel_id']).exists():
            if selectedCity:
                fetch= Hotel.objects.filter(id=userLikesHotelData['hotel_id']).filter(city_id__in=selectedCity)
            else:
                fetch= Hotel.objects.filter(id=userLikesHotelData['hotel_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            plans =fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            
            imageList=[]
            userList =UserLikesHotel.objects.filter(plan_id=plan_id).all()\
                .values('hotel_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('hotel_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            
            for plan in plans:
                plan['user_count']=len(userLikesHotel)
                plan['users']=list(imageList)
                hotelList.append(plan)
    
    if userLikesWeirdAndWacky:
        userLikesWeirdAndWackyData = userLikesWeirdAndWacky[0]
        if WeirdAndWacky.objects.filter(id=userLikesWeirdAndWackyData['weirdandwacky_id']).exists():
            if selectedCity:
                fetch=WeirdAndWacky.objects.filter(id=userLikesWeirdAndWackyData['weirdandwacky_id']).filter(city_id__in=selectedCity)
            else:
                fetch=WeirdAndWacky.objects.filter(id=userLikesWeirdAndWackyData['weirdandwacky_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
                
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            imageList=[]
            userList =UserLikesWeirdAndWacky.objects.filter(plan_id=plan_id).all()\
                .values('weirdandwacky_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('weirdandwacky_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            for plan in plans:
                plan['user_count']=len(userLikesWeirdAndWacky)
                plan['users']=list(imageList)
                weirdAndWackyList.append(plan)
            # plans_list.append({"WeirdAndWacky":list(plans)})
            
    if userLikesExtremeSport:
        
        userLikesExtremeSportData = userLikesExtremeSport[0]
        if ExtremeSport.objects.filter(id=userLikesExtremeSportData['extremesport_id']).exists():
            if selectedCity:
                fetch=ExtremeSport.objects.filter(id=userLikesExtremeSportData['extremesport_id']).filter(city_id__in=selectedCity)
            else:
                fetch=ExtremeSport.objects.filter(id=userLikesExtremeSportData['extremesport_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            
            imageList=[]
            userList =UserLikesExtremeSport.objects.filter(plan_id=plan_id).all()\
                .values('extremesport_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('extremesport_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            
            for plan in plans:
                plan['user_count']=len(userLikesExtremeSport)
                plan['users']=list(imageList)
                extremeSportList.append(plan)
    
    if userLikesAttraction:
        
        userLikesAttractionData = userLikesAttraction[0]
        if Attraction.objects.filter(id=userLikesAttractionData['attraction_id']).exists():
            if selectedCity:
                fetch=Attraction.objects.filter(id=userLikesAttractionData['attraction_id']).filter(city_id__in=selectedCity)
            else:
                fetch=Attraction.objects.filter(id=userLikesAttractionData['attraction_id'])
            if selectedCategory:
                fetch=fetch.filter(category_id__in=selectedCategory)
            plans = fetch.all().values(
            'id', 'name', 
            'description', 'images',
            'city_id'
            ).annotate(city_name=F('city__name')).values(
            'id', 'name', 
            'description', 'images',
            'city_id',
            'city_name'
            )
            
            
            imageList=[]
            userList =UserLikesAttraction.objects.filter(plan_id=plan_id).all()\
                .values('attraction_id','id','userlikes_id')\
                    .annotate(user_id=F('userlikes__user_id'))\
                        .values('attraction_id','id','userlikes_id','user_id')
                        
            for users in userList:
                profile_pic = user_models.User.objects.filter(id=users['user_id']).\
                    values('profile_pic_id', profile_picture=F('profile_pic__media_url'))
                for pic in profile_pic:
                    imageList.append({
                    "profile_pic_id":pic['profile_pic_id'],
                    "profile_picture":pic['profile_picture'],
                })
                print('profile_pic = ',profile_pic)
            
            
            
            for plan in plans:
                plan['user_count']=len(userLikesAttraction)
                plan['users']=list(imageList)
                attractionList.append(plan)
    
    plans_list.append({"HistoricalSite":list(historicalSiteList)})
    plans_list.append({"Event":list(eventList)})
    plans_list.append({"Park":list(parkList)})
    plans_list.append({"Hotel":list(hotelList)})
    plans_list.append({"WeirdAndWacky":list(weirdAndWackyList)})
    plans_list.append({"ExtremeSport":list(extremeSportList)})
    plans_list.append({"Attraction":list(attractionList)})
    return JsonResponse(json.dumps(
        {
        "HistoricalSite":list(historicalSiteList),
         "Event":list(eventList),
         "Park":list(parkList),
         "Hotel":list(hotelList),
         "WeirdAndWacky":list(weirdAndWackyList),
         "ExtremeSports":list(extremeSportList),
         "Attraction":list(attractionList)
         },
        default=str
        ) ,safe=False,status=status.HTTP_200_OK)
    
    return JsonResponse(plans_list ,safe=False,status=status.HTTP_200_OK)

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
        print("Data = ",data)
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