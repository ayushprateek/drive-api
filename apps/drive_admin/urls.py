from django.urls import path
from apps.trip import views as trip_views
from .views import *

app_name = 'drive_admin'

urlpatterns = [
    path('check/', checkAdminAPI, name='check-api'),
    path('add-city/', addCity, name='add city'),
    path('update-city/<city_id>', updateCity),
    path('delete-city/<city_id>', deleteCity),
    path('add-category/', addCategory),
    path('update-category/<category_id>', updateCategory),
    path('delete-category/<category_id>', deleteCategory),
]
