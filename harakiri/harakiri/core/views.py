from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from harakiri.core.aws import AWS_REGIONS


class ConfigsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kw):
        return Response({"AWS_REGIONS": AWS_REGIONS})
