from rest_framework.permissions import IsAuthenticated

from harakiri.core.permissions import IsObjectOwner
from harakiri.core.viewsets import ModelViewSetWithoutDestroy
from harakiri.environments.models import Environment
from harakiri.environments.serializers import EnvironmentSerializer


class EnvironmentViewSet(ModelViewSetWithoutDestroy):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

    def get_queryset(self):
        return Environment.objects.filter(user=self.request.user.id)
