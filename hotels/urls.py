from django.urls import path
from .views import *

urlpatterns = [
    # path('scrape/', ScrapeHotelsView.as_view(), name='scrape_hotels'),
    # path('get_hotels/', getAllHotels),
    path('get-hotels-along-route/', get_coordinates_along_polyline),
    path('temp-save-hotel/', saveHotel),
    path('fetch_latestHotels/', fetch_latestHotels),
    path('truncate_all_tables/', truncate_all_tables),
]
