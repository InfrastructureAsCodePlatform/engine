from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.environments.models import Environment
from harakiri.projects.models import Project
from harakiri.users.models import User

ENVIRONMENT_FIELDS = ["id", "user", "project", "name", "description"]


class EnvironmentSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Environment.objects.all(), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Environment
        fields = ENVIRONMENT_FIELDS
