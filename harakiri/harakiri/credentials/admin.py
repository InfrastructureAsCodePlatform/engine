from django.contrib import admin

from harakiri.credentials.models import Credential


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_filter = ["cloud"]
    list_display = ["id", "name", "user"]
    search_fields = ["name"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "user",
                    "cloud",
                    "name",
                    "description",
                    "aws_access_key_id",
                    "aws_secret_access_key",
                ]
            },
        ),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-id"]
    filter_horizontal = []
