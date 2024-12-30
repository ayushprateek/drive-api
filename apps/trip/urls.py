from django.urls import path
from apps.trip import views as trip_views
from .views import *

app_name = 'trip'

urlpatterns = [
    path('bulk_upload/', trip_views.BulkUploadAPIView.as_view(), name='bulk_upload'),
    # path('add/hotel/', trip_views.AddHotelAPIView.as_view(), name='add_hotel'),
    path('add/site/', trip_views.AddSiteAPIView.as_view(), name='add_data'),
    path('list/', trip_views.CategoryWiseListAPIView.as_view(), name='get_category_based_data'),
    path('category/list/', trip_views.CategoryListAPIView.as_view(), name='get_category_list'),
    path('city/list/', trip_views.CityListAPIView.as_view(), name='get_city_list'),
    path('city/details/', trip_views.CityDetailAPIView.as_view(), name='get_city_details'),
    path('plan/list/', trip_views.TripPlanListAPIView.as_view(), name='get_planned_trip_list_view'),
    path('plan/', trip_views.TripPlanAPIView.as_view(), name='trip-api'),
    path('save/', trip_views.TripSaveAPIView.as_view(), name='trip-save-api'),
    path('like/', trip_views.UserLikeAPIView.as_view(), name='user-like-api'),
    # path('scrape/', ScrapeHotelsView.as_view(), name='scrape_hotels'),
    path('getHotels/', getAllHotels),
    path('get-hotels-along-route/', get_coordinates_along_polyline),
    # todo: uncomment
    path('temp-save-hotel/', saveHotel),
    # path('fetch_latestHotels/', fetch_latestHotels),
    path('truncate_all_tables/', truncate_all_tables),
    path('printRoot/', printRoot),
    path('city-scrape/', cityScrape),
    path('create-trip/', createTripPlan, name='create-trip'),
    path('get-trip/', getTripPlan, name='create-trip'),
    path('get-itinerary-plan-via-site/', getItineraryPlanViaSite, name='create-trip'),
    path('get-all-cities/', getCityList, name='create-trip'),
    path('get-trip-via-id/<id>', getTripViaId, name='create-trip'),
    path('delete-plan/<id>', deletePlan, name='create-trip'),
    path('get-site-via-id/<id>', getSiteViaId, name='create-trip'),
    path('city-search/', SearchCityListAPIView.as_view(), name='city-search'),
    # path('historicalSitesScrape/', sitesScrape, name='city-search'),
    path('get-historical-sites/', getSites, name='create-trip'),
    # path('get-experience-sites/', getExperienceSites, name='create-trip'),
    # path('get-hotel-sites/', getHotelSites, name='create-trip'),
    # path('get-park-sites/', getParkSites, name='create-trip'),
    # path('get-event-sites/', getEventSites, name='create-trip'),
    # path('GetExtremeSport/', getExtremeSport, name='create-trip'),
    # path('GetWeirdAndWacky/', getWeirdAndWacky, name='create-trip'),
    # path('weird/', weird, name='create-trip'),
    path('like-place/', likePlace, name='create-trip'),
    path('unlike-place/', unlikePlace, name='create-trip'),
    path('is-place-liked/', isPlaceLiked, name='create-trip'),
    path('is-place-liked-in-plan/', isPlaceLikedInPlan, name='create-trip'),
    path('add-user-to-plan/', addUserToPlan, name='add-user'),
    path('get-liked-sites-via-plan/', getLikedSitesViaPlan, name='add-user'),
    path('add-country/', addCountry, name='add-user'),
    path('get-all-country/', getAllCountry, name='add-user'),
    path('get-all-priority/', getAllPriority, name='add-user'),
    path('get-all-travel-goal/', getAllTravelGoal, name='add-user'),
    path('get-all-motivation/', getAllMotivation, name='add-user'),
    path('get-all-hotel-brand/', getAllHotelBrand, name='add-user'),
    path('get-all-airline-brand/', getAllAirlineBrand, name='add-user'),
    path('get-all-restaurant-brand/', getAllRestaurantBrand, name='add-user'),
    path('get-plan-users/', getUserAssignedToPlan, name='add-user'),
    path('get-trip-filter/', getTripFilter, name='add-user'),
    path('addtripplancategory/', addTrip, name='add trip plan'),
    path('get-trip-plan-category/', getTripPlanCategory, name='add trip plan'),
    path('get-sites-near-me/', getSitesNearMe, name='add trip plan'),
    path('save-to-itinerary/', saveToItinerary, name='add trip plan'),
    path('is-place-in-itinerary/', isPlaceInItinerary, name='add trip plan'),
    path('get-itinerary-via-plan/', getItineraryViaPlan, name='add trip plan'),
    path('get-itinerary-filter/', getItineraryFilter, name='add-user'),
    path('save-city-category-site/', getItineraryFilter, name='add-user'),
    path('get-ad/', getAd, name='add-user'),
    path('get-place-description/', get_place_description, name='add-user'),
    path('new-scrape-api/', newScrapeAPI, name='add-user'),
    path('new-scrape-amenities/', newAmenitiesScrapeAPI, name='add-user'),
    path('new-scrape-client-data/', newScrapeClientData, name='add-user'),
    path('get-photo-via-site/<id>', getPhotoViaSite, name='add-user'),
    # path('update-location-in-site/', updateLocationInSite, name='add-user'),
]
