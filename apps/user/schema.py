from drf_yasg import openapi

email_login_resp = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 200,
    "data": {
        "message": "User Logged In Successfully!",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMTc3OTI2LCJqdGkiOiIyMWIzNDU2NDg3NzA0N2NkOGU3NjEwMTkwOTZlM2Q3ZSIsInVzZXJfaWQiOiI0YTQ2MjdlNi1mYTg3LTQwMGYtOTUwNi0xODI0NWQ1MjRlMWMifQ.APLIhA0EeZO9cguqkkZQkGrc3LS8A52AkB7bq0_Y90k",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MDI2NDMyNiwianRpIjoiNzlhNDY3MDNhOWMzNGFiOGFmNDU4Y2IxZmZlYjZjZWEiLCJ1c2VyX2lkIjoiNGE0NjI3ZTYtZmE4Ny00MDBmLTk1MDYtMTgyNDVkNTI0ZTFjIn0.DucXsC5dlSKGMp6jPzOqqdWNfG4TOcrCgdWyFdI9HWk"
    }
}}
                                    )

reset_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'verification_code': openapi.Schema(type=openapi.TYPE_STRING, description='verification_code'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='New Password'),
        'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Confirm Password'),
    })

reset_password_ex_resp = openapi.Response(description="Reset password", examples={
    "application/json": {
        "success": True,
        "code": 200,
        "data": {
            "message": "Password Set"
        }
    }
}
                                          )

facebook_login = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'auth_token': openapi.Schema(type=openapi.TYPE_STRING, description='Auth Token'),
        'unique_key': openapi.Schema(type=openapi.TYPE_STRING, description='Unique Key From FB'),
        'profile_picture': openapi.Schema(type=openapi.TYPE_STRING, description='Profile Pic URL'),
    }
)

social_login_resp = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 200,
    "data": {
        "message": "You've Logged In Successfully",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMjU3MzQxLCJqdGkiOiIyYWE3ZjkwOWIwNTg0NzIwOGRlZDkxNTQ5N2RhYjE5MyIsInVzZXJfaWQiOiJhYjg1YmE5MC1hMDZhLTQ0MGYtYmVhZC1hNGY2NzMzZDY3NTMifQ.6TQhn5lFNsef5JHjY0JYO6-wwAqkG653nebxAx23VHE",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MDM0Mzc0MSwianRpIjoiNTQ3ZDdhYmQ2NmY5NDliNGI4ZmQzMDhkOTI2YWI0YjIiLCJ1c2VyX2lkIjoiYWI4NWJhOTAtYTA2YS00NDBmLWJlYWQtYTRmNjczM2Q2NzUzIn0.9MrYb6XzrDM4spoBk29G-LNwZemP5H_2AEmictYMqBo"
    }
}}
                                     )

forgot_password_resp = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 200,
    "data": {
        "message": "The Verification code sent successfully!"
    }
}}
                                        )

logout_resp = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 200,
    "data": {
        "message": "You're logged out."
    }
}}
                               )

media_response = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 201,
    "data": {
        "id": "c8debcd8-a313-482c-911f-4809ffa28fc5",
        "created_at": "2023-03-30T10:17:20.635459Z",
        "media_type": "IMAGE",
        "message": "SUCCESS",
        "media_url": None
    }
}}
                                  )

email_signup_response = openapi.Response(description="Success", examples={"application/json": {
    "success": True,
    "code": 201,
    "data": {
        "message": "Account Created Successfully",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMjczNTgxLCJpYXQiOjE2ODAxODcxODEsImp0aSI6IjI3MjcwYjJmMmMzMjQxMmI5Mzc1MDc3ZTkwNmMyMzViIiwidXNlcl9pZCI6IjE0MmQ2NzVmLWViNzYtNDY3Ny1hMWM1LTljMjhiZjljNmRjMCJ9.BZ_5OO9OPEIJM2vkFxASCEe44QW_cWy_qwd2oqYWkow",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MDM1OTk4MSwiaWF0IjoxNjgwMTg3MTgxLCJqdGkiOiJlY2NkODNkZDUwMjU0YzYzYjA5MTNjYzI4M2I3ZmI0ZSIsInVzZXJfaWQiOiIxNDJkNjc1Zi1lYjc2LTQ2NzctYTFjNS05YzI4YmY5YzZkYzAifQ.Ig6_6rZUc71FikC9ss58YJsKZ8h6d7m_tI3n5Y6EsKU"
    }
}, "application/json": {
    "success": True,
    "code": 201,
    "data": {
        "message": "Account Created Successfully",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMjczNTgxLCJpYXQiOjE2ODAxODcxODEsImp0aSI6IjI3MjcwYjJmMmMzMjQxMmI5Mzc1MDc3ZTkwNmMyMzViIiwidXNlcl9pZCI6IjE0MmQ2NzVmLWViNzYtNDY3Ny1hMWM1LTljMjhiZjljNmRjMCJ9.BZ_5OO9OPEIJM2vkFxASCEe44QW_cWy_qwd2oqYWkow",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MDM1OTk4MSwiaWF0IjoxNjgwMTg3MTgxLCJqdGkiOiJlY2NkODNkZDUwMjU0YzYzYjA5MTNjYzI4M2I3ZmI0ZSIsInVzZXJfaWQiOiIxNDJkNjc1Zi1lYjc2LTQ2NzctYTFjNS05YzI4YmY5YzZkYzAifQ.Ig6_6rZUc71FikC9ss58YJsKZ8h6d7m_tI3n5Y6EsKU"
    }
}}
                                         )

apple_login = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "user": openapi.Schema(type=openapi.TYPE_STRING, description='unique_key'),
        "email": openapi.Schema(type=openapi.TYPE_STRING, description='emil'),
        'profile_picture': openapi.Schema(type=openapi.TYPE_STRING, description='Profile Pic URL'),
        "fullName": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "namePrefix": openapi.Schema(type=openapi.TYPE_STRING, description='first_name'),
                "givenName": openapi.Schema(type=openapi.TYPE_STRING, description='given_name'),
                "familyName": openapi.Schema(type=openapi.TYPE_STRING, description='family_name'),
                "nickname": openapi.Schema(type=openapi.TYPE_STRING, description='nick_name'),
                "middleName": openapi.Schema(type=openapi.TYPE_STRING, description='middle_name'),
                "nameSuffix": openapi.Schema(type=openapi.TYPE_STRING, description='name_suffix')
            }
        ),
    }
)
