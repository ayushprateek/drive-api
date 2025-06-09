# models.py
import jwt
import datetime
from django.conf import settings
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class AdminManager(BaseUserManager):
    def create_admin(self, username, name, password=None):
        if not username:
            raise ValueError("Admins must have a username")
        admin = self.model(username=username, name=name)
        admin.set_password(password)
        admin.save(using=self._db)
        return admin


class AdminModel(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)  # Already handled securely by AbstractBaseUser
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AdminManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


    def tokens(self):
        payload = {
            'admin_id': str(self.id),
            'username': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # expires in 1 day
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return {
            'access_token': str(token),
            'refresh_token': str(token),
            'admin_id': str(self.id),
            'username': self.username
        }
    class Meta:
        db_table = 'drive_admin'
