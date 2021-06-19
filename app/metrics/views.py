from rest_framework.views import APIView


# Create your views here.
class ChronicleView(APIView):
    """
    Chronicle with events that happened within date range
    """

    def get(self, request, *args, **kwargs):
        pass
