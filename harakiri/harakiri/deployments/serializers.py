from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.boilerplates.models import Boilerplate
from harakiri.credentials.models import Credential
from harakiri.deployments.models import Deployment, History
from harakiri.projects.models import Project
from harakiri.sources.models import Source

DEPLOYMENT_FIELDS = [
    "id",
    "name",
    "description",
    "aws_region",
    "environment",
    "project",
    "credential",
    "source",
    "boilerplate",
    "branch",
    "tag",
    "path",
    "inputs",
    "outputs",
]
HISTORY_FIELDS = ["id", "msg", "task_id", "attempt", "status", "deployment"]


class DeploymentSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    credential = PrimaryKeyRelatedField(queryset=Credential.objects.all(), allow_null=True, required=False)
    source = PrimaryKeyRelatedField(queryset=Source.objects.all(), allow_null=True, required=False)
    boilerplate = PrimaryKeyRelatedField(queryset=Boilerplate.objects.all())

    class Meta:
        model = Deployment
        fields = DEPLOYMENT_FIELDS


class HistorySerializer(ModelSerializer):
    deployment = PrimaryKeyRelatedField(queryset=Deployment.objects.all())

    class Meta:
        model = History
        fields = HISTORY_FIELDS
