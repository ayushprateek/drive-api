# permissions.py

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import AdminModel
from django.urls import resolve
from rest_framework_simplejwt.exceptions import InvalidToken
from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import AuthenticationFailed
from .authentication import AdminTokenAuthentication

EXCLUDED_PATHS = [
    '/drive-admin/login/',
    '/drive-admin/register/',
]

class DriveAdminAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info

        if path.startswith('/drive-admin/') and path not in EXCLUDED_PATHS:
            user_auth = AdminTokenAuthentication()
            try:
                user, _ = user_auth.authenticate(request)
                request.user = user
                print("request.user = ",request.user)
            except AuthenticationFailed as e:
                from django.http import JsonResponse
                return JsonResponse({'detail': str(e)}, status=401)

class IsAuthenticatedAdmin(BasePermission):
    def has_permission(self, request, view):
        return isinstance(getattr(request, "user", None), AdminModel)

    
