from rest_framework.response import Response
from rest_framework.views import APIView


class HomeApiView(APIView):
    def get(self, request, format=None):
        return Response(
            {"none": "cleyson Lima", "idade": 26},
            status=200
        )
