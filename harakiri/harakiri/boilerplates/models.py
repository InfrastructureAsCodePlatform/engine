from django.db import models

from harakiri.core.configs import CLOUDS
from harakiri.core.models import BaseModel
from harakiri.modules.models import Module
from harakiri.users.models import User


class Boilerplate(BaseModel):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cloud = models.CharField("Type", max_length=6, null=False, blank=False, choices=CLOUDS, default=CLOUDS.aws)
    name = models.CharField("Name", max_length=64, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)
    is_active = models.BooleanField("Is Active", default=True)

    class Meta:
        app_label = "boilerplates"
        verbose_name_plural = "Boilerplates"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (boilerplate {self.id})"


class BoilerplateModule(BaseModel):
    boilerplate = models.ForeignKey(Boilerplate, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    step = models.IntegerField("Step", default=1)

    class Meta:
        app_label = "boilerplates"
        verbose_name_plural = "BoilerplateModules"
        unique_together = ("boilerplate", "module", "step")
        ordering = ["boilerplate"]

    def __str__(self) -> str:
        return f"{self.boilerplate}-{self.module}"
