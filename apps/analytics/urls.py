# urls.py
from django.urls import path
from .views import (TopSearchedRoutesView, TopUsersView, SearchTimeAnalysisView, UserBehaviorAnalyticsView,
                    TopSearchedCategories, AnalyticsDataView)

app_name = 'analytics'


urlpatterns = [
    path('top-searched-routes/', TopSearchedRoutesView.as_view(), name='top-searched-routes'),
    path('top-users/', TopUsersView.as_view(), name='top-users'),
    path('search-time-analysis/', SearchTimeAnalysisView.as_view(), name='search-time-analysis'),
    path('user-behavior-analytics/', UserBehaviorAnalyticsView.as_view(), name='user-behavior-analytics'),
    path('top-searched-categories/', TopSearchedCategories.as_view(), name='top-searched-categories'),
    path('analytics-data/', AnalyticsDataView.as_view(), name='analytics-data'),
]
