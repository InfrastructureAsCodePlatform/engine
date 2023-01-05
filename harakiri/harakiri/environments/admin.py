from django.contrib import admin

from harakiri.environments.models import Environment


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    list_display = ["id", "name"]
    search_fields = ["name", "description"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["user", "project", "name", "description"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-id"]
    filter_horizontal = []
