from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def checkAdminAPI(request):
    return JsonResponse({
            'message': 'Running'})
