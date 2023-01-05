from django.contrib import admin

from harakiri.blades.models import Blade


@admin.register(Blade)
class BladeAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["id", "name"]
    search_fields = ["name", "description"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["user", "environment", "name", "description"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-id"]
    filter_horizontal = []
