from django.urls import path
from apps.trip import views as trip_views
from .views import *

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
    path('scrape/', ScrapeHotelsView.as_view(), name='scrape_hotels'),
    path('getHotels/', getAllHotels),
    path('get-hotels-along-route/', get_coordinates_along_polyline),
    # todo: uncomment
    # path('temp-save-hotel/', saveHotel),
    path('fetch_latestHotels/', fetch_latestHotels),
    path('truncate_all_tables/', truncate_all_tables),
    path('printRoot/', printRoot),
    path('city-scrape/', cityScrape),
    path('create-trip/', createTripPlan,name='create-trip'),
    path('get-trip/', getTripPlan,name='create-trip'),
    path('get-trip-via-id/<id>', getTripViaId,name='create-trip'),
    path('city-search/', SearchCityListAPIView.as_view(), name='city-search'),
    path('historicalSitesScrape/', historicalSitesScrape, name='city-search'),
    path('get-historical-sites/', getHistoricalsites,name='create-trip'),
    path('GetExtremeSport/', getExtremeSport,name='create-trip'),
    path('GetWeirdAndWacky/', getWeirdAndWacky,name='create-trip'),
    path('weird/', weird,name='create-trip'),
    path('like-place/', likePlace,name='create-trip'),
    path('unlike-place/', unlikePlace,name='create-trip'),
    path('is-place-liked/', isPlaceLiked,name='create-trip'),
    path('add-user-to-plan/', addUserToPlan,name='add-user'),
]
