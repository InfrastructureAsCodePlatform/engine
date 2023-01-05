from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from harakiri.core.aws import AWS_REGIONS
from harakiri.core.configs import CLOUDS


class ConfigsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kw):
        from harakiri.environments.configs import ENVIRONMENTS

        payload = {
            "AWS_REGIONS": AWS_REGIONS,
            "CLOUDS": CLOUDS,
            "ENVIRONMENTS": ENVIRONMENTS,
        }
        return Response(payload)
