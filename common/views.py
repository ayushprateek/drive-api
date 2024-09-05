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
            "package_name": "us.driveenterprises.dev.dev",
            "sha256_cert_fingerprints": [
                "49:5B:4B:94:92:6B:18:14:CA:48:58:61:BC:17:B5:C0:56:F2:AF:EC:EF:C2:50:AB:69:58:F2:17:DB:4A:80:81"
            ]
        }
    }]
    
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
