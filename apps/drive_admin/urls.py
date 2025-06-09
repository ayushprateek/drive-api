from django.urls import path
from apps.trip import views as trip_views
from .views import *

app_name = 'drive_admin'

urlpatterns = [
    path('check/', checkAdminAPI, name='check-api'),
    path('register/', AdminRegisterView.as_view()),
     path('login/', AdminLoginAPIView.as_view(), name='user_token_obtain_pair'),
    # path('secure/', SomeDriveAdminView.as_view()),
    
    path('add-city/', addCity, name='add city'),
    path('update-city/<city_id>', updateCity),
    path('get-city/<city_id>', getCity),
    path('get-all-cities/', getAllCities),
    path('delete-city/<city_id>', deleteCity),
    path('add-category/', addCategory),
    path('get-category/<category_id>', getCategory),
    path('get-all-categories/', getAllCategories),
    path('update-category/<category_id>', updateCategory),
    path('delete-category/<category_id>', deleteCategory),
]
