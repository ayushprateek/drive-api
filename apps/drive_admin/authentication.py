# drive_admin/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import AccessToken

from common import caches
from common.caches.constants import ADMIN_TOKEN
from drive_ai import settings
from .models import AdminModel
from django.core.cache import cache
import jwt
from rest_framework.permissions import BasePermission

class AdminTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("Auth called")
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            raise exceptions.AuthenticationFailed('No Bearer Token provided')

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            admin_id = payload.get('admin_id')
            print("admin_id = ",admin_id)
            admin_user = AdminModel.objects.get(id=admin_id)
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid admin token')

        return (admin_user, None)
class IsAuthenticatedAdmin(BasePermission):
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and isinstance(user, AdminModel))