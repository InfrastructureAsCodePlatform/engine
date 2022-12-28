from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from harakiri.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "first_name", "last_name", "modified"]
    list_filter = ["is_staff"]
    search_fields = ["email", "first_name", "last_name"]
    readonly_fields = [
        "created",
        "modified",
    ]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Details",
            {
                "fields": [
                    "first_name",
                    "last_name",
                ]
            },
        ),
        ("Managing", {"fields": ["is_staff"]}),
        ("Permissions", {"fields": ["is_active", "is_superuser"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    add_fieldsets = [
        (None, {"classes": ["wide"], "fields": ["email", "password1", "password2"]}),
    ]
    ordering = ["-modified"]
    filter_horizontal = []
    show_full_result_count = False


admin.site.unregister(Group)
