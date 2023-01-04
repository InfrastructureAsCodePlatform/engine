from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from furl import furl

from harakiri.core.models import BaseModel
from harakiri.users.models import User


class Source(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=64, null=False, blank=False)
    url = models.URLField("URL")
    branch = models.CharField("Branch", max_length=32, null=True, blank=True)
    tag = models.CharField("Tag", max_length=32, null=True, blank=True)
    path = models.CharField("Path", max_length=64, null=True, blank=True)
    token = EncryptedCharField(max_length=100, null=True, blank=True)
    description = models.TextField("Description", blank=True)
    is_active = models.BooleanField("Is Active", default=True)

    class Meta:
        app_label = "sources"
        verbose_name_plural = "Sources"
        ordering = ["-id"]

    @property
    def repository_name(self):
        return self.url.split(".git")[0].split("/")[-1] if self.url else "-"

    @property
    def repository_auth_url(self):
        if self.url and self.token:
            f = furl(self.url)
            f.username = f.pathstr.split("/")[1]
            f.password = self.token
            return f.url
        return "-"
