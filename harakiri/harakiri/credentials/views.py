from rest_framework.permissions import IsAuthenticated

from harakiri.core.permissions import IsObjectOwner
from harakiri.core.viewsets import ModelViewSetWithoutDestroy
from harakiri.credentials.models import Credential
from harakiri.credentials.serializers import CredentialSerializer


class CredentialViewSet(ModelViewSetWithoutDestroy):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

    def get_queryset(self):
        return Credential.objects.filter(user=self.request.user.id)
