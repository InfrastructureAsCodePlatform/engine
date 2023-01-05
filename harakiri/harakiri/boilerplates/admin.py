from django.contrib import admin

from harakiri.boilerplates.models import Boilerplate, BoilerplateModule


class BoilerplateModuleAdmin(admin.TabularInline):
    model = BoilerplateModule
    extra = 1


@admin.register(Boilerplate)
class BoilerplateAdmin(admin.ModelAdmin):
    list_filter = ["is_active"]
    list_display = ["id", "name", "is_active"]
    search_fields = ["name", "description"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["owner", "name", "description"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-id"]
    inlines = [BoilerplateModuleAdmin]
    filter_horizontal = []
