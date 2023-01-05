from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from harakiri.core.configs import CLOUDS
from harakiri.core.models import BaseModel
from harakiri.users.models import User


class Credential(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cloud = models.CharField("Type", max_length=6, null=False, blank=False, choices=CLOUDS, default=CLOUDS.aws)
    name = models.CharField("Name", max_length=64, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)

    # aws
    aws_access_key_id = EncryptedCharField(max_length=100, null=True, blank=True)
    aws_secret_access_key = EncryptedCharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = "credentials"
        verbose_name_plural = "Credentials"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (credential {self.id})"

    @property
    def credentials(self):
        if self.cloud == CLOUDS.aws:
            return {"AWS_ACCESS_KEY_ID": self.aws_access_key_id, "AWS_SECRET_ACCESS_KEY": self.aws_secret_access_key}
        return {}
