from django.db import models

from harakiri.core.models import BaseModel
from harakiri.environments.models import Environment
from harakiri.users.models import User


class Blade(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=128, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        app_label = "blades"
        verbose_name_plural = "Blades"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (blade {self.id})"
