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
            "package_name": "us.driveenterprises.app",
            "sha256_cert_fingerprints": [
                "3C:9F:1D:2B:3E:BB:39:40:5B:D2:EB:D4:76:13:49:59:A2:95:47:31:9C:CC:13:9F:E9:E6:D2:7C:83:E9:FB:FD"
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
