from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from harakiri.core.models import BaseModel
from harakiri.modules.configs import SUBTYPE_CHOICES, TYPE_CHOICES
from harakiri.users.models import User


class Module(BaseModel):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField("Name", max_length=64, null=False, blank=False)
    url = models.URLField("URL", null=True, blank=True)
    branch = models.CharField("Branch", max_length=32, null=True, blank=True)
    tag = models.CharField("Tag", max_length=32, null=True, blank=True)
    path = models.CharField("Path", max_length=64, null=True, blank=True)
    token = EncryptedCharField(max_length=100, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    type = models.CharField("Type", max_length=16, null=False, blank=False, choices=TYPE_CHOICES)
    subtype = models.CharField("SubType", max_length=16, null=False, blank=False, choices=SUBTYPE_CHOICES)
    docker_image = models.CharField("Docker Image", max_length=64, null=True, blank=True)
    docker_command = models.CharField("Docker Command", max_length=64, null=True, blank=True)
    docker_directory = models.CharField("Docker Directory", max_length=32, null=True, blank=True)
    inputs = models.JSONField("Inputs", encoder=DjangoJSONEncoder, null=True, blank=True)
    outputs = models.JSONField("Outputs", encoder=DjangoJSONEncoder, null=True, blank=True)
    is_active = models.BooleanField("Is Active", default=True)

    class Meta:
        app_label = "modules"
        verbose_name_plural = "Modules"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (module {self.id})"
