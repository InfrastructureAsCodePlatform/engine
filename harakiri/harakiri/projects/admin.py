from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from harakiri.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_filter = []
    list_display = ["name", "user", "description"]
    search_fields = ["name", "description"]
    readonly_fields = ["identifier", "created", "modified"]
    fieldsets = [
        (None, {"fields": ["user", "name", "identifier", "description"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["name"]
    filter_horizontal = []
