from rest_framework.permissions import IsAuthenticated

from harakiri.core.permissions import IsObjectOwner
from harakiri.core.viewsets import ModelViewSetWithoutDestroy
from harakiri.projects.models import Project
from harakiri.projects.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSetWithoutDestroy):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user.id)
