from django.urls import path, include

from apps.search import views as search_views

app_name = 'search'

"""
Search URLs
"""

urlpatterns = [
    path("", search_views.SearchAPIView.as_view(), name="user-search"),
]
