from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from harakiri.boilerplates.views import BoilerplateReadOnlyModelViewSet
from harakiri.core.views import ConfigsView
from harakiri.credentials.views import CredentialViewSet
from harakiri.deployments.views import (
    DeployApiView,
    DeploymentViewSet,
    HistoryReadOnlyModelViewSet,
)
from harakiri.projects.views import ProjectViewSet
from harakiri.sources.views import SourceViewSet

router = routers.DefaultRouter()
router.register(r"credentials", CredentialViewSet)
router.register(r"sources", SourceViewSet)
router.register(r"boilerplates", BoilerplateReadOnlyModelViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"deployments", DeploymentViewSet)
router.register(r"histories", HistoryReadOnlyModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"^healthcheck/", include("health_check.urls")),
    # our apps
    path("api/v1/", include(router.urls)),
    path("api/v1/configs/", ConfigsView.as_view(), name="configs"),
    path("api/v1/deploy/", DeployApiView.as_view(), name="deploy"),
]
