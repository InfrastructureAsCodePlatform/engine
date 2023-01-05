from rest_framework.permissions import IsAuthenticated

from harakiri.blades.models import Blade
from harakiri.blades.serializers import BladeSerializer
from harakiri.core.permissions import IsObjectOwner
from harakiri.core.viewsets import ModelViewSetWithoutDestroy


class BladeViewSet(ModelViewSetWithoutDestroy):
    queryset = Blade.objects.all()
    serializer_class = BladeSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

    def get_queryset(self):
        return Blade.objects.filter(user=self.request.user.id)
