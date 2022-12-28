from rest_framework.permissions import IsAuthenticated

from harakiri.core.permissions import IsObjectOwner
from harakiri.core.viewsets import ModelViewSetWithoutDestroy
from harakiri.sources.models import Source
from harakiri.sources.serializers import SourceSerializer


class SourceViewSet(ModelViewSetWithoutDestroy):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user.id)
