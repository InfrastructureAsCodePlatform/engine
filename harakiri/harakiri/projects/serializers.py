from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.projects.models import Project
from harakiri.users.models import User

PROJECT_FIELDS = ["id", "name", "description", "user"]


class ProjectSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = PROJECT_FIELDS
