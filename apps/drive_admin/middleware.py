# permissions.py

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import AdminModel

class IsAuthenticatedAdmin(BasePermission):
    def has_permission(self, request, view):
        user = JWTAuthentication().authenticate(request)
        return user and isinstance(user[0], AdminModel)
