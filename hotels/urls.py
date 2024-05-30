from django.urls import path
from .views import ScrapeHotelsView,getAllHotels

urlpatterns = [
    path('scrape/', ScrapeHotelsView.as_view(), name='scrape_hotels'),
    path('getHotels/', getAllHotels),
]
