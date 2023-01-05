from django.db import models
from model_utils import FieldTracker

from harakiri.core.models import BaseModel
from harakiri.environments.configs import ENVIRONMENTS
from harakiri.projects.models import Project
from harakiri.users.models import User


class Environment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(
        "Name", max_length=8, null=False, blank=False, choices=ENVIRONMENTS, default=ENVIRONMENTS.dev
    )
    description = models.TextField("Description", null=True, blank=True)

    tracker = FieldTracker()

    class Meta:
        app_label = "environments"
        verbose_name_plural = "Environments"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (environment {self.id})"

    def save(self, *args, **kwargs):
        new, changed = not self.id, self.tracker.changed()
        if not new:
            for field in ["name"]:
                if getattr(self, field) and field in changed:
                    setattr(self, field, changed[field])
        super().save(*args, **kwargs)
