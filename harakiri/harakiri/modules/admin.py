from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from harakiri.modules.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_filter = ["type", "subtype"]
    list_display = ["id", "name", "owner", "is_active"]
    search_fields = ["name"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "owner",
                    "name",
                    "url",
                    "branch",
                    "tag",
                    "path",
                    "token",
                    "description",
                    "type",
                    "subtype",
                    "docker_image",
                    "docker_command",
                    "docker_directory",
                    "inputs",
                    "outputs",
                    "is_active",
                ]
            },
        ),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["name"]
    filter_horizontal = []
