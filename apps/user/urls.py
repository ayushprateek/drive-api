from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user import views as user_views

app_name = 'user'

"""
Login level URLs
"""
urlpatterns = [
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path("signup/", user_views.UserSignUpAPIView.as_view(), name="user-signup"),
    path("login/", user_views.UserEmailLoginAPIView.as_view(), name="user-email-login"),
    path("profile/", user_views.UserProfileAPIView.as_view(), name="user-email-login"),
    path("google-login/", user_views.GoogleSocialLoginView.as_view(), name="google-login"),
    path('facebook-login/', user_views.FacebookSocialLoginView.as_view(), name="facebook"),
    path('apple-login/', user_views.AppleLoginView.as_view(), name="apple-login"),
    path("media/", user_views.MediaAPIView.as_view(), name="media-post"),
    path('forgot-password/', user_views.ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path('reset-password/', user_views.ResetPasswordAPIView.as_view(), name="reset-password"),
    path("logout/", user_views.UserLogoutAPIView.as_view(), name="user-logout"),
]
