
from geopy import geocoders  
from geopy.geocoders import Nominatim


def get_geo_code(name):
    try:
        gn = geocoders.GeoNames("trip")
        geo_data = gn.geocode(name)
        if geo_data:
            lat, long = geo_data.raw.get("lat"), geo_data.raw.get("lng")
            return lat, long
        return None, None
    except Exception:
        return None, None


def get_lat_lng_geopy(place_name):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(place_name)
        if location:
            return location.latitude, location.longitude
        return None, None
    except Exception:
        return None, None


def get_geo_code_area(name):
    """
    This will return the lattitude and logitude and actual address of the
    hotel
    """
    try:
        #making an instance of Nominatim class
        geolocator = Nominatim(user_agent="my_request")
        
        #applying geocode method to get the location
        location = geolocator.geocode(name)
        if location:
            return location.latitude, location.longitude, location.address
    except Exception:
        pass
    return None, None, None


def get_city_name(latitude, longitude):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    
    if location and hasattr(location, 'address'):
        address = location.address.split(',')
        city = address[-3]  # The city name should be the third-to-last element in the address
        return city.strip()
    else:
        return None