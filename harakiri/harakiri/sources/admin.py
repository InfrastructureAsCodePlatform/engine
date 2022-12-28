from django.contrib import admin

from harakiri.sources.models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["name", "user", "is_active"]
    search_fields = ["name"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["user", "name", "url", "branch", "tag", "path", "token", "description", "is_active"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["name"]
    filter_horizontal = []
