from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import BasePermission

from common import caches
from common.caches import USER_TOKEN


def verify_token_validity(request):
    """This Function is used to validate token"""
    #todo: uncomment the following
    return True
    try:
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        stored_token = caches.get(USER_TOKEN, user_id=str(request.user.id), token=token)
        if stored_token:
            return True
        else:
            raise Exception(f'Token is invalid or expired')
    except Exception as ex:
        raise AuthenticationFailed(ex, status.HTTP_401_UNAUTHORIZED)


class IsUser(BasePermission):
    """User"""

    def has_permission(self, request, view):
        return bool(
            not isinstance(request.user, AnonymousUser)
            and verify_token_validity(request)
        )


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin
