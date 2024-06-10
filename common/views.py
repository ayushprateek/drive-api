from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.utils.translation import gettext as _
from rest_framework.response import Response

from common.constants import ApplicationMessages


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
