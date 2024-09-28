"""drive_ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from common.views import HomePageView, DashBoardAnalytics, getDeepLink
from drive_ai import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home-page'),
    path('.well-known/assetlinks.json', getDeepLink, name='home-page'),
    path('apple-app-site-association/', getDeepLink, name='home-page'),
    path('v1/analytics', DashBoardAnalytics.as_view(), name='Analytics'),
    path('user/', include('apps.user.urls')),
    path('search/', include('apps.search.urls')),
    path('trip/', include('apps.trip.urls', namespace='trip')),
    path('analytics/', include('apps.analytics.urls', namespace='analytics')),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Drive-AI API Documentation",
            default_version='v1',
            description="DRIVE AI",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@foxlabs.in"),
            license=openapi.License(name="Test License"),
        ),
        url='{scheme}://{host}'.format(scheme=settings.SCHEME, host=settings.SWAGGER_HOST),
        public=True,
        permission_classes=[AllowAny, ],
    )

    # Serve API documentation: swagger and redoc when debug mode on
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
