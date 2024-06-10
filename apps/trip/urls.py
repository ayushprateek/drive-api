from django.urls import path
from apps.trip import views as trip_views

app_name = 'trip'

urlpatterns = [
    path('bulk_upload/', trip_views.BulkUploadAPIView.as_view(), name='bulk_upload'),
    path('add/hotel/', trip_views.AddHotelAPIView.as_view(), name='add_hotel'),
    path('add/site/', trip_views.AddSiteAPIView.as_view(), name='add_data'),
    path('list/', trip_views.CategoryWiseListAPIView.as_view(), name='get_category_based_data'),
    path('category/list/', trip_views.CategoryListAPIView.as_view(), name='get_category_list'),
    path('city/list/', trip_views.CityListAPIView.as_view(), name='get_city_list'),
    path('city/details/', trip_views.CityDetailAPIView.as_view(), name='get_city_details'),
    path('plan/list/', trip_views.TripPlanListAPIView.as_view(), name='get_planned_trip_list_view'),
    path('plan/', trip_views.TripPlanAPIView.as_view(), name='trip-api'),
    path('save/', trip_views.TripSaveAPIView.as_view(), name='trip-save-api'),
    path('like/', trip_views.UserLikeAPIView.as_view(), name='user-like-api'),

]
