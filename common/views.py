from django.http import JsonResponse
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.utils.translation import gettext as _
from rest_framework.response import Response

from common.constants import ApplicationMessages


def getDeepLink(request):
    print('getDeepLink called')

    response_data = [{
        "relation": ["delegate_permission/common.handle_all_urls"],
        "target": {
            "namespace": "android_app",
            "package_name": "us.driveenterprises.app2",
            "sha256_cert_fingerprints": [
                "C8:4D:B3:50:CF:5D:96:31:0D:38:99:63:FF:15:4A:C4:3D:CD:52:06:B2:49:CA:BD:38:EA:D7:82:2F:24:E2:1F"
            ]
        }
    }]

    return JsonResponse(response_data, safe=False)


def getDeepLinkiOS(request):
    print('ios deep link called')
    response_data = {
        "applinks": {
            "apps": [],
            "details": [
                {
                    "appID": "B76FB65Q7F.us.driveenterprises.app",
                    "paths": [
                        "/deeplink/*"
                    ]
                }
            ]
        }
    }
    return JsonResponse(response_data, safe=False)


class HomePageView(generics.GenericAPIView):
    """Home Page View"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home_page.html'

    def get(self, request, *args, **kwargs):
        """returns the template for home page.
        :param request:
        :return:
        """
        context = {"message": _("")}
        return Response(context, template_name=self.template_name)


class DashBoardAnalytics(generics.GenericAPIView):
    """Home Page View"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/analytics_dashboard.html'

    def get(self, request, *args, **kwargs):
        """Dashboard Analytics Page.
        :param request:
        :return:
        """
        context = {"message": _("")}
        return Response(context, template_name=self.template_name)
