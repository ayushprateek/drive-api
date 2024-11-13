# from django.db import models
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
#     compound_code = models.CharField(max_length=50)
#     global_code = models.CharField(max_length=50)

# class Hotel(models.Model):  # Renamed from Result to Hotel
#     business_status = models.CharField(max_length=50,null=True)
#     geometry = models.OneToOneField(Geometry, on_delete=models.CASCADE,null=True)
#     icon = models.URLField()
#     icon_background_color = models.CharField(max_length=10,null=True)
#     icon_mask_base_uri = models.URLField(null=True)
#     name = models.CharField(max_length=255)
#     open_now = models.BooleanField(default=False)
#     place_id = models.CharField(max_length=50)
#     plus_code = models.OneToOneField(PlusCode, on_delete=models.CASCADE,null=True)
#     rating = models.FloatField(null=True)
#     reference = models.CharField(max_length=50,null=True)
#     scope = models.CharField(max_length=50,null=True)
#     types = models.TextField(null=True)  # Will be stored as a comma-separated string
#     user_ratings_total = models.IntegerField()
#     vicinity = models.CharField(max_length=255,null=True)
#     photos = models.ManyToManyField(Photo)
#     discount_url=models.CharField(max_length=400,null=True)




# class Status(models.Model):
#     class Meta:
#         db_table = '"status_status"'
#     title = models.CharField(max_length=50)
    
# class Media(models.Model):
#     class Meta:
#         db_table = '"media_hotel_media"'
#     media = models.CharField(max_length=200)
    
# # class Hotel(models.Model):
# #     place_id = models.CharField(max_length=255, unique=True)
# #     name = models.CharField(max_length=255)
# #     address = models.CharField(max_length=255, blank=True, null=True)
# #     rating = models.FloatField(default=0)
# #     user_ratings_total = models.IntegerField(default=0)
# #     start_price = models.FloatField(null=True)
# #     end_price = models.FloatField(null=True)
# #     latitude = models.FloatField(null=True)
# #     longitude = models.FloatField(null=True)
# #     icon = models.CharField(max_length=500, blank=True, null=True)
# #     media = models.ForeignKey(Media, on_delete=models.CASCADE,null=True)

# #     def __str__(self):
# #         return self.name
    
# class HotelMedia(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     media = models.ForeignKey(Media, on_delete=models.CASCADE)
#     status = models.IntegerField(default=1)
#     position = models.IntegerField(default=1)
#     class Meta:
#         db_table = 'hotel_media'

#     def __str__(self):
#         return f"HotelMedia(hotel_id={self.hotel_id}, media_id={self.media_id})"
    
# class Customer(models.Model):
#     class Meta:
#         db_table = '"customer"'
#     name = models.CharField(max_length=50)
#     token = models.CharField(max_length=250,null=True)
#     mobile = models.CharField(max_length=10)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     reward = models.DecimalField(max_digits=10, decimal_places=2)
#     status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True,default=1)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=True)
#     # @staticmethod
#     # def get_customer_by_mobile_and_password(mobile, password):
#         # return Customer.objects.filter(mobile=mobile, password=password)
#     def __str__(self):
#         return self.email
# class Tax(models.Model):
#     class Meta:
#         db_table = '"tax"'
#     name = models.CharField(max_length=50)
#     percentage = models.DecimalField(max_digits=10, decimal_places=2) 


    
# class Category(models.Model):
#     class Meta:
#         db_table='"category"'
#     name = models.CharField(max_length=50)
#     media=models.ForeignKey(Media, on_delete=models.CASCADE,null=True,default=1)
#     trip_date = models.DateTimeField(null=False)
#     status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True,default=1)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=True)
    
# class Article(models.Model):
#     class Meta:
#         db_table='"article"'
#     name = models.CharField(max_length=50)
#     short_description = models.CharField(max_length=200)
#     url = models.CharField(max_length=200)
#     status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True,default=1)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=True)

# class Banner(models.Model):
#     class Meta:
#         db_table='"banner"'
    
    
