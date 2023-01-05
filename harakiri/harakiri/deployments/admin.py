from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from harakiri.core.decorators import message_user
from harakiri.deployments.mixins import DeploymentAdminMixin
from harakiri.deployments.models import Deployment, History


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin, DeploymentAdminMixin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_filter = []
    list_display = ["id", "name", "blade", "source", "boilerplate"]
    search_fields = ["name"]
    readonly_fields = ["histories_url", "created", "modified"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "blade",
                    "credential",
                    "source",
                    "boilerplate",
                    "name",
                    "description",
                    "aws_region",
                    "branch",
                    "tag",
                    "path",
                    "inputs",
                    "outputs",
                    "histories_url",
                ]
            },
        ),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    filter_horizontal = []
    actions = ["launch"]

    @message_user("Launched deployment for selected deployments")
    def launch(self, request, queryset):
        for deployment in queryset:
            deployment.launch()

    launch.short_description = "Launch deployments"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_display = ["id", "deployment", "status"]
    list_filter = ["status"]
    search_fields = ["id", "task_id"]
    readonly_fields = ["status", "attempt", "task_id", "created", "modified"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "deployment",
                    "inputs",
                    "outputs",
                    "msg",
                    "task_id",
                    "attempt",
                    "status",
                    "logs",
                ]
            },
        ),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-id"]
    filter_horizontal = []
    actions = ["relaunch"]

    def has_add_permission(self, request):
        return False

    @message_user("Relaunched selected history")
    def relaunch(self, request, queryset):
        for history in queryset:
            history.relaunch()

    relaunch.short_description = "Relaunch history"
