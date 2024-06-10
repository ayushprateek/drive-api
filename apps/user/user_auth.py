from google.auth.transport import requests
from google.oauth2 import id_token
import facebook
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.backends import TokenBackend

from common.constants import ApplicationMessages


class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        try:
            google = "accounts.google.com"
            id_info = id_token.verify_oauth2_token(auth_token, requests.Request())

            # if id_info["aud"] != GOOGLE_CLIENT_ID or google != id_info["iss"]:
            #     raise ValidationError(ApplicationMessages.INVALID_AUTH_TOKEN)

            user_data = {
                "first_name": id_info.get("given_name"),
                "email": id_info.get("email"),
                "last_name": id_info.get("family_name"),
            }
            return user_data

        except Exception as ex:
            raise Exception(ApplicationMessages.INVALID_AUTH_TOKEN)


class Facebook:
    """
    Facebook class to fetch the user info and return it
    """

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the facebook GraphAPI to fetch the user info
        """
        try:
            graph = facebook.GraphAPI(access_token=auth_token)
            profile = graph.request('/me?fields=first_name,last_name,email')
            return profile
        except Exception:
            raise Exception(ApplicationMessages.INVALID_AUTH_TOKEN)


def get_headers(data):
    """Get Access and Refresh Token Headers """
    return {
        "access_token": data.get("access_token"),
        "refresh_token": data.get("refresh_token")
    }


def get_apple_user_data(identity_token):
    """
    Get Apple user data from identity token
    """
    try:
        decoded = TokenBackend(algorithm='HS256').decode(identity_token, verify=False)
        user_data = {
            "email": decoded.get("email")
        }
        return user_data
    except Exception as ex:
        raise Exception(ex)
