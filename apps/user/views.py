"""
user>views>profile
This view file has:
    - all the basic and common views for the profile
    1. Reset Password
    2. Forgot Password
    3. Logout

"""
import datetime
import uuid

from django.http import JsonResponse
from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views, parsers, generics
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user import (
    serializers as user_serializer,
    models as user_models, schema,
)
from apps.user.user_auth import get_headers, get_apple_user_data
from common import cloud_service, permissions, caches
from common.caches import USER_TOKEN
from common.constants import ApplicationMessages, Constant
from django.conf import settings
import os
from rest_framework.decorators import api_view

@api_view(['POST'])
def uploadImage(request):
    mediaId = None
    if request.method == 'POST' and bool(request.FILES['file']) == True:
        uploaded_file = request.FILES['file']
        with open(os.path.join(settings.BASE_DIR,'static', uploaded_file.name), 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        mediaObj = user_models.Media(
            media_key='',
            media_url=os.path.join('static', uploaded_file.name)
            )
        mediaObj.save()
        mediaId = mediaObj.id

    return JsonResponse({'message': 'File uploaded successfully.'})
class MediaAPIView(generics.GenericAPIView):
    """Media api view"""

    serializer_class = user_serializer.MediaSerializer
    model = user_models.Media
    media_serializer = user_serializer.MediaModelSerializer
    parser_classes = (parsers.MultiPartParser,)

    @swagger_auto_schema(responses={201: schema.media_response})
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            media_type = serializer.validated_data.get("media_type")
            content_type = serializer.validated_data.get("content_type")
            data = {"media_type": media_type}
            if serializer.validated_data.get("media_key"):
                media = serializer.validated_data.get("media_key")
                split_name = media._name.split(".")
                media._name = split_name[0] + (str(uuid.uuid4())) + "." + split_name[1]
                s3_upload = cloud_service.S3Object(media, media_type, content_type).upload()
                data["media_key"] = s3_upload
            elif serializer.validated_data.get("media_url"):
                data['media_url'] = serializer.validated_data['media_url']
            res = user_models.Media.create_instance(data)
            serializer_data = self.media_serializer(res).data
            serializer_data["message"] = "SUCCESS"
            if serializer.validated_data.get('media_key'):
                serializer_data['media_url'] = cloud_service.convert_image_id_to_s3_signed_url(serializer_data['id'])
            else:
                serializer_data['media_url'] = res.media_url
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendEmailOTP(generics.GenericAPIView):
    serializer_class = user_serializer.SendEmailOTPSerializer
    model = user_models.UserVerification
    
    @swagger_auto_schema(responses={201: 'Email sent successfully'})
    def post(self, request, *args, **kwargs):
        print('SendEmailOTP')
        data=request.data
        if user_models.User.objects.filter(email=data.get("email")).exists():
            raise ValidationError(ApplicationMessages.USER_ALREADY_EXIST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'detail': 'Email sent successfully'}, status=201)
        
        # serializer_class.create(validated_data=request.data)
        
        return Response({'OTP Sent':'Hi'}, status.HTTP_200_OK)

            
class UserSignUpAPIView(generics.GenericAPIView):
    """
    SignUp customer and Create Customer Profile (POST Request)
    """
    print('Method called')

    serializer_class = user_serializer.UserSignUpSerializer
    model = user_models.UserSignupVerification

    @swagger_auto_schema(responses={201: schema.email_signup_response})
    def post(self, request, *args, **kwargs):
        """
        create a new User
        payload For Email Signup: {"email": "example@ex.com", "password": "Admin@123"}
        """
        data=request.data
        try:
            print('OTPVerificationTemp = ',data.get("verification_code"))
            verification_instance=self.model.get_instance( {
                    "verification_code": data.get("verification_code"),
                    "is_used": False,})  
            print("CCCCC")
            # Check for code expiry
            if timezone.now() > verification_instance.expiry_time:
                verification_instance.is_used = True
                verification_instance.save()
                return Response(
                    ApplicationMessages.VERIFICATION_CODE_EXPIRED, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as ex:
            raise ValidationError(ApplicationMessages.INVALID_VERIFICATION_CODE)
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                response = serializer.save()
                print("User added",response)
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print("EX = ",ex)
            raise ValidationError(ApplicationMessages.SOMETHING_WENT_WRONG, status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.GenericAPIView):
    
    serializer_class = user_serializer.UserProfileUpdateSerializer
    permission_classes = [permissions.IsUser]

    def patch(self, request, *args, **kwargs):
        """Update User Profile"""
        try:
            user = request.user
            tempData=request.data
            mediaId = None
            # print('with_file = ',tempData['with_file'])
            # print('with_file = ',tempData['with_file']==1 is True)
            with_file = int(tempData.get('with_file', 0))
            print('with_file = ', with_file == 1) 
            if with_file==1 and 'file' in request.FILES and bool(request.FILES['file']) == True:
                uploaded_file = request.FILES['file']
                with open(os.path.join(settings.BASE_DIR,'static', uploaded_file.name), 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                mediaObj = user_models.Media(
                    media_key='',
                    media_url=os.path.join('static', uploaded_file.name)
                    )
                mediaObj.save()
                mediaId = mediaObj.id
                tempData['profile_pic']=mediaId
            print("tempData = ",tempData)
            serializer = self.serializer_class(user, data=tempData, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(ApplicationMessages.USER_PROFILE_UPDATED, status=status.HTTP_200_OK)
            else:
                print('Validation errors:')
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print('An error occurred:')
            
            raise ValidationError(ApplicationMessages.SOMETHING_WENT_WRONG)

    def get(self, request, *args, **kwargs):
        """Get User Profile"""
        try:
            user = request.user
            serializer = user_serializer.UserProfileGetSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as ex:
            raise ValidationError(ApplicationMessages.SOMETHING_WENT_WRONG)


class UserEmailLoginAPIView(generics.GenericAPIView):
    """Customer Login API with Email"""

    serializer_class = user_serializer.LoginSerializer

    @swagger_auto_schema(responses={200: schema.email_login_resp})
    def post(self, request):
        """User Login as well as create a session"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email, password = serializer.data['email'], serializer.data['password']
        user = user_models.User.get_instance_or_none({"email": email})
        if not user:
            raise ValidationError(ApplicationMessages.USER_N_EMAIL_EXISTS)
        if password and user.check_password(password):
            response = {
                "message": "User Logged In Successfully!",
                "access_token": user.tokens()['access'],
                "refresh_token": user.tokens()['refresh'],
                "user_id": user.id
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            raise ValidationError(ApplicationMessages.INVALID_PASSWORD)


class UserLogoutAPIView(views.APIView):

    permission_classes = (permissions.IsUser,)

    @swagger_auto_schema(responses={200: schema.logout_resp})
    def delete(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            refresh_token = caches.get(USER_TOKEN, user_id=str(request.user.id), token=token)
            caches.delete(USER_TOKEN, user_id=str(request.user.id), token=token)
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response("You're logged out.", status.HTTP_200_OK)
        except Exception as ex:
            ex = "You're logged out."
            return Response(f'{ex}', status.HTTP_200_OK)


class ForgotPasswordAPIView(generics.GenericAPIView):
    """
    API endpoint to initiate the password reset process for users.

    This view is responsible for generating a verification code that gets sent to the user's email address.
    The code is used in the subsequent reset password process to verify the user's identity.
    """
    throttle_classes = (AnonRateThrottle,)
    serializer_class = user_serializer.ForgotPasswordSerializer
    parser_classes = (parsers.JSONParser,)
    model = user_models.UserVerification

    @swagger_auto_schema(responses={200: schema.forgot_password_resp})
    def post(self, request, *args, **kwargs):
        """
        Handle the incoming POST request to start the password reset process.

        Validates the user's email, generates a unique verification code, and sends it to the
        user's email.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                ApplicationMessages.VERIFICATION_CODE_SENT, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(views.APIView):
    """
    API endpoint to facilitate user password resets.

    Users who have requested to reset their password through the "forgot password" flow
    are directed here to complete the process. The API view ensures that the user's identity
    is verified through a verification code before allowing a password reset.
    """

    serializer_class = user_serializer.ResetPasswordSerializer
    model = user_models.UserVerification
    parser_classes = (parsers.JSONParser,)
    user_model = user_models.User

    @swagger_auto_schema(request_body=schema.reset_password, responses={200: schema.reset_password_ex_resp})
    def patch(self, request, *args, **kwargs):
        """
        Handle the password reset process.

        Validates the verification code to ensure it's genuine and still valid, then processes the
        request to update the user's password. If any of the steps fail, appropriate error
        messages are returned in the response.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                verification_instance = self.model.get_instance(
                    {
                        "verification_code": request.data['verification_code'],
                        "is_used": False,
                    }
                )
                # Check for code expiry
                if timezone.now() > verification_instance.expiry_time:
                    verification_instance.is_used = True
                    verification_instance.save()
                    return Response(
                        ApplicationMessages.VERIFICATION_CODE_EXPIRED, status=status.HTTP_400_BAD_REQUEST
                    )

                user = self.user_model.get_instance(
                    {"email": verification_instance.user.email}
                )

                user.set_password(serializer.validated_data.get("password"))
                verification_instance.is_used = True
                verification_instance.save()
                user.save()
                return Response(
                    ApplicationMessages.PASSWORD_SET, status=status.HTTP_200_OK
                )
            except Exception as ex:
                raise ValidationError(ApplicationMessages.INVALID_VERIFICATION_CODE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleSocialLoginView(generics.GenericAPIView):
    """User google login API"""

    parser_class = (parsers.JSONParser,)
    serializer_class = user_serializer.GoogleSocialAuthSerializer

    @swagger_auto_schema(responses={200: schema.social_login_resp})
    def post(self, request):
        """
        User Google Login/Signup API by using "Auth_token", "unique_key"
        """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                response = {
                    "message": "You've Logged In Successfully",
                    "access_token": user.tokens()['access'],
                    "refresh_token": user.tokens()['refresh']
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise ValidationError(ApplicationMessages.SOMETHING_WENT_WRONG)


class FacebookSocialLoginView(views.APIView):
    """ Customer Facebook Login API"""

    parser_class = (parsers.JSONParser,)
    serializer_class = user_serializer.FacebookSocialAuthSerializer

    @swagger_auto_schema(request_body=schema.facebook_login, responses={200: schema.social_login_resp})
    def post(self, request):
        """
        POST with "Auth_token"
        Send an access token as from facebook to get user information
        """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                response = {
                    "message": "You've Logged In Successfully",
                    "access_token": user.tokens()['access'],
                    "refresh_token": user.tokens()['refresh']
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            raise ValidationError(str(ex), status.HTTP_400_BAD_REQUEST)


class AppleLoginView(views.APIView):
    """ Customer Apple Login API"""

    parser_class = (parsers.JSONParser,)
    serializer_class = user_serializer.AppleSocialAuthSerializer

    @swagger_auto_schema(request_body=schema.apple_login, responses={200: schema.social_login_resp})
    def post(self, request):
        """
        POST with "Auth_token"
        """
        try:
            full_name = request.data["fullName"]
            name = None
            if full_name.get("givenName", None):
                name = full_name["givenName"]
            if full_name.get("middleName", None):
                name += full_name["middleName"]
            if full_name.get("familyName", None):
                name += full_name["familyName"]
            request_data = {
                "unique_key": request.data.get("user"),
                "first_name": name,
                "email": get_apple_user_data(request.data["identityToken"])['email'],
                "profile_picture": request.data["profile_picture"],
            }
            serializer = self.serializer_class(data=request_data)
            if serializer.is_valid():
                user = serializer.save()
                response = {
                    "message": "You've Logged In Successfully",
                    "access_token": user.tokens()['access'],
                    "refresh_token": user.tokens()['refresh']
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            raise ValidationError(str(ex), status.HTTP_400_BAD_REQUEST)
