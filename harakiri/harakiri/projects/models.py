from django.db import models

from harakiri.core.models import BaseModel
from harakiri.users.models import User


class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=32, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        app_label = "projects"
        verbose_name_plural = "Projects"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (project {self.id})"
