from django.db import models
from django.db.models import JSONField
from apps.trip.choices import ChoicesFields
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from django.contrib.postgres.fields import ArrayField
from apps.trip.services.common import get_geo_code, get_geo_code_area
from apps.trip.services.fetch_image import scrap_images

from apps.user.models import BaseModel, Media, User as user
from common.cloud_service import upload_file_to_aws_s3


class Category(BaseModel):
    """
    A "Category" model in Django typically represents a grouping or classification used
    to categorize and organize items or content within an application, providing a structured
    way to manage and filter data based on specific attributes or characteristics.
    """
    name = models.CharField(max_length=100)
    icon_url = models.URLField(max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    keywords = ArrayField(models.TextField(null=True), default=list)
    scrape = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class PlanCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Plan Category"
        verbose_name_plural = "Plan Categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class TripCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Plan Category"
        verbose_name_plural = "Plan Categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class City(BaseModel):
    """
    "City" model in Django typically represents geographical locations, storing information
    about cities such as their name, country,  latitude and 
    longitude coordinates, enabling applications to manage and query city-related data.
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    images = ArrayField(models.TextField(null=True), default=list)
    description = models.TextField(null=True, blank=True)
    # lat_long = ArrayField(models.TextField(null=True), default=list)
    lat_long = models.JSONField(default=list)
    scrape = models.BooleanField(default=False)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


# class Food(BaseModel):  # have to replace name with Hotels
#     """
#     "Food" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='food_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)

#     class Meta:
#         verbose_name = "Food"
#         verbose_name_plural = "Foods"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class FamilyFun(BaseModel):
#     """
#     "FamilyFun" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='familyfun_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)

#     class Meta:
#         verbose_name = "Family Fun"
#         verbose_name_plural = "Family Fun"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class Attraction(BaseModel):
#     """
#     "Attractions" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     attraction = models.CharField(max_length=200,
#                                   choices=ChoicesFields.ATTRACTIONS_CHOICE,
#                                   blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attraction_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Attraction"
#         verbose_name_plural = "Attractions"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class WeirdAndWacky(BaseModel):
#     """
#     "WeirdAndWacky" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weirdandwacky_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Weird And Wacky"
#         verbose_name_plural = "Weird And Wacky"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class Camp(BaseModel):
#     """
#     "Camp" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='camp_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)

#     class Meta:
#         verbose_name = "Camp"
#         verbose_name_plural = "Camps"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class Park(BaseModel):
#     """
#     "Park" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='park_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Park"
#         verbose_name_plural = "Parks"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


class DriveWebsite(BaseModel):
    """
    "Deeplink URL" in a Django model typically refers to a field that stores a URL pointing
    to a specific internal or external resource, allowing applications to provide direct
    access to relevant content or functionality, enhancing user experience and navigation.
    """
    url_link = models.URLField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='website_category')

    class Meta:
        verbose_name = "DriveWebsite"
        verbose_name_plural = "DriveWebsites"
        ordering = ["-created_at"]

    def __str__(self):
        return self.url_link


# class Event(BaseModel):
#     """
#     "Events" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, blank=True, null=True)
#     type = models.CharField(max_length=200,
#                             choices=ChoicesFields.EVENT_CHOICE,
#                             blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='event_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     description = models.TextField(null=True, blank=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Event"
#         verbose_name_plural = "Events"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class Site(BaseModel):
#     """
#     "Site" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='historicalsite_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
#     description = models.TextField(null=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Historical Site"
#         verbose_name_plural = "Historical Sites"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# class ExtremeSport(BaseModel):
#     """
#     "ExtremeSport" model in Django typically represents objects, individuals, or items with
#     specific attributes and relationships.
#     """
#     name = models.CharField(max_length=500, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='extremesport_city')
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
#     description = models.TextField(null=True)
#     images = ArrayField(models.TextField(null=True), default=list)
#     meta_data = models.JSONField(default=dict)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

#     class Meta:
#         verbose_name = "Extreme Sport"
#         verbose_name_plural = "Extreme Sports"
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.name


# @receiver(post_save, sender=City)
# def post_save_city_image_obj(sender, created, instance, **kwargs):
#     if created:
#         image_scrap_url = DriveWebsite.objects.filter(
#             category=Category.objects.filter(name="City").first()).first().url_link
#         media_obj = scrap_images(instance, image_scrap_url + instance.name)
#         latitude, longitude = get_geo_code(instance.name)
#         instance.image = media_obj
#         instance.latitude = latitude
#         instance.longitude = longitude
#         instance.save()

#
# @receiver(post_save, sender=City)
# def post_save_hotel_obj(sender, created, instance, **kwargs):
#     if created:
#         food_scrap_url = DriveWebsite.objects.filter(
#             category=Category.objects.filter(name="Hotels").first()).first().url_link
#         get_hotel_metadata(instance, food_scrap_url + instance.name + "/")

# class LatLng:
#     def __init__(self, lat, lng):
#         self.lat = lat
#         self.lng = lng


# class Location(models.Model):
#     lat = models.FloatField(null=True)
#     lng = models.FloatField(null=True)


# class Viewport(models.Model):
#     northeast_lat = models.FloatField(null=True)
#     northeast_lng = models.FloatField(null=True)
#     southwest_lat = models.FloatField(null=True)
#     southwest_lng = models.FloatField(null=True)


# class Geometry(models.Model):
#     location = models.OneToOneField(Location, on_delete=models.CASCADE)
#     viewport = models.OneToOneField(Viewport, on_delete=models.CASCADE)


# class Photo(models.Model):
#     height = models.IntegerField()
#     width = models.IntegerField()
#     html_attributions = models.TextField()
#     photo_reference = models.CharField(max_length=255)


# class PlusCode(models.Model):
#     compound_code = models.CharField(max_length=250)
#     global_code = models.CharField(max_length=250)


class Status(models.Model):
    class Meta:
        db_table = '"status"'
    title = models.CharField(max_length=50)


class Media(models.Model):
    class Meta:
        db_table = '"media"'
    media = models.CharField(max_length=200)


class Plan(models.Model):
    class Meta:
        db_table = '"plan"'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)


class PlanUser(models.Model):
    class Meta:
        db_table = 'plan_user'
        unique_together = (('plan', 'user'),)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LatLng:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


# class Location(models.Model):
#     lat = models.FloatField(null=True)
#     lng = models.FloatField(null=True)


# class Viewport(models.Model):
#     northeast_lat = models.FloatField(null=True)
#     northeast_lng = models.FloatField(null=True)
#     southwest_lat = models.FloatField(null=True)
#     southwest_lng = models.FloatField(null=True)


# class Geometry(models.Model):
#     location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
#     viewport = models.OneToOneField(Viewport, on_delete=models.CASCADE, null=True)

# class Geometry(models.Model):
#     location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True)
#     viewport = models.OneToOneField(Viewport, on_delete=models.CASCADE,null=True)


class Photo(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    html_attributions = models.TextField()
    photo_reference = models.CharField(max_length=255)


# class PlusCode(models.Model):
#     compound_code = models.CharField(max_length=250)
#     global_code = models.CharField(max_length=250)


class Site(BaseModel):
    """
    Represents hotel entities with details about the hotel, its facilities,
    policies, reviews, geographical data, images, and other related metadata.
    """
    place_id = models.CharField(max_length=500, null=True)  # Removed unique=True
    ad_status = models.IntegerField(default=0)  # Removed unique=True
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.TextField(null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name="city", null=True)
    description = models.TextField(null=True)
    contact_info = models.JSONField(default=dict)
    check_in_data = models.JSONField(default=dict)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    reviews = models.JSONField(default=dict)
    amenities = models.JSONField(default=dict)
    service_amenities = models.JSONField(default=dict)
    facility_overview = models.TextField(null=True, blank=True)
    policy = models.JSONField(default=dict)
    meta_data = models.JSONField(default=dict)
    cover_image = models.TextField(null=True)
    images = ArrayField(models.TextField(null=True), default=list)
    address = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0, null=True)
    user_ratings_total = models.IntegerField(default=0, null=True)
    start_price = models.FloatField(null=True)
    end_price = models.FloatField(null=True)
    icon = models.CharField(max_length=500, blank=True, null=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)
    discount_url = models.CharField(max_length=400, null=True)
    business_status = models.CharField(max_length=50, null=True)
    icon_background_color = models.CharField(max_length=10, null=True)
    icon_mask_base_uri = models.URLField(null=True)
    open_now = models.BooleanField(default=False)
    reference = models.CharField(max_length=50, null=True)
    scope = models.CharField(max_length=50, null=True)
    types = models.TextField(null=True)  # Will be stored as a comma-separated string
    keyword = models.CharField(max_length=255,null=True)  # Keyword using which this site is scraped
    vicinity = models.CharField(max_length=255, null=True)
    photos = models.ManyToManyField(Photo)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["place_id", "category"],
                name="unique_place_category"
            )  # Enforces unique composite key
        ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    # def updateLocationInSite(self):
    #     """
    #     Updates the latitude and longitude of the Site instance
    #     using the associated Geometry's Location model.
    #     """
    #     if self.geometry and self.geometry.location:
    #         with transaction.atomic():  # Ensures atomicity of the operation
    #             self.latitude = self.latitude  # Fetch latitude from Location
    #             self.longitude = self.plan.longitude  # Fetch longitude from Location
    #             self.save()

# class UserLikes(models.Model):
#     user = models.OneToOneField(user, on_delete=models.CASCADE)
#     liked_hotels = models.ManyToManyField(Hotel)
#     liked_extremesports = models.ManyToManyField(ExtremeSport)
#     liked_historicalsites = models.ManyToManyField(HistoricalSite)
#     liked_events = models.ManyToManyField(Event)
#     liked_wierdandwacky = models.ManyToManyField(WeirdAndWacky)
#     liked_parks = models.ManyToManyField(Park)
#     liked_attractions = models.ManyToManyField(Attraction)


class UserLikes(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)

    # liked_hotels_new = models.ManyToManyField(Hotel, through='UserLikesHotel')
    # liked_extremesports_new = models.ManyToManyField(ExtremeSport, through='UserLikesExtremeSport')
    liked_sites_new = models.ManyToManyField(Site, through='UserLikesSite')
    # liked_events_new = models.ManyToManyField(Event, through='UserLikesEvent')
    # liked_wierdandwacky_new = models.ManyToManyField(WeirdAndWacky, through='UserLikesWeirdAndWacky')
    # liked_parks_new = models.ManyToManyField(Park, through='UserLikesPark')
    # liked_attractions_new = models.ManyToManyField(Attraction, through='UserLikesAttraction')


# class UserLikesHotel(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


# class UserLikesExtremeSport(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     extremesport = models.ForeignKey(ExtremeSport, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class UserLikesSite(models.Model):
    userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


# class UserLikesEvent(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


# class UserLikesWeirdAndWacky(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     weirdandwacky = models.ForeignKey(WeirdAndWacky, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


# class UserLikesPark(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     park = models.ForeignKey(Park, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


# class UserLikesAttraction(models.Model):
#     userlikes = models.ForeignKey(UserLikes, on_delete=models.CASCADE)
#     attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.first_name


class Itinerary(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    # hotel_itinerary = models.ManyToManyField(Hotel, through='ItineraryHotel')
    # extremesports_itinerary = models.ManyToManyField(ExtremeSport, through='ItineraryExtremeSport')
    sites_itinerary = models.ManyToManyField(Site, through='ItinerarySite')
    # events_itinerary = models.ManyToManyField(Event, through='ItineraryEvent')
    # wierdandwacky_itinerary = models.ManyToManyField(WeirdAndWacky, through='ItineraryWeirdAndWacky')
    # parks_itinerary = models.ManyToManyField(Park, through='ItineraryPark')
    # attractions_itinerary = models.ManyToManyField(Attraction, through='ItineraryAttraction')


# class ItineraryHotel(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)


# class ItineraryExtremeSport(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     extremesport = models.ForeignKey(ExtremeSport, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)


class ItinerarySite(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)


# class ItineraryEvent(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)


# class ItineraryWeirdAndWacky(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     weirdandwacky = models.ForeignKey(WeirdAndWacky, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)


# class ItineraryPark(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     park = models.ForeignKey(Park, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)


# class ItineraryAttraction(models.Model):
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
#     attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.user.first_name

 # -------- add values to the follwoing -------------


class Country(models.Model):
    class Meta:
        db_table = '"country"'
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=80)
    nicename = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3)
    numeric_code = models.IntegerField(null=True)
    phone_code = models.CharField(max_length=10, null=True)


class Priority(models.Model):
    class Meta:
        db_table = '"priority"'
    name = models.CharField(max_length=80)


class TravelGoal(models.Model):
    class Meta:
        db_table = '"travel_goal"'
    name = models.CharField(max_length=80)


class Motivation(models.Model):
    class Meta:
        db_table = '"motivation"'
    name = models.CharField(max_length=80)
    emoji = models.CharField(max_length=80)


class AirlineBrand(models.Model):
    class Meta:
        db_table = '"airline_brand"'
    name = models.CharField(max_length=80)


class RentalCars(models.Model):
    class Meta:
        db_table = '"rental_cars"'
    name = models.CharField(max_length=80)


class HotelBrand(models.Model):
    class Meta:
        db_table = '"hotel_brand"'
    name = models.CharField(max_length=80)


class RestaurantBrand(models.Model):
    class Meta:
        db_table = '"restaurant_brand"'
    name = models.CharField(max_length=80)
