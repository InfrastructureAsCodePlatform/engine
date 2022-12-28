from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
)
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from harakiri.core.viewsets import ModelViewSetWithoutDestroy
from harakiri.deployments.models import Deployment, History
from harakiri.deployments.serializers import DeploymentSerializer, HistorySerializer
from harakiri.projects.permissions import IsProjectOwner


class DeploymentViewSet(ModelViewSetWithoutDestroy):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_queryset(self):
        return Deployment.objects.filter(project__user=self.request.user.id).select_related("project")


class HistoryReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["task_id"]

    def get_queryset(self):
        return History.objects.filter(deployment__project__user=self.request.user.id).select_related(
            "deployment__project__user"
        )


class DeployApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if "deployment_id" not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)

        deployment = Deployment.objects.get(id=request.data.get("deployment_id"))
        if request.user.id != deployment.project.user.id:
            return Response(status=HTTP_403_FORBIDDEN)

        inputs = deployment.inputs.copy()
        for field, configuration in deployment.boilerplate.inputs.items():
            if field not in inputs:
                if configuration["value"]:
                    inputs[field] = getattr(deployment, configuration["value"])
                elif bool(configuration["required"]):
                    Response(data={"msg": f"required {field} doesn't exist."}, status=HTTP_400_BAD_REQUEST)
        history = deployment.launch(inputs=inputs)
        return Response(data={"msg": "Deployment started", "task_id": history.task_id}, status=HTTP_201_CREATED)
