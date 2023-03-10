from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from harakiri.boilerplates.models import Boilerplate
from harakiri.boilerplates.serializers import BoilerplateSerializer


class BoilerplateReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Boilerplate.objects.all()
    serializer_class = BoilerplateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Boilerplate.objects.filter(is_active=True)
