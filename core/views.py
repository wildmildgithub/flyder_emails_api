from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import *

import simplejson as JSON

class EmailsAPIView(APIView):
    authentication_classes = []
    def post(self, request, format=None):
        data = request.data.get('data')
        data = JSON.loads( data )
        for value in data:
            CrawledEmailAddress.objects.create(value=data.get('email'), source=data.get('source'))

        return Response({'valid': True})
