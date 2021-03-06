from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, services


class ChronicleView(APIView):
    """
    Chronicle with events that happened within date range
    """

    def get(self, request, *args, **kwargs):
        unique_id = kwargs['id']
        chronicle = services.get_chronicle(unique_id)
        data = serializers.ChronicleSerializer(chronicle).data
        return Response(data=data, status=status.HTTP_200_OK)
