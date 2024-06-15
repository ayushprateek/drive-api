import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import MinValueValidator
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from common import caches
from common.caches import USER_TOKEN, ONE_DAY
from common.constants import Constant, ApplicationMessages
from drive_ai import settings


class BaseModel(models.Model):
    """
    Base Model class to add a id, created_at and updated_at field as common for all models.
    properties: id (uuid), created_at, updated_at (timestamp)
    """

    class Meta:
        abstract = True

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        print: {id}/created_date
        :return:
        """
        return "{}-{}".format(self.id, self.created_at)

    @classmethod
    def create_instance(cls, data):
        """Create Instance"""
        try:
            obj = cls.objects.create(**data)
            return obj
        except Exception as ex:
            raise ValidationError(str(ex))

    @classmethod
    def get_instance(cls, query):
        """Get Instance or Raise Error"""
        try:
            return cls.objects.get(**query)
        except Exception as err:
            raise ValidationError(str(err), status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_instance_or_none(cls, query):
        """Get Instance or Return None"""
        try:
            return cls.objects.get(**query)
        except Exception as ex:
            return None

    @classmethod
    def filter_instance(cls, query):
        """Filter Instance"""
        return cls.objects.filter(deleted_at__isnull=True, **query)


class Media(BaseModel):
    """Upload media with type (IMAGE, AUDIO, VIDEO) and return url"""

    OTHER = "OTHER"
    IMAGE = "IMAGE"

    media_types = (
        (OTHER, "OTHER"),
        (IMAGE, "IMAGE")
    )

    media_key = models.TextField(blank=True, null=True)
    media_type = models.CharField(max_length=200, choices=media_types, default="IMAGE")
    meta_data = models.JSONField(default=dict)
    media_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """return string representation"""
        return "{}".format(self.media_key)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"


# Create your models here.


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self,
            email: str,
            password: str,
            is_admin: bool,
            **extra_fields
    ):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_admin=is_admin,
            is_active=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password=None, **extra_fields):
        """Creates and saves a User with the given email and password."""
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class User(AbstractBaseUser, BaseModel):
    """The user Model for storing emails, password and permissions"""

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )

    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    country_code = models.CharField(max_length=4, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.ForeignKey(
        Media, on_delete=models.SET_NULL, blank=True, null=True
    )
    meta_data = models.JSONField(default=dict)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True, choices=GENDER_CHOICE)

    objects = MyUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email if self.email else f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        caches.set(USER_TOKEN, tokens['refresh'], ONE_DAY, user_id=str(self.id), token=tokens['access'])
        return tokens
    
class UserSignupVerification(BaseModel):
    email=models.CharField(null=True,blank=True,max_length=225)
    verification_code = models.CharField(max_length=255)
    expiry_time = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    
    @staticmethod
    def create_signup_verification(kwargs):
        """
        Creates a OTP/Token and return user obj
        """
        
        obj = UserSignupVerification(**kwargs)
        obj.save()
        return obj

class UserVerification(BaseModel):
    """
    UserVerification model is designed to store verification codes for users.
    This can be an OTP (One Time Password) or a more persistent token, depending
    on the use-case.
    """
    OTP = "OTP"
    TOKEN = "TOKEN"
    VERIFICATION_CHOICES = (
        (TOKEN, "TOKEN"),
        (OTP, "OTP"),
    )
    user = models.ForeignKey(
        User, related_name="verifications", on_delete=models.CASCADE
    )
    verification_type = models.CharField(
        max_length=100, choices=VERIFICATION_CHOICES, default=OTP
    )
    verification_code = models.CharField(max_length=255)
    expiry_time = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    def __str__(self):
        """
        String  representation of User Verification
        :return:
        """

        return f"{self.user.email} ({self.verification_code} - {self.verification_type})"

    class Meta:
        """
        Verbose name and verbose name plural
        """

        verbose_name = "UserVerification"
        verbose_name_plural = "UserVerifications"
        ordering = ["-created_at"]

    @staticmethod
    def create_reset_password_verification(kwargs):
        """
        Creates a OTP/Token and return user obj
        """

        obj = UserVerification(**kwargs)
        obj.save()
        return obj


class SocialLoginModel(BaseModel):
    PROVIDER_CHOICE = (
        ('Google', 'google'),
        ('Facebook', 'facebook'),
        ('Apple', 'apple')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="social_login_model")
    email = models.EmailField(null=True, blank=True)
    unique_key = models.CharField(max_length=128)
    provider = models.CharField(max_length=16, blank=True, null=True, choices=PROVIDER_CHOICE)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Social Login"
        verbose_name_plural = "Social Login"

    def __str__(self):
        """String representation of Social login model"""
        return "User: {}".format(self.user)


class UserPlanTripLogs(BaseModel):
    """
    Model to capture user trip planning logs and analytics data.

    Fields:
    - user: The user who performed the trip planning.
    - route_request_timestamp: The timestamp of the trip planning request.
    - origin: The starting point of the trip.
    - destination: The destination of the trip.
    - travel_time: The estimated travel time for the trip.
    - categories: A JSON string or list of categories related to the trip.

    Note: Customize the model as needed to capture additional analytics data.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route_request_timestamp = models.DateTimeField(auto_now_add=True)
    origin = models.TextField()
    destination = models.TextField()
    travel_time = models.CharField(max_length=10, null=True)
    categories = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    discount_type = models.CharField(max_length=256, blank=True, null=True)
    meta_data = models.JSONField(default=dict)
    response_time = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['-created_at']
        verbose_name = "User Trip Log"
        verbose_name_plural = "User Trip Log"

    def __str__(self):
        """
        String representation of a UserPlanTripLogs instance.
        """
        return f"User: {self.user}, Origin: {self.origin}, Destination: {self.destination}"
