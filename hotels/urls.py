from django.urls import path
from .views import *

urlpatterns = [
    path('scrape/', ScrapeHotelsView.as_view(), name='scrape_hotels'),
    path('get_hotels/', getAllHotels),
    path('get-hotels-along-route/', get_coordinates_along_polyline),
]
