import random
import string
from rest_framework.exceptions import ValidationError

from apps.user.models import SocialLoginModel, User, Media
from common.constants import ApplicationMessages


def register_social_user(provider, user_data, unique_key):
    """Register/Login User From Facebook and Google"""

    email = user_data.get("email")
    if email:
        email = email.lower()
        user_login = SocialLoginModel.filter_instance(
            {"email": email, "provider": provider, "unique_key": unique_key}
        )
    else:
        user_login = SocialLoginModel.filter_instance(
            {"provider": provider, "unique_key": unique_key}
        )

    if user_login.exists():
        user = user_login.get()
        return user.user

    else:
        user = User.objects.filter(email=email)
        if user.exists():
            return user.first()
        else:
            profile_picture = user_data.pop("profile_picture")
            password = _generate_password()
            user = User.create_instance(user_data)
            user.set_password(password)
            user.save()
            if profile_picture:
                profile_picture = _sanitize_profile_picture(profile_picture)
                user.profile_pic = profile_picture
                user.save()
            data = {"email": email, "unique_key": unique_key, "provider": provider, "user": user}
            SocialLoginModel.create_instance(data)
            return user


def _generate_password():
    """generate random password"""

    result_str = "".join(random.sample(string.ascii_lowercase, 8))
    return result_str.capitalize() + "@"


def _sanitize_profile_picture(profile_pic):
    """Save Profile Picture URL To Database"""

    data = {"media_key": profile_pic, "media_type": Media.IMAGE}
    media = Media.create_instance(data=data)
    return media
