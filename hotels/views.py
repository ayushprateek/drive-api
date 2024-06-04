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
# views.py
from django.http import JsonResponse

from shapely.geometry import Point, LineString,box

import requests
from django.http import JsonResponse
from django.conf import settings
from .models import Location, Viewport, Geometry, Photo, PlusCode, Hotel
import math

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
        
        hotel = Hotel.objects.create(
            business_status=result['business_status'],
            geometry=geometry,
            icon=result['icon'],
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
            user_ratings_total=result['user_ratings_total'],
            vicinity=result['vicinity']
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
        lat = data['latitude']
        lng =  data['longitude']
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=50000&type=lodging&key={settings.GOOGLE_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data=response.json()
            saveToDb(data)
            next_page_token = data.get('next_page_token')
            print('next_page_token = ',next_page_token)
            while next_page_token:
                newUrl = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={settings.GOOGLE_API_KEY}"
                res = requests.get(newUrl)
                newData=res.json()
                next_page_token = newData.get('next_page_token')
                print('2nd calling next page url, Status = ',res.status_code)
                if res.status_code == 200:
                    saveToDb(res.json())
                if not next_page_token:
                    break
            
            
            
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
    
    
    for hotel in results:
        # print("latitude == ",hotel['geometry']['location']['lat'],hotel['geometry']['location']['lng'])
        point = Point(hotel['geometry']['location']['lng'], hotel['geometry']['location']['lat'])
        # print("distance from point == ",line.distance(point),bounding_box.contains(point))
        
        # if line.distance(point) <= threshold_distance and bounding_box.contains(point):
        if is_distance_one(hotel['geometry']['location']['lat'],hotel['geometry']['location']['lng'], decoded_points,threshold_distance) and bounding_box.contains(point):
            print('inserting')
            result.append(hotel)
    print('Len', len(results))
    
    return JsonResponse(result, safe=False)

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


class ScrapeHotelsView(View):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        # call using http://127.0.0.1:8000/hotels/scrape

        # if not latitude or not longitude:
        #     return JsonResponse({'error': 'Latitude and longitude are required parameters'}, status=400)

        # try:
        #     latitude = float(latitude)
        #     longitude = float(longitude)
        # except ValueError:
        #     return JsonResponse({'error': 'Invalid latitude or longitude'}, status=400)
        # latlang=[{"latitude":29.679547,"longitude":-82.379897},{"latitude":29.679578,"longitude":-82.380034},{"latitude":29.679627,"longitude":-82.380513},{"latitude":29.679804,"longitude":-82.381193},{"latitude":29.679943,"longitude":-82.38145},{"latitude":29.680216,"longitude":-82.381955},{"latitude":29.677717,"longitude":-82.383302},{"latitude":29.675189,"longitude":-82.383311},{"latitude":29.675189,"longitude":-82.383669},{"latitude":29.67525,"longitude":-82.383744},{"latitude":29.675472,"longitude":-82.383969},{"latitude":29.675603,"longitude":-82.384184},{"latitude":29.675632,"longitude":-82.384412},{"latitude":29.675611,"longitude":-82.384866},{"latitude":29.67556,"longitude":-82.385087},{"latitude":29.675499,"longitude":-82.385306},{"latitude":29.67549,"longitude":-82.385412},{"latitude":29.675392,"longitude":-82.386263},{"latitude":29.674703,"longitude":-82.386236},{"latitude":29.673954,"longitude":-82.386243},{"latitude":29.67351,"longitude":-82.38624},{"latitude":29.673228,"longitude":-82.386266},{"latitude":29.672914,"longitude":-82.386413},{"latitude":29.673199,"longitude":-82.386966},{"latitude":29.673956,"longitude":-82.388644},{"latitude":29.674086,"longitude":-82.388981},{"latitude":29.672808,"longitude":-82.388989},{"latitude":29.672062,"longitude":-82.38901},{"latitude":29.67113,"longitude":-82.388986},{"latitude":29.671031,"longitude":-82.388986},{"latitude":29.670093,"longitude":-82.38899},{"latitude":29.669899,"longitude":-82.388991},{"latitude":29.669918,"longitude":-82.389157},{"latitude":29.66992,"longitude":-82.389663},{"latitude":29.671027,"longitude":-82.389668},{"latitude":29.671062,"longitude":-82.389677},{"latitude":29.671091,"longitude":-82.389695},{"latitude":29.671129,"longitude":-82.389736},{"latitude":29.671146,"longitude":-82.389769},{"latitude":29.671156,"longitude":-82.389807},{"latitude":29.671157,"longitude":-82.39082},{"latitude":29.671158,"longitude":-82.39197},{"latitude":29.672004,"longitude":-82.392038},{"latitude":29.672286,"longitude":-82.392052},{"latitude":29.674104,"longitude":-82.392041},{"latitude":29.674104,"longitude":-82.392656},{"latitude":29.674105,"longitude":-82.393312},{"latitude":29.674107,"longitude":-82.393688},{"latitude":29.674108,"longitude":-82.394615},{"latitude":29.674108,"longitude":-82.394983},{"latitude":29.674111,"longitude":-82.397338},{"latitude":29.674108,"longitude":-82.397763},{"latitude":29.674116,"longitude":-82.399786},{"latitude":29.674112,"longitude":-82.400703},{"latitude":29.674113,"longitude":-82.401078},{"latitude":29.674105,"longitude":-82.401495},{"latitude":29.674095,"longitude":-82.4023},{"latitude":29.674104,"longitude":-82.403927},{"latitude":29.674111,"longitude":-82.405782},{"latitude":29.674113,"longitude":-82.405934},{"latitude":29.67412,"longitude":-82.406351},{"latitude":29.674137,"longitude":-82.407342},{"latitude":29.674142,"longitude":-82.40765},{"latitude":29.674171,"longitude":-82.409397},{"latitude":29.674173,"longitude":-82.409779},{"latitude":29.67418,"longitude":-82.410352},{"latitude":29.674227,"longitude":-82.413173},{"latitude":29.674227,"longitude":-82.413207},{"latitude":29.674229,"longitude":-82.413525},{"latitude":29.674232,"longitude":-82.413899},{"latitude":29.674234,"longitude":-82.415307},{"latitude":29.674241,"longitude":-82.416242},{"latitude":29.67424,"longitude":-82.416961},{"latitude":29.674247,"longitude":-82.417297},{"latitude":29.674247,"longitude":-82.418067},{"latitude":29.674248,"longitude":-82.418615},{"latitude":29.674233,"longitude":-82.419265},{"latitude":29.674215,"longitude":-82.420078},{"latitude":29.674172,"longitude":-82.421023},{"latitude":29.67417,"longitude":-82.421041},{"latitude":29.674144,"longitude":-82.421525},{"latitude":29.674118,"longitude":-82.42213},{"latitude":29.674109,"longitude":-82.422262},{"latitude":29.67409,"longitude":-82.422564},{"latitude":29.674091,"longitude":-82.422754},{"latitude":29.67409,"longitude":-82.422816},{"latitude":29.674083,"longitude":-82.423091},{"latitude":29.674068,"longitude":-82.423502},{"latitude":29.674085,"longitude":-82.424289},{"latitude":29.674108,"longitude":-82.42461},{"latitude":29.674114,"longitude":-82.424952},{"latitude":29.674141,"longitude":-82.425419},{"latitude":29.674177,"longitude":-82.4258},{"latitude":29.674212,"longitude":-82.426725},{"latitude":29.674259,"longitude":-82.427455},{"latitude":29.674294,"longitude":-82.428482},{"latitude":29.674293,"longitude":-82.430031},{"latitude":29.674304,"longitude":-82.430354},{"latitude":29.674314,"longitude":-82.431393},{"latitude":29.674307,"longitude":-82.432091},{"latitude":29.674307,"longitude":-82.432548},{"latitude":29.673463,"longitude":-82.431726},{"latitude":29.67251,"longitude":-82.430798},{"latitude":29.6682,"longitude":-82.426605},{"latitude":29.664706,"longitude":-82.42339},{"latitude":29.664368,"longitude":-82.423103},{"latitude":29.659838,"longitude":-82.419248},{"latitude":29.659656,"longitude":-82.419093},{"latitude":29.659654,"longitude":-82.41976},{"latitude":29.659657,"longitude":-82.420036},{"latitude":29.659664,"longitude":-82.420516},{"latitude":29.659668,"longitude":-82.420757},{"latitude":29.659687,"longitude":-82.421575},{"latitude":29.659694,"longitude":-82.422084},{"latitude":29.659698,"longitude":-82.422373},{"latitude":29.658529,"longitude":-82.422389},{"latitude":29.658527,"longitude":-82.423453},{"latitude":29.659105,"longitude":-82.424168},{"latitude":29.659239,"longitude":-82.424085},{"latitude":29.659709,"longitude":-82.424076},{"latitude":29.659717,"longitude":-82.424704},{"latitude":29.65973,"longitude":-82.425765},{"latitude":29.659731,"longitude":-82.426204},{"latitude":29.659737,"longitude":-82.42777},{"latitude":29.65976,"longitude":-82.428106},{"latitude":29.659811,"longitude":-82.428569},{"latitude":29.660094,"longitude":-82.429754},{"latitude":29.660207,"longitude":-82.430196},{"latitude":29.660275,"longitude":-82.430588},{"latitude":29.660326,"longitude":-82.430981},{"latitude":29.660324,"longitude":-82.431521},{"latitude":29.660343,"longitude":-82.433577},{"latitude":29.660345,"longitude":-82.434333},{"latitude":29.660327,"longitude":-82.436342},{"latitude":29.66033,"longitude":-82.436754},{"latitude":29.66033,"longitude":-82.436844},{"latitude":29.660258,"longitude":-82.43811},{"latitude":29.660203,"longitude":-82.438937},{"latitude":29.66015,"longitude":-82.439525},{"latitude":29.660033,"longitude":-82.440638},{"latitude":29.659949,"longitude":-82.441488},{"latitude":29.659917,"longitude":-82.442251},{"latitude":29.659905,"longitude":-82.442592},{"latitude":29.65988,"longitude":-82.443381},{"latitude":29.659879,"longitude":-82.443585},{"latitude":29.659877,"longitude":-82.444552},{"latitude":29.659876,"longitude":-82.445552},{"latitude":29.659875,"longitude":-82.446603},{"latitude":29.659912,"longitude":-82.453247},{"latitude":29.659918,"longitude":-82.4538},{"latitude":29.659921,"longitude":-82.454962},{"latitude":29.659923,"longitude":-82.455858},{"latitude":29.65993,"longitude":-82.456642},{"latitude":29.659934,"longitude":-82.458383},{"latitude":29.659943,"longitude":-82.459945},{"latitude":29.659942,"longitude":-82.460922},{"latitude":29.659965,"longitude":-82.463128},{"latitude":29.659969,"longitude":-82.463489},{"latitude":29.659961,"longitude":-82.463732},{"latitude":29.659947,"longitude":-82.464161},{"latitude":29.659948,"longitude":-82.464204},{"latitude":29.659979,"longitude":-82.465139},{"latitude":29.659968,"longitude":-82.467777},{"latitude":29.65998,"longitude":-82.468713},{"latitude":29.659982,"longitude":-82.470503},{"latitude":29.65997,"longitude":-82.471067},{"latitude":29.659971,"longitude":-82.471318},{"latitude":29.659942,"longitude":-82.471598},{"latitude":29.659917,"longitude":-82.471782},{"latitude":29.659887,"longitude":-82.472012},{"latitude":29.659871,"longitude":-82.47211},{"latitude":29.659825,"longitude":-82.472384},{"latitude":29.659991,"longitude":-82.472413},{"latitude":29.660333,"longitude":-82.472426},{"latitude":29.66091,"longitude":-82.472436},{"latitude":29.661158,"longitude":-82.472428},{"latitude":29.661254,"longitude":-82.472434},{"latitude":29.661464,"longitude":-82.472416},{"latitude":29.66172,"longitude":-82.472414},{"latitude":29.661835,"longitude":-82.472406},{"latitude":29.662383,"longitude":-82.472411},{"latitude":29.662572,"longitude":-82.472421},{"latitude":29.66279,"longitude":-82.472414},{"latitude":29.662972,"longitude":-82.4724},{"latitude":29.663114,"longitude":-82.472394},{"latitude":29.663259,"longitude":-82.472373},{"latitude":29.663438,"longitude":-82.472358},{"latitude":29.663647,"longitude":-82.472333},{"latitude":29.663985,"longitude":-82.472339},{"latitude":29.66415,"longitude":-82.47235},{"latitude":29.664527,"longitude":-82.472405},{"latitude":29.664655,"longitude":-82.472445},{"latitude":29.664668,"longitude":-82.488956},{"latitude":29.664678,"longitude":-82.489981},{"latitude":29.664727,"longitude":-82.495293},{"latitude":29.664734,"longitude":-82.496027},{"latitude":29.664945,"longitude":-82.496023},{"latitude":29.666409,"longitude":-82.496029},{"latitude":29.668079,"longitude":-82.496007},{"latitude":29.668786,"longitude":-82.496006},{"latitude":29.670659,"longitude":-82.496002},{"latitude":29.671946,"longitude":-82.496009},{"latitude":29.672088,"longitude":-82.496004},{"latitude":29.672238,"longitude":-82.496003},{"latitude":29.672567,"longitude":-82.496002},{"latitude":29.674785,"longitude":-82.496002},{"latitude":29.675489,"longitude":-82.496001},{"latitude":29.677005,"longitude":-82.496035},{"latitude":29.67813,"longitude":-82.496022},{"latitude":29.678488,"longitude":-82.496018},{"latitude":29.679486,"longitude":-82.496007},{"latitude":29.680945,"longitude":-82.495991},{"latitude":29.68104,"longitude":-82.495991},{"latitude":29.682703,"longitude":-82.495991},{"latitude":29.682969,"longitude":-82.495991},{"latitude":29.686397,"longitude":-82.495989},{"latitude":29.686892,"longitude":-82.495985},{"latitude":29.688442,"longitude":-82.495974},{"latitude":29.689227,"longitude":-82.495985},{"latitude":29.690107,"longitude":-82.495999},{"latitude":29.691208,"longitude":-82.495985},{"latitude":29.692439,"longitude":-82.495984},{"latitude":29.694141,"longitude":-82.495995},{"latitude":29.694724,"longitude":-82.495995},{"latitude":29.694959,"longitude":-82.495991},{"latitude":29.695854,"longitude":-82.495979},{"latitude":29.696797,"longitude":-82.49598},{"latitude":29.697377,"longitude":-82.495981},{"latitude":29.697798,"longitude":-82.495982},{"latitude":29.698794,"longitude":-82.495992},{"latitude":29.699289,"longitude":-82.495992},{"latitude":29.699564,"longitude":-82.495992},{"latitude":29.700309,"longitude":-82.495979},{"latitude":29.701115,"longitude":-82.49599},{"latitude":29.701196,"longitude":-82.495991},{"latitude":29.70163,"longitude":-82.495982},{"latitude":29.702394,"longitude":-82.495982},{"latitude":29.704654,"longitude":-82.495977},{"latitude":29.706681,"longitude":-82.495973},{"latitude":29.706681,"longitude":-82.482689},{"latitude":29.703692,"longitude":-82.479652},{"latitude":29.697256,"longitude":-82.467959},{"latitude":29.699976,"longitude":-82.457045},{"latitude":29.699977,"longitude":-82.457046},{"latitude":29.700697,"longitude":-82.457548},{"latitude":29.701458,"longitude":-82.458048},{"latitude":29.702164,"longitude":-82.458485},{"latitude":29.702883,"longitude":-82.458906},{"latitude":29.703562,"longitude":-82.459271},{"latitude":29.708848,"longitude":-82.462114},{"latitude":29.713732,"longitude":-82.464697},{"latitude":29.716325,"longitude":-82.466092},{"latitude":29.716217,"longitude":-82.465768},{"latitude":29.716085,"longitude":-82.465374},{"latitude":29.715541,"longitude":-82.463789},{"latitude":29.71421,"longitude":-82.459736},{"latitude":29.712781,"longitude":-82.455421},{"latitude":29.712498,"longitude":-82.454581},{"latitude":29.712157,"longitude":-82.453568},{"latitude":29.711969,"longitude":-82.453082},{"latitude":29.711778,"longitude":-82.45252},{"latitude":29.711599,"longitude":-82.451953},{"latitude":29.711433,"longitude":-82.451381},{"latitude":29.711279,"longitude":-82.450804},{"latitude":29.711138,"longitude":-82.450223},{"latitude":29.711009,"longitude":-82.449638},{"latitude":29.71098,"longitude":-82.449496},{"latitude":29.703537,"longitude":-82.449506},{"latitude":29.702209,"longitude":-82.449324},{"latitude":29.702209,"longitude":-82.430575},{"latitude":29.702209,"longitude":-82.426366},{"latitude":29.700279,"longitude":-82.423483},{"latitude":29.70004,"longitude":-82.41893},{"latitude":29.698613,"longitude":-82.418516},{"latitude":29.695545,"longitude":-82.410969},{"latitude":29.696684,"longitude":-82.404678},{"latitude":29.699632,"longitude":-82.403477},{"latitude":29.699632,"longitude":-82.397301},{"latitude":29.699608,"longitude":-82.397186},{"latitude":29.697863,"longitude":-82.393454},{"latitude":29.703259,"longitude":-82.388888},{"latitude":29.703268,"longitude":-82.388606},{"latitude":29.703246,"longitude":-82.388111},{"latitude":29.703239,"longitude":-82.387244},{"latitude":29.703258,"longitude":-82.386828},{"latitude":29.70326,"longitude":-82.386801},{"latitude":29.70333,"longitude":-82.38607},{"latitude":29.703374,"longitude":-82.385372},{"latitude":29.703365,"longitude":-82.381897},{"latitude":29.696969,"longitude":-82.381897},{"latitude":29.695985,"longitude":-82.381436},{"latitude":29.691314,"longitude":-82.379463},{"latitude":29.688657,"longitude":-82.379463},{"latitude":29.688656,"longitude":-82.379109},{"latitude":29.685891,"longitude":-82.37904},{"latitude":29.684431,"longitude":-82.379038},{"latitude":29.684427,"longitude":-82.379798},{"latitude":29.683846,"longitude":-82.379761},{"latitude":29.683373,"longitude":-82.379654},{"latitude":29.682718,"longitude":-82.379478},{"latitude":29.681981,"longitude":-82.379334},{"latitude":29.681211,"longitude":-82.379107},{"latitude":29.680578,"longitude":-82.378957},{"latitude":29.680298,"longitude":-82.378812},{"latitude":29.680094,"longitude":-82.378686},{"latitude":29.679808,"longitude":-82.378403},{"latitude":29.679505,"longitude":-82.378037},{"latitude":29.679467,"longitude":-82.378031},{"latitude":29.679467,"longitude":-82.378258},{"latitude":29.679412,"longitude":-82.378649},{"latitude":29.67944,"longitude":-82.379423},{"latitude":29.679547,"longitude":-82.379897}]
        
         #{"latitude":30.135078,"longitude": -82.303956},
        # latlang=[
           
        #     30.528997, -85.884900,
        #     30.467823, -85.481728,
        #     30.177115, -85.285272,
        #     30.395227, -84.892362,
        #     30.346799, -84.331061,
        #     30.274113, -83.853955,
        #     30.152850, -83.404915,
        #     30.201373, -83.012004,
        #     29.934201, -83.124264,
        #     29.934201, -83.124264,
        #     29.644144, -82.891468,
        #     29.564339, -82.570213,
        #     29.577644, -82.172468,
        #     30.438702, -82.631404,
        #     30.148104, -82.524319,
        #     30.121644, -82.264255,
        #     30.174558, -81.988894,
        #     30.028976, -82.203064,
        #     29.909704, -81.820617,
        #     29.577644, -81.912404,
        #     29.670732, -81.637043,
        #     29.617549, -81.453468,
        #     29.497786, -81.820617,
        #     29.271181, -82.019489,
        #     29.003942, -82.065383,
        #     29.271181, -81.835915,
        #     29.137648, -81.499362,
        #     29.097555, -81.835915,
        #     28.896852, -81.973596,
        #     28.548048, -81.988894,
        #     28.292419, -81.790021,
        #     28.157630, -81.606447,
        #     28.066303, -81.422551,
        #     28.012578, -81.257333,
        #     27.951145, -81.083420,
        #     27.935782, -81.379073,
        #     27.920416, -81.744290,
        #     27.527851, -81.639942,
        #     27.481574, -81.909508,
        #     27.334902, -81.944290,
        #     27.303999, -82.248638,
        #     27.242167, -82.074725,
        #     27.175862, -81.461201,
        #     27.189757, -81.195667,
        #     27.264911, -81.067270,
        #     27.037494, -81.176805,
        #     26.796580, -81.220619,
        #     26.646564, -81.206014,
        #     26.522489, -81.279037,
        #     26.378655, -81.454292,
        #     26.195335, -81.498106,
        #     26.037974, -81.468897,
        #     26.051095, -81.198712,
        #     26.064215, -80.957736,
        #     26.319763, -80.826294,
        #     26.260840, -80.629132,
        #     26.110124, -80.497691,
        #     25.978909, -80.541504,
        #     25.840975, -80.687551,
        #     25.702879, -80.745969,
        #     25.919814, -80.541504,
        #     25.722617, -80.556109,
        #     25.630480, -80.753271,
        #     25.538271, -80.833597,
        #     25.426209, -80.592621,
        #     25.314042, -80.541504,
        #     25.818571, -80.344273,
        #     25.920899, -80.361579,
        #     26.038690, -80.378885,
        #     26.063122, -80.304716,
        #     26.158581, -80.228075,
        #     26.194080, -80.186046,
        #     26.327422, -80.199521,
        #     26.452348, -80.185849,
        #     26.415619, -80.150300,
        #     26.545343, -80.177645,
        #     26.689580, -80.163973,
        #     26.779940, -80.188583,
        #     26.914127, -80.174911,
        #     27.067636, -80.267884,
        #     27.194184, -80.338981,
        #     27.325447, -80.478440,
        #     27.451702, -80.503051,
        #     27.546299, -80.538599,
        #     27.589932, -80.590555,
        #     27.730407, -80.672590,
        #     27.880370, -80.686262,
        #     27.984256, -80.724545,
        #     28.044608, -80.814784,
        #     28.170033, -80.754625,
        #     28.467230, -80.949765,
        #     28.657637, -81.044611,
        #     28.930741, -81.078484,
        #     29.078866, -81.410445,
        #     29.356766, -81.329149,
        #     29.527859, -81.417220,
        #     29.610352, -81.667884,
        #     29.728083, -81.457868,
        #     29.869178, -81.437544,
        #     30.021805, -81.816928,
        #     30.215187, -81.471418,
        #     30.644946, -81.820757,
        #     ]
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
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=50000&type=lodging&key={settings.GOOGLE_API_KEY}"
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
