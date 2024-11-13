import math
import random

import requests

from apps.user.models import UserPlanTripLogs
from common.constants import Constant, common_descriptions

from drive_ai import settings

from apps.trip import models as trip_models


def get_geo_data(hotel_name_or_address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    api_key = settings.GOOGLE_API_KEY
    # Parameters for the API call
    params = {"address": hotel_name_or_address, "key": api_key}

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extracting required data if available
    if data["status"] == "OK":
        geo_data = data["results"][0]["geometry"]["location"]
        components = data["results"][0]["address_components"]

        # Finding the city name from address components
        city_name = None
        for component in components:
            if "locality" in component["types"]:
                city_name = component["long_name"]
                break

        geo_data = {
            "latitude": geo_data["lat"],
            "longitude": geo_data["lng"],
            "city_name": city_name,
        }
        return geo_data, data
    else:
        return None, None


class ModelMap:
    """
    Maps the Model char with the Models
    """

    category_to_model = {
        # Constant.ATTRACTION: trip_models.Attraction,
        # Constant.FOOD: trip_models.Food,
        # Constant.WEIRDANDWACKY: trip_models.WeirdAndWacky,
        # Constant.CAMPING: trip_models.Camp,
        # Constant.NATIONAL_PARK: trip_models.Park,
        # Constant.FAMILY_FUN: trip_models.FamilyFun,
        Constant.SITES: trip_models.Site,
        # Constant.EXTREME_SPORTS: trip_models.ExtremeSport,
        # Constant.EVENT_CALENDAR: trip_models.Event,
        # Constant.HOTEL: trip_models.Hotel,
    }


CATEGORY_MAPPING = {
    "Food": "restaurant",
    "Shopping": "shopping_mall",
    "Cheap Gas": "gas_station",
    "Attractions": "tourist_attraction",
    "Weird and Wacky": "point_of_interest",
    "Travel Info": "travel_agency",
    "EV Charging": "electric_vehicle_charging_station",
    "RV & Camping": "campground",
    "Hotels": "lodging",
    "Historical Sites": "historical site",
    "Clubs & Dancing": "night_club",
    "National Park": "park",
    "Events": "events",
}

MODEL_MAPPING = {
    # Constant.ATTRACTION: trip_models.Attraction,
    # Constant.FOOD: trip_models.Food,
    # Constant.WEIRDANDWACKY: trip_models.WeirdAndWacky,
    # Constant.CAMPING: trip_models.Camp,
    # Constant.NATIONAL_PARK: trip_models.Park,
    # Constant.FAMILY_FUN: trip_models.FamilyFun,
    Constant.SITES: trip_models.Site,
    # Constant.EXTREME_SPORTS: trip_models.ExtremeSport,
    # Constant.EVENT_CALENDAR: trip_models.Event,
    # Constant.HOTEL: trip_models.Hotel,
}


def get_route(start, end, api_key):
    """
    Fetch the best route (steps) between a start and end location using Google Directions API.

    Parameters:
    - start (str): The start location (can be a name or a 'lat,long').
    - end (str): The end location (similar format to start).
    - api_key (str): Your Google API key.

    Returns:
    - list: List of steps (or route segments) between start and end, or None if failed.
    """

    # Base endpoint for the Google Directions API.
    base_url = "https://maps.googleapis.com/maps/api/directions/json?"

    # Prepare the request parameters.
    params = {"origin": start, "destination": end, "key": api_key}

    # Make the API request.
    response = requests.get(base_url, params=params).json()

    # Check if the response is successful.
    if response["status"] == "OK":
        # Return the steps of the route.
        return response["routes"][0]["legs"][0]["steps"], response
    else:
        # Return None if there's an issue.
        return None, None


def get_coordinates(address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    api_key = settings.GOOGLE_API_KEY
    params = {
        "address": address,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None, None


def get_pois_along_route(route, api_key, type_of_place="restaurant", radius=800):
    """
    Fetch points of interest (POIs) of a certain type around each step in a route using Google Places API.

    Parameters:
    - route (list): A list of steps or segments from the route.
    - api_key (str): Your Google API key.
    - type_of_place (str): The type of place of interest (defaults to "restaurant").
    - radius (int): The radius around each route step to search for places (in meters, default is 20,000 i.e., 20 km).

    Returns:
    - list: A list of POIs around the provided route.
    """

    # Base endpoint for the Google Places NearBy Search API.
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    pois = []  # Initialize a list to store points of interest.

    # Loop through each step in the route.
    for step in route:
        # Extract the end location of the current step.
        location = step["end_location"]

        # Prepare the request parameters.
        params = {
            "location": f"{location['lat']},{location['lng']}",
            "radius": radius,
            "type": type_of_place,
            "key": api_key,
            "photo": True,
            "opennow": True,  # Filters to only get currently open places.
        }

        if type_of_place == "park":
            params.update({'keyword': 'national park'})

        if type_of_place == "historical site":
            params.update({'type': 'tourist_attraction',
                           'keyword': 'historical'})

        if type_of_place == "lodging":
            params.update({'keyword': 'star hotel'})

        # Make the API request.
        response = requests.get(base_url, params=params).json()

        # Add the found places to our POIs list.
        pois.extend(response.get("results", []))

    # Return the aggregated list of POIs.
    return pois


def get_pois_around_location(location, api_key, type_of_place="restaurant", radius=800):
    """
    Fetch points of interest (POIs) of a certain type around each step in a route using Google Places API.

    Parameters:
    - route (list): A list of steps or segments from the route.
    - api_key (str): Your Google API key.
    - type_of_place (str): The type of place of interest (defaults to "restaurant").
    - radius (int): The radius around each route step to search for places (in meters, default is 20,000 i.e., 20 km).

    Returns:
    - list: A list of POIs around the provided route.
    """

    # Base endpoint for the Google Places NearBy Search API.
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    pois = []  # Initialize a list to store points of interest.

    # Loop through each step in the route.
    # for step in route:
    # Extract the end location of the current step.
    location = location

    # Prepare the request parameters.
    params = {
        "location": f"{location['lat']},{location['lng']}",
        "radius": radius,
        "type": type_of_place,
        "key": api_key,
        "photo": True,
        "opennow": True,  # Filters to only get currently open places.
    }

    if type_of_place == "lodging":
        params.update({'keyword': 'star hotel'})

    # Make the API request.
    response = requests.get(base_url, params=params).json()

    # Add the found places to our POIs list.
    pois.extend(response.get("results", []))

    # Return the aggregated list of POIs.
    return pois


def haversine_distance(coord1, coord2):
    """
    Calculate the Haversine distance between two sets of GPS coordinates.

    Parameters:
    coord1 (tuple): A tuple of (lat, long) for the first coordinate.
    coord2 (tuple): A tuple of (lat, long) for the second coordinate.

    Returns:
    float: distance between the two coordinates in kilometers.
    """
    r = 6371.0  # Radius of the Earth in kilometers

    lat1, lon1 = float(coord1)
    lat2, lon2 = float(coord2)

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = r * c

    return distance


def get_images(images):
    """Function to Get Images"""
    image_urls = []
    for image in images:
        if image and image != "":
            if image.startswith("http") or image.startswith("https"):
                image_urls.append(image)
            else:
                image_urls.append(
                    f"https://s3.amazonaws.com/{settings.AWS_BUCKET}/{image}"
                )

    return image_urls


def fetch_pois_for_category(args):
    """
    Fetches points of interest (POIs) for a given category along a particular route. It fetches both from Google API
    and the local database.

    Parameters:
    - args (tuple): A tuple containing:
        - category (str): The category of interest.
        - filtered_steps (list): Steps/routes to look around.
        - api_key (str): The Google API key.
        - seen_places (set): A set of coordinates (in the form 'lat_lng') already processed.
        - results (list): A list to store the results.

    Returns:
    - list: A list of unified places (both from Google API and the database) matching the category.
    """

    (
        category,
        filtered_steps,
        api_key,
        seen_places,
        results,
        origin_city,
        destination_city,
        user
    ) = args

    category_obj = trip_models.Category.objects.filter(name=category)
    icon_url = category_obj.first().icon_url if category_obj else None

    # Fetch from Google Places API
    pois = get_pois_along_route(
        filtered_steps, api_key=api_key, type_of_place=CATEGORY_MAPPING[category]
    )
    for poi in pois:
        # Create a unique key based on lat-lng to avoid duplicate places
        lat_long_key = f"{round(poi['geometry']['location']['lat'], 4)}_{round(poi['geometry']['location']['lng'], 4)}"

        if lat_long_key not in seen_places:
            # Check if the poi name or vicinity contains the city name
            poi_data = f"{poi.get('name', '')} {poi.get('vicinity', '')}".lower()
            is_origin = origin_city.lower() in poi_data
            is_destination = destination_city.lower() in poi_data
            images = []
            if "photos" in poi.keys():
                phot_reference = poi["photos"][0]["photo_reference"]
                photo_width = poi["photos"][0]["width"]
                image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photo_width}&photoreference={phot_reference}&key="
                images.append(image_url)
            unified_place = {
                "business_status": poi.get("business_status", "OPERATIONAL"),
                "location": poi["geometry"]["location"],
                "icon": icon_url,
                "name": poi["name"],
                "place_id": poi["place_id"],
                "in_route": not (is_origin or is_destination),
                "origin": is_origin,
                "destination": is_destination,
                "category_name": category,
                "description": None,
                "rating": poi.get("rating", None),
                "images": images,
            }
            results.append(unified_place)
            seen_places.add(lat_long_key)

    # Fetch from the local database for the given category
    model = MODEL_MAPPING.get(category)
    if model:
        for step in filtered_steps:
            location = step["end_location"]

            # Filter database places based on proximity (10km range assumed)
            db_places = model.objects.filter(
                latitude__range=(location["lat"] - 0.1, location["lat"] + 0.1),
                longitude__range=(location["lng"] - 0.1, location["lng"] + 0.1),
            )
            discount_url = None
            for place in db_places:
                if category == Constant.HOTEL:
                    images = place.images
                    if "discount_url" in place.meta_data.keys():
                        discount_url = place.meta_data["discount_url"]
                    if not images:
                        images = [place.cover_image]
                else:
                    images = place.images
                lat_long_key = f"{round(place.latitude, 4)}_{round(place.longitude, 4)}"
                if lat_long_key not in seen_places:
                    origin_city = origin_city.split(",")[0]
                    destination_city = destination_city.split(",")[0]
                    description = (
                        place.description
                        if place.description
                        else None
                    )
                    if place.city:
                        is_origin = (
                            place.city.name.lower() == origin_city.split(",")[0].lower()
                        )
                        is_destination = (
                            place.city.name.lower()
                            == destination_city.split(",")[0].lower()
                        )
                    else:
                        is_origin, is_destination = False, False

                    # Create a dictionary to map category names to their corresponding liked fields
                    category_to_field = {
                        "Extreme Sports": "liked_extremesports",
                        "Historical Sites": "liked_historicalsites",
                        "Events Calendar": "liked_events",
                        "Weird and Wacky": "liked_wierdandwacky",
                        "National Park": "liked_parks",
                        "Attractions": "liked_attractions",
                        "Hotels": "liked_hotels"
                    }

                    liked_field = category_to_field.get(category)
                    is_favorite = False
                    if liked_field:
                        # Dynamically access the liked field based on the category
                        is_favorite = trip_models.UserLikes.objects.filter(user=user, **{liked_field: place}).exists()

                    unified_place = {
                        "business_status": "OPERATIONAL",
                        "location": {"lat": place.latitude, "lng": place.longitude},
                        "icon": icon_url,
                        "name": place.name,
                        "place_id": None,
                        "id": place.id,
                        "in_route": not (is_origin or is_destination),
                        "origin": is_origin,
                        "destination": is_destination,
                        "category_name": category,
                        "rating": None,
                        "description": description,
                        "images": get_images(images),
                        "discount_url": discount_url,
                        "is_favorite": is_favorite
                    }
                    results.append(unified_place)
                    seen_places.add(lat_long_key)
    return results


def fetch_pois_save_with_route(args):  # for save with route
    """
    Fetches points of interest (POIs) for a given category along a particular route. It fetches both from Google API
    and the local database.

    Parameters:
    - args (tuple): A tuple containing:
        - category (str): The category of interest.
        - filtered_steps (list): Steps/routes to look around.
        - api_key (str): The Google API key.
        - seen_places (set): A set of coordinates (in the form 'lat_lng') already processed.
        - results (list): A list to store the results.

    Returns:
    - list: A list of unified places (both from Google API and the database) matching the category.
    """

    category, filtered_steps, api_key, seen_places, results = args

    # Fetch from Google Places API
    pois = get_pois_along_route(
        filtered_steps, api_key=api_key, type_of_place=CATEGORY_MAPPING[category]
    )

    for poi in pois:
        # Create a unique key based on lat-lng to avoid duplicate places
        lat_long_key = f"{round(poi['geometry']['location']['lat'], 4)}_{round(poi['geometry']['location']['lng'], 4)}"
        category_obj = trip_models.Category.objects.filter(name=category)
        icon_url = category_obj.first().icon_url if category_obj else None
        images = []
        if "photos" in poi.keys():
            phot_reference = poi["photos"][0]["photo_reference"]
            photo_width = poi["photos"][0]["width"]
            image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photo_width}&photoreference={phot_reference}&key="
            images.append(image_url)
        if lat_long_key not in seen_places:
            is_origin = False
            is_destination = False
            unified_place = {
                "business_status": poi.get("business_status", "OPERATIONAL"),
                "location": poi["geometry"]["location"],
                "icon": icon_url,
                "name": poi["name"],
                "place_id": poi["place_id"],
                "in_route": not (is_origin or is_destination),
                "origin": is_origin,
                "destination": is_destination,
                "category_name": category,
                "description": None,
                "meta_data": None,
                "is_scraped": False,
                "images": images,
            }
            results.append(unified_place)
            seen_places.add(lat_long_key)

    # Fetch from the local database for the given category
    model = MODEL_MAPPING.get(category)
    if model:
        for step in filtered_steps:
            location = step["end_location"]

            # Filter database places based on proximity (10km range assumed)
            db_places = model.objects.filter(
                latitude__range=(location["lat"] - 0.1, location["lat"] + 0.1),
                longitude__range=(location["lng"] - 0.1, location["lng"] + 0.1),
            )

            for place in db_places:
                lat_long_key = f"{round(place.latitude, 4)}_{round(place.longitude, 4)}"
                if lat_long_key not in seen_places:
                    # Check if the place is close to origin or destination
                    # is_origin = haversine_distance((place.latitude, place.longitude),
                    #                                filtered_steps[0]['start_location']) < 1.0
                    # is_destination = haversine_distance((place.latitude, place.longitude),
                    #                                     filtered_steps[-1]['end_location']) < 1.0
                    description = (
                        place.description
                        if place.description
                        else None
                    )
                    category_obj = trip_models.Category.objects.filter(name=category)
                    icon_url = category_obj.first().icon_url if category_obj else None
                    is_origin = False
                    is_destination = False
                    unified_place = {
                        "business_status": "OPERATIONAL",
                        "location": {"lat": place.latitude, "lng": place.longitude},
                        "icon": icon_url,
                        "name": place.name,
                        "place_id": place.id,
                        "in_route": not (is_origin or is_destination),
                        "origin": is_origin,
                        "destination": is_destination,
                        "category_name": category,
                        "images": get_images(place.images),
                        "meta_data": place.meta_data,
                        "description": description,
                        "is_scraped": True,
                    }
                    results.insert(0, unified_place)
                    seen_places.add(lat_long_key)
    return results


def fetch_pois_save_for_location(args):  # for save without route
    """
    Fetches points of interest (POIs) for a given category along a particular route. It fetches both from Google API
    and the local database.

    Parameters:
    - args (tuple): A tuple containing:
        - category (str): The category of interest.
        - filtered_steps (list): Steps/routes to look around.
        - api_key (str): The Google API key.
        - seen_places (set): A set of coordinates (in the form 'lat_lng') already processed.
        - results (list): A list to store the results.

    Returns:
    - list: A list of unified places (both from Google API and the database) matching the category.
    """
    category, location, api_key, seen_places, results = args

    # Fetch from Google Places API
    pois = get_pois_around_location(
        location, api_key=api_key, type_of_place=CATEGORY_MAPPING[category]
    )

    for poi in pois:
        # Create a unique key based on lat-lng to avoid duplicate places
        lat_long_key = f"{round(poi['geometry']['location']['lat'], 4)}_{round(poi['geometry']['location']['lng'], 4)}"

        if lat_long_key not in seen_places:
            # Check if the poi is close to origin or destination
            # is_origin = haversine_distance((poi['geometry']['location']['lat'], poi['geometry']['location']['lng']),
            #                                filtered_steps[0]['start_location']) < 1.0
            # is_destination = haversine_distance(
            #     (poi['geometry']['location']['lat'], poi['geometry']['location']['lng']),
            #     filtered_steps[-1]['end_location']) < 1.0
            images = []
            if "photos" in poi.keys():
                phot_reference = poi["photos"][0]["photo_reference"]
                photo_width = poi["photos"][0]["width"]
                image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photo_width}&photoreference={phot_reference}&key="
                images.append(image_url)
            category_obj = trip_models.Category.objects.filter(name=category)
            icon_url = category_obj.first().icon_url if category_obj else poi["icon"]
            is_origin = False
            is_destination = False
            unified_place = {
                "id": None,
                "business_status": poi.get("business_status", "OPERATIONAL"),
                "location": poi["geometry"]["location"],
                "icon": icon_url,
                "name": poi["name"],
                "place_id": poi["place_id"],
                "in_route": not (is_origin or is_destination),
                "origin": is_origin,
                "destination": is_destination,
                "category_name": category,
                "images": images,
                "description": None,
                "meta_data": None,
                "is_scraped": False,
            }
            results.append(unified_place)
            seen_places.add(lat_long_key)

    # Fetch from the local database for the given category
    model = MODEL_MAPPING.get(category)
    if model:
        # Filter database places based on proximity (10km range assumed)
        db_places = model.objects.filter(
            latitude__range=(location["lat"] - 0.1, location["lat"] + 0.1),
            longitude__range=(location["lng"] - 0.1, location["lng"] + 0.1),
        )
        for place in db_places:
            lat_long_key = f"{round(place.latitude, 4)}_{round(place.longitude, 4)}"
            if lat_long_key not in seen_places:
                # Check if the place is close to origin or destination
                # is_origin = haversine_distance((place.latitude, place.longitude),
                #                                filtered_steps[0]['start_location']) < 1.0
                # is_destination = haversine_distance((place.latitude, place.longitude),
                #                                     filtered_steps[-1]['end_location']) < 1.0
                description = (
                    place.description
                    if place.description
                    else None
                )
                category_obj = trip_models.Category.objects.filter(name=category)
                icon_url = category_obj.first().icon_url if category_obj else None
                is_origin = False
                is_destination = False
                unified_place = {
                    "id": place.id,
                    "business_status": "OPERATIONAL",
                    "location": {"lat": place.latitude, "lng": place.longitude},
                    "icon": icon_url,
                    "name": place.name,
                    "place_id": place.id,
                    "in_route": not (is_origin or is_destination),
                    "origin": is_origin,
                    "destination": is_destination,
                    "category_name": category,
                    "images": get_images(place.images),
                    "meta_data": place.meta_data,
                    "description": description,
                    "is_scraped": True,
                }

                results.insert(0, unified_place)
                seen_places.add(lat_long_key)
    return results


def get_place_photos(place_name):
    try:
        url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=place_id&key={settings.GOOGLE_API_KEY}"
        response = requests.get(url)
        data = response.json()
        # Extract Place ID from the result
        place_id = data["candidates"][0]["place_id"] if data.get("candidates") else None
        # Step 2: Use Place Details to get place information including photos
        url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=photos&key={settings.GOOGLE_API_KEY}"
        response = requests.get(url)
        place_details = response.json()
        # Extract photo references
        photos = (
            place_details["result"]["photos"]
            if place_details.get("result", {}).get("photos")
            else []
        )
        if photos:
            # Assuming you have a photo reference
            photo_reference = photos[0]["photo_reference"]
            # Construct the image URL
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key="
        return photo_url
    except Exception as e:
        return ""


def get_key_from_value(target_value):
    for key, value in CATEGORY_MAPPING.items():
        if value == target_value:
            return key


def fetch_pois_for_smart_search(args):
    """
    Fetches points of interest (POIs) for a given category along a particular route. It fetches both from Google API
    and the local database.
    Parameters:
    - args (tuple): A tuple containing:
        - category (str): The category of interest.
        - filtered_steps (list): Steps/routes to look around.
        - api_key (str): The Google API key.
        - seen_places (set): A set of coordinates (in the form 'lat_lng') already processed.
        - results (list): A list to store the results.
    Returns:
    - list: A list of unified places (both from Google API and the database) matching the category.
    """
    category, location, api_key, seen_places, results, data_from_db = args

    # Fetch from Google Places API
    if not data_from_db:
        pois = get_pois_around_location(
            location, api_key=api_key, type_of_place=CATEGORY_MAPPING[category]
        )

        for poi in pois:
            # Create a unique key based on lat-lng to avoid duplicate places
            lat_long_key = f"{round(poi['geometry']['location']['lat'], 4)}_{round(poi['geometry']['location']['lng'], 4)}"

            if lat_long_key not in seen_places:
                unified_place = {"name": poi["name"], "is_scraped": False}
                results.append(unified_place)
                seen_places.add(lat_long_key)
    # Fetch from the local database for the given category
    model = MODEL_MAPPING.get(category)
    if model:
        # Filter database places based on proximity (50km range assumed)
        db_places = model.objects.filter(
            latitude__range=(location["lat"] - 0.5, location["lat"] + 0.5),
            longitude__range=(location["lng"] - 0.5, location["lng"] + 0.5),
        )
        for place in db_places:
            lat_long_key = f"{round(place.latitude, 4)}_{round(place.longitude, 4)}"
            if lat_long_key not in seen_places:
                unified_place = {"name": place.name, "is_scraped": True}

                results.insert(0, unified_place)
                seen_places.add(lat_long_key)
    return results


def save_user_trip_info(log_data, at_start, at_end):
    try:
        log_data["response_time"] = (at_end - at_start).total_seconds()
        UserPlanTripLogs.create_instance(log_data)
    except Exception as ex:
        print(f"{ex}")
