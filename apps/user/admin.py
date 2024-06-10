from django.contrib import admin
from apps.user.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(UserVerification)
admin.site.register(Media)
admin.site.register(SocialLoginModel)
admin.site.register(UserPlanTripLogs)
