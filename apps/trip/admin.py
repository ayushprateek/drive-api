from django.contrib import admin
from apps.trip import models as trip_models


@admin.register(trip_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    The CategoryAdmin class specifies how the Category model should be displayed and filtered
    in the admin interface. It sets up filters for the id and name fields, enables searching
    for these fields, and specifies the columns to display in the list view as id and name.
    """
    search_fields = ['id', 'name']
    list_display = ['id', 'name']


@admin.register(trip_models.City)
class CityAdmin(admin.ModelAdmin):
    """
    The CityAdmin class specifies how the City model should be displayed and filtered
    in the admin interface. It sets up filters for the id, name, latitude, and
    longitude fields, enables searching for these fields, and specifies the columns
    to display in the list view as id, name, latitude, and longitude.
    """
    search_fields = ['id', 'name', 'latitude', 'longitude']
    list_display = ['id', 'name', 'latitude', 'longitude']


# @admin.register(trip_models.DriveWebsite)
# class DriveWebsiteAdmin(admin.ModelAdmin):
#     """
#     The DriveWebsiteAdmin class specifies how the DriveWebsite model should be displayed
#     and filtered in the admin interface. It sets up filters for the id, url_link, and
#     category fields, enables searching for these fields, and specifies the columns to
#     display in the list view as id, url_link, and category.
#     """
#     list_filter = ['id', 'url_link', 'category']
#     search_fields = ['id', 'url_link', 'category']
#     list_display = ['id', 'url_link', 'category']


# @admin.register(trip_models.Food)
# class FoodAdmin(admin.ModelAdmin):
#     """
#     The FoodAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.FamilyFun)
# class FamilyFunAdmin(admin.ModelAdmin):
#     """
#     The FamilyFunAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.Attraction)
# class AttractionAdmin(admin.ModelAdmin):
#     """
#     The AttractionAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.WeirdAndWacky)
# class WeirdAndWackyAdmin(admin.ModelAdmin):
#     """
#     The WeirdAndWackyAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.Camp)
# class CampAdmin(admin.ModelAdmin):
#     """
#     The CampAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.Park)
# class ParkAdmin(admin.ModelAdmin):
#     """
#     The ParkAdmin class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.    
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


@admin.register(trip_models.Site)
class SiteAdmin(admin.ModelAdmin):
    """
    The HistoricalSite class specifies how the Entity model should be displayed and filtered
    in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
    and category fields, enables searching for these fields, and specifies the columns
    to display in the list view as id, name, city, latitude, longitude, and category.
    """
    list_filter = ['city']
    search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
    list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.Event)
# class EventAdmin(admin.ModelAdmin):
#     """
#     The Event class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


# @admin.register(trip_models.ExtremeSport)
# class ExtremeSportAdmin(admin.ModelAdmin):
#     """
#     The ExtremeSport class specifies how the Entity model should be displayed and filtered
#     in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
#     and category fields, enables searching for these fields, and specifies the columns
#     to display in the list view as id, name, city, latitude, longitude, and category.
#     """
#     list_filter = ['city']
#     search_fields = ['id', 'name', 'city', 'latitude', 'longitude']
#     list_display = ['id', 'name', 'city', 'latitude', 'longitude']


@admin.register(trip_models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    """
    The ExtremeSport class specifies how the Entity model should be displayed and filtered
    in the admin interface. It sets up filters for the id, name, city, latitude, longitude,
    and category fields, enables searching for these fields, and specifies the columns
    to display in the list view as id, name, city, latitude, longitude, and category.
    """
    list_filter = ['name']
    search_fields = ['id', 'name']
    list_display = ['id', 'name']
    exclude = ["cover_image"]


@admin.register(trip_models.UserLikes)
class UserLikesAdmin(admin.ModelAdmin):
    """
    The UserLikes class specifies how the UserLikes model should be displayed and filtered
    """
    search_fields = ['id']
    list_display = ['id']
