import re

from django.db import transaction
from rest_framework import serializers, status
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from rest_framework.validators import ValidationError
from apps.user import models as user_models, user_auth
from apps.user.social_login import register_social_user
from apps.user.user_auth import Google, Facebook
from drive_ai import settings
from common.constants import ApplicationMessages, Constant
from common import (
    utils,
    mail,
    cloud_service
)


class MediaSerializer(serializers.Serializer):
    """Media Serializer for POST"""

    def validate(self, attrs):
        if not (dict(attrs).keys() >= {"media_key"} or dict(attrs).keys() >= {"media_url"}):
            raise ValidationError('media file or media url required')
        if dict(attrs).keys() >= {"media_key", "media_url"}:
            raise ValidationError("only file or url can be used at once")
        return super().validate(attrs)

    TYPE_CHOICES = (("OTHER", "OTHER"), ("IMAGE", "IMAGE"), ("VIDEO", "VIDEO"))
    media_key = serializers.FileField(required=False)
    media_type = serializers.ChoiceField(required=True, choices=TYPE_CHOICES)
    content_type = serializers.CharField(max_length=255, required=True)
    media_url = serializers.URLField(required=False)


class MediaModelSerializer(serializers.ModelSerializer):
    """Media model serializer use for GET, PUT & PATCH"""

    class Meta:
        model = user_models.Media
        fields = ("id", "created_at", "media_type")


class GetMediaSerializer(serializers.Serializer):
    """Media Serializer for POST"""

    media_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user_models.Media
        fields = ("id", "media_url")

    def get_media_url(self, obj):
        """take id and return the s3 url"""
        return cloud_service.convert_image_id_to_s3_signed_url(self.initial_data.get("id"))

class SendEmailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    

    def create(self, data):
        """create and mail the token to the user"""
        print('SendEmailOTPSerializer called',data)
        print("Email = ",data.get("email"))
        verification_code = utils.generate_verification_code(6)
        data = {
            "email": data.get("email"),
            "verification_code": verification_code,
            "expiry_time": timezone.now() + timezone.timedelta(minutes=Constant.VERIFICATION_CODE_EXPIRE_TIME),
        }
        instance = user_models.UserSignupVerification.create_signup_verification(data)
        mail.SignupOTP(
                {
                    "verification_code": instance.verification_code,
                    "email": instance.email
                }
            )
        # if data:
        #     print('data exists')
        #     instance = user_models.UserVerification.create_reset_password_verification(data)
        #     mail.SignupOTP(
        #         {
        #             "verification_code": verification_code,
        #             "email": self.validated_data.get("email")
        #         }
        #     )
        # else:
        #     raise ValidationError(ApplicationMessages.BAD_REQUEST)
        
        return data
    
class UserSignUpSerializer(serializers.ModelSerializer):
    """Customer profile serializer"""
    profile_pic = serializers.PrimaryKeyRelatedField(queryset=user_models.Media.objects.all(), required=False)

    class Meta:
        model = user_models.User
        fields = (
            "email",
            "password",
            "country_code",
            "phone",
            "first_name",
            "last_name",
            "profile_pic"
        )

    def validate(self, attrs):
        """password, email, and phone validation"""

        if attrs.get('password'):
            password_regex = re.search(
                "^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$",
                attrs.get("password"),
            )
            if (
                    len(attrs.get("password")) < 8
                    or len(attrs.get("password")) > 25
                    or password_regex
            ):
                raise ValidationError(ApplicationMessages.PASSWORD_VALIDATION)

        email = attrs.get("email")
        if email and user_models.User.objects.filter(email=attrs["email"].lower()).exists():
            raise ValidationError(ApplicationMessages.USER_ALREADY_EXIST)

        return attrs

    def create(self, validated_data):
        """User Sign Up"""
        if validated_data.get('email'):
            password = validated_data.pop("password", None)
            user = user_models.User.create_instance(validated_data)

            user.set_password(password)
            user.save()
            return {
                "message": ApplicationMessages.USER_CREATED,
                "access_token": user.tokens()['access'],
                "refresh_token": user.tokens()['refresh']
            }

        else:
            raise ValidationError(ApplicationMessages.INVALID_REQUEST, status.HTTP_400_BAD_REQUEST)


class LoginSerializer(serializers.Serializer):
    """
    Login serializer
    """

    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    def validate(self, attrs):
        """will check email and password"""
        attrs["email"] = attrs.get("email").lower()
        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    """
    Take email as a parameter
    """

    email = serializers.EmailField(required=True)

    def validate(self, attr):
        """Validate user exists with same account or not"""

        attr["email"] = attr.get("email").lower()
        user = user_models.User.get_instance({"email": attr.get("email")})
        if user.is_active:
            return attr
        else:
            raise ValidationError(ApplicationMessages.USER_NOT_EXISTS)

    def create(self, validated_data):
        """create and mail the token to the user"""

        user = user_models.User.get_instance({"email": validated_data.get("email")})
        verification_code = utils.generate_verification_code(6)
        data = {
            "user": user,
            "verification_code": verification_code,
            "expiry_time": timezone.now() + timezone.timedelta(minutes=Constant.VERIFICATION_CODE_EXPIRE_TIME),
        }
        if data:
            instance = user_models.UserVerification.create_reset_password_verification(data)
            mail.ResetPasswordMail(
                {
                    "verification_code": verification_code,
                    "user": instance.user.first_name,
                    "email": instance.user.email
                }
            )
        else:
            return ValidationError(ApplicationMessages.BAD_REQUEST)
        return instance


class ResetPasswordSerializer(serializers.Serializer):
    """
    Confirm Reset password after the forgot password link sent
    """

    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    verification_code = serializers.CharField(required=True)

    def validate(self, attrs):
        """
        Check if new password is not equal to retyped password
        :param attrs:
        :return:
        """
        if attrs.get('password'):
            password_regex = re.search(
                "^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$",
                attrs.get("password"),
            )
            if (
                    len(attrs.get("password")) < 8
                    or len(attrs.get("password")) > 25
                    or password_regex
            ):
                raise ValidationError(ApplicationMessages.PASSWORD_VALIDATION)
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                ApplicationMessages.CURRENT_NEW_PASSWORD_NOT_SAME
            )
        return {
            "password": attrs["password"],
            "confirm_password": attrs["confirm_password"],
        }


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField(required=True)
    unique_key = serializers.CharField(required=True)
    profile_picture = serializers.CharField(required=True, allow_null=True)

    def create(self, validated_data):
        """Google Signup/login"""
        user_data = Google.validate(auth_token=validated_data.pop("auth_token"))
        user_data["profile_picture"] = validated_data.get("profile_picture")
        response = register_social_user(
            provider="Google",
            user_data=user_data,
            unique_key=validated_data.get("unique_key"),
        )
        return response


class FacebookSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField(required=True)
    unique_key = serializers.CharField(required=True)
    profile_picture = serializers.CharField(required=True, allow_null=True)

    def create(self, validated_data):
        """ Facebook Signup/login"""

        user_data = Facebook.validate(validated_data.pop("auth_token"))
        if user_data.pop("id", None) != validated_data.get("unique_key"):
            raise ValidationError(ApplicationMessages.USER_AUTH_FAILED)
        user_data["profile_picture"] = validated_data.get("profile_picture")
        response = register_social_user(provider="Facebook", user_data=user_data,
                                        unique_key=validated_data.get("unique_key"))
        return response


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """User profile Update serializer"""

    class Meta:
        model = user_models.User
        fields = ("email", "first_name", "last_name", "gender", "dob", "profile_pic",'meta_data')

    def update(self, instance, validated_data):
        """Update User Profile"""
        email = validated_data.get("email")
        if email and instance.email != email.lower() and email != '':
            if user_models.User.objects.filter(email=email).exists():
                raise ValidationError(ApplicationMessages.USER_ALREADY_EXIST)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class UserProfileGetSerializer(serializers.ModelSerializer):
    """User profile serializer"""
    profile_pic_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user_models.User
        exclude = ("created_at", "updated_at", "is_active", "is_admin", "password", "last_login")

    def get_profile_pic_url(self, obj):
        """take id and return the s3 url"""
        image_url = None
        if obj.profile_pic:
            s3_url = cloud_service.convert_s3_key_to_s3_signed_url(obj.profile_pic.media_key)
            return s3_url if s3_url else obj.profile_pic.media_key
        return image_url


class AppleSocialAuthSerializer(serializers.Serializer):
    unique_key = serializers.CharField(required=True)
    profile_picture = serializers.CharField(required=True, allow_null=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, allow_null=True)

    def create(self, validated_data):
        """ Apple Signup/login"""

        user_data = validated_data
        user_data["profile_picture"] = validated_data.get("profile_picture")
        response = register_social_user(provider="Apple", user_data=user_data,
                                        unique_key=validated_data.pop("unique_key"))
        return response
