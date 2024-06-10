from ast import Constant
from apps.trip.choices import ChoicesFields
from apps.trip.helper import get_images, get_place_photos
from apps.user.models import User
from rest_framework import serializers
from apps.trip import models as trip_models
from common.constants import Constant


class AttractionModelSerializer(serializers.ModelSerializer):
    """Prepares Serialized Objects

    Args:
        serializers (_type_): returns dict of objects
    """
    city_name = serializers.CharField(source="city.name", required=False)
    images = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    is_favorite = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = trip_models.Attraction
        fields = ("id", "name", "is_favorite", "city_name", "latitude",
                  "longitude", "description", "images",
                  "meta_data")

    def get_name(self, obj):
        try:
            if obj.name:
                return " ".join(obj.name.split("-")).title()
        except Exception:
            return obj.name

    def get_images(self, obj):
        if obj.images:
            return get_images(obj.images)
        return []

    def get_is_favorite(self, obj):
        user_id = self.context["request"].user.id
        category_name = self.context["category"]

        # Create a dictionary to map category names to their corresponding liked fields
        category_to_field = {
            "Extreme Sports": "liked_extremesports",
            "Historical Sites": "liked_historicalsites",
            "Events Calendar": "liked_events",
            "Weird and Wacky": "liked_wierdandwacky",
            "National Park": "liked_parks",
            "Attractions": "liked_attractions",
        }

        liked_field = category_to_field.get(category_name)

        if liked_field:
            # Dynamically access the liked field based on the category
            is_favorited = trip_models.UserLikes.objects.filter(user=user_id, **{liked_field: obj}).exists()
            return is_favorited

        return False


class HotelModelSerializer(serializers.ModelSerializer):
    """Prepares Serialized Objects

    Args:
        serializers (_type_): returns in dict of hotel objects
    """
    city_name = serializers.CharField(source="city.name", required=False)
    images = serializers.SerializerMethodField(read_only=True)
    is_favorite = serializers.SerializerMethodField(read_only=True)



    class Meta:
        model = trip_models.Hotel
        fields = ("id", "name", "is_favorite", "city_name", "latitude",
                  "longitude", "contact_info","check_in_data", "address",
                  "hotel_reviews", "amenities", "service_amenities", "facility_overview",
                  "hotel_policy", "meta_data",
                  "description", "images", "cover_image")
    
    def get_images(self, obj):
        if obj.images:
            return get_images(obj.images)
        return []

    def get_is_favorite(self, obj):
        user_id = self.context["request"].user.id
        is_favorited = trip_models.UserLikes.objects.filter(user=user_id, liked_hotels=obj).exists()
        return is_favorited

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = trip_models.Category
        fields = ("id", "name", "image_url", "icon_url")


class CommonSerializer(serializers.Serializer):
    """Prepares Serialized Objects

    Args:
        serializers (_type_): returns dict of objects
    """
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    images = serializers.ListField(read_only=True)
    id = serializers.UUIDField(required=True)

    class Meta:
        fields = ("id", "name", "description", "images")

    def get_name(self, obj):
        if obj.id:
            return obj.id
        return ""

    def get_name(self, obj):
        if obj.name:
            return obj.name
        return ""
    
    def get_description(self, obj):
        if obj.description:
            return obj.description
        return ""

    def get_images(self, obj):
        if obj.images:
            return obj.images
        return []

class CitySerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (dict): return serialized city objects

    Returns:
        _type_: return list of items related to city with attributes
    """
    components = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    is_favorite = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = trip_models.City
        fields = ["id", "name", "latitude", "longitude", "description",
                  "images", "name", "components", "is_favorite",]

    def get_images(self, obj):
        if obj.images:
            return obj.images
        images = [get_place_photos(obj.name)]
        return images

    def get_is_favorite(self, obj):
        try:
            user_obj = User.objects.filter(id=self.context["request"].user.id).first()
            if user_obj:
                if str(obj.id) in user_obj.meta_data["cities"]:
                    return True
                else:
                    return False
        except Exception:
            return False


    def get_components(self, obj):
        """_summary_

        Args:
            obj (city_obj): city obj got from the request

        Returns:
            list: return in list of data for individual category
        """
        component_list = []

        # Extract Hotel Obj.
        hotel_obj = trip_models.Hotel.filter_instance({"city":obj}).first()
        if hotel_obj:
            component_list.append({"type": Constant.HOTEL,
                                   **CommonSerializer(hotel_obj).data})

        # Extract Attraction Obj.
        attraction_obj = trip_models.Attraction.filter_instance({"city":obj}).first()
        if attraction_obj:
            component_list.append({"type": Constant.ATTRACTION,
                                   **CommonSerializer(attraction_obj).data})

        # Extract Food Obj.
        food_obj = trip_models.Food.filter_instance({"city":obj}).first()
        if food_obj:
            component_list.append({"type": Constant.FOOD,
                                   **CommonSerializer(food_obj).data})

        # Extract WeirdAndWacky Obj. 
        weirdandwacky_obj = trip_models.WeirdAndWacky.filter_instance({"city":obj}).first()
        if weirdandwacky_obj:
            component_list.append({"type": Constant.WEIRDANDWACKY,
                                   **CommonSerializer(weirdandwacky_obj).data})

        # Extract Camp Obj.
        camp_obj = trip_models.Camp.filter_instance({"city":obj}).first()
        if camp_obj:
            component_list.append({"type": Constant.CAMPING,
                                   **CommonSerializer(camp_obj).data})

        # Extract Park Obj.
        park_obj = trip_models.Park.filter_instance({"city":obj}).first()
        if park_obj:
            component_list.append({"type": Constant.NATIONAL_PARK,
                                   **CommonSerializer(park_obj).data})

        # Extract Historical Site Obj.
        historical_site_obj = trip_models.HistoricalSite.filter_instance({"city":obj}).first()
        if historical_site_obj:
            component_list.append({"type": Constant.HISTORICAL_SITES,
                                   **CommonSerializer(historical_site_obj).data})

        # Extract Family Fun Obj.
        family_fun_obj = trip_models.FamilyFun.filter_instance({"city":obj}).first()
        if family_fun_obj:
            component_list.append({"type": Constant.FAMILY_FUN,
                                   **CommonSerializer(family_fun_obj).data})

        # Extract Extreme Sports Obj.
        extreme_sports_obj = trip_models.ExtremeSport.filter_instance({"city":obj}).first()
        if extreme_sports_obj:
            component_list.append({"type": Constant.EXTREME_SPORTS,
                                   **CommonSerializer(extreme_sports_obj).data})

        # Extract Event Obj.
        event_obj = trip_models.Event.filter_instance({"city":obj}).first()
        if event_obj:
            component_list.append({"type": Constant.EVENT_CALENDAR,
                                   **CommonSerializer(event_obj).data})

        return component_list


class LocationSerializer(serializers.Serializer):
    """
    A serializer for validating location data.
    """
    name = serializers.CharField()
    place_id = serializers.CharField()


class TripPlanSerializer(serializers.Serializer):
    origin = LocationSerializer()
    destination = LocationSerializer()
    categories = serializers.ListField(child=serializers.CharField())
    travel_time = serializers.CharField(required=False, allow_null=True)
    discount_type = serializers.CharField(required=False, allow_null=True)



class TripSaveSerializer(serializers.Serializer):
    origin = LocationSerializer(required=False)
    destination = LocationSerializer(required=False)
    base_location = LocationSerializer(required=False)
    # categories = serializers.ListField(child=serializers.CharField())
    discount_type = serializers.CharField(required=False)
    view_type = serializers.CharField(required=False)


class CityDetailSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (dict): return serialized city objects

    Returns:
        _type_: return list of items related to city with attributes
    """
    components = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    is_favorite = serializers.SerializerMethodField(read_only=True)



    class Meta:
        model = trip_models.City
        fields = ["id", "name", "latitude", "longitude", "description",
                  "images", "name", "components", "is_favorite"]

    def get_images(self, obj):
        if obj.images:
            return obj.images
        images = [get_place_photos(obj.name)]
        return images

    def get_components(self, obj):
        """_summary_

        Args:
            obj (city_obj): city obj got from the request

        Returns:
            list: return in list of data for individual category
        """
        component_list = []

        # Extract Hotel Obj.
        hotel_obj = trip_models.Hotel.filter_instance({"city":obj})
        if hotel_obj:
            data = CommonSerializer(hotel_obj[:3], many=True).data
            component_list.append({"type": Constant.HOTEL,
                                   "image_url": trip_models.Category.get_instance(
                                       {"name":Constant.HOTEL}).image_url,
                                   "total_count": hotel_obj.count(),
                                   "data":data
                                   })

        # Extract Attraction Obj.
        attraction_obj = trip_models.Attraction.filter_instance({"city":obj})
        if attraction_obj:
            data = CommonSerializer(attraction_obj[:3], many=True).data
            component_list.append({"type": Constant.ATTRACTION,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.ATTRACTION}).image_url,
                                   "total_count": attraction_obj.count(),
                                   "data":data})

        # Extract Food Obj.
        food_obj = trip_models.Food.filter_instance({"city":obj})
        if food_obj:
            data = CommonSerializer(food_obj[:3], many=True).data
            component_list.append({"type": Constant.FOOD,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.FOOD}).image_url,
                                   "total_count": food_obj.count(),
                                   "data":data})

        # Extract WeirdAndWacky Obj. 
        weirdandwacky_obj = trip_models.WeirdAndWacky.filter_instance({"city":obj})
        if weirdandwacky_obj:
            data = CommonSerializer(weirdandwacky_obj[:3], many=True).data
            component_list.append({"type": Constant.WEIRDANDWACKY,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.WEIRDANDWACKY}).image_url,
                                   "total_count": weirdandwacky_obj.count(),
                                   "data":data})

        # Extract Camp Obj.
        camp_obj = trip_models.Camp.filter_instance({"city":obj})
        if camp_obj:
            data = CommonSerializer(camp_obj[:3], many=True).data
            component_list.append({"type": Constant.CAMPING,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.CAMPING}).image_url,
                                   "total_count": camp_obj.count(),
                                   "data":data})

        # Extract Park Obj.
        park_obj = trip_models.Park.filter_instance({"city":obj})
        if park_obj:
            data = CommonSerializer(park_obj[:3], many=True).data
            component_list.append({"type": Constant.NATIONAL_PARK,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.NATIONAL_PARK}).image_url,
                                   "total_count": park_obj.count(),
                                   "data":data})

        # Extract Historical Site Obj.
        historical_site_obj = trip_models.HistoricalSite.filter_instance({"city":obj})
        if historical_site_obj:
            data = CommonSerializer(historical_site_obj[:3], many=True).data
            component_list.append({"type": Constant.HISTORICAL_SITES,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.HISTORICAL_SITES}).image_url,
                                   "total_count": historical_site_obj.count(),
                                   "data":data})

        # Extract Family Fun Obj.
        family_fun_obj = trip_models.FamilyFun.filter_instance({"city":obj})
        if family_fun_obj:
            data = CommonSerializer(family_fun_obj[:3], many=True).data
            component_list.append({"type": Constant.FAMILY_FUN,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.FAMILY_FUN}).image_url,
                                    "total_count": family_fun_obj.count(),
                                   "data":data})

        # Extract Extreme Sports Obj.
        extreme_sports_obj = trip_models.ExtremeSport.filter_instance({"city":obj})
        if extreme_sports_obj:
            data = CommonSerializer(extreme_sports_obj[:3], many=True).data
            component_list.append({"type": Constant.EXTREME_SPORTS,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.EXTREME_SPORTS}).image_url,
                                    "total_count": extreme_sports_obj.count(),
                                   "data":data})                                   

        # Extract Event Obj.
        event_obj = trip_models.Event.filter_instance({"city":obj})
        if event_obj:
            data = CommonSerializer(event_obj[:3], many=True).data
            component_list.append({"type": Constant.EVENT_CALENDAR,
                                    "image_url": trip_models.Category.get_instance(
                                        {"name":Constant.EVENT_CALENDAR}).image_url,
                                   "total_count": event_obj.count(),
                                   "data":data})
        return component_list

    def get_is_favorite(self, obj):
        try:
            user_obj = User.objects.filter(id=self.context["request"].user.id).first()
            if user_obj:
                if str(obj.id) in user_obj.meta_data["cities"]:
                    return True
                else:
                    return False
        except Exception:
            return False
