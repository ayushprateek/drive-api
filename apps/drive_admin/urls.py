from django.urls import path
from apps.trip import views as trip_views
from .views import *

app_name = 'drive_admin'

urlpatterns = [
    path('check/', checkAdminAPI, name='check-api'),
    path('add-city/', addCity, name='add city'),
    path('add-category/', addCategory, name='add category'),
]
