import uuid

from django.db import models
from model_utils import FieldTracker

from harakiri.core.models import BaseModel
from harakiri.users.models import User


class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=128, null=False, blank=False)
    identifier = models.CharField("Identifier", max_length=40, editable=False, unique=True)
    description = models.TextField("Description", null=True, blank=True)

    tracker = FieldTracker()

    class Meta:
        app_label = "projects"
        verbose_name_plural = "Projects"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (project {self.id})"

    def save(self, *args, **kwargs):
        new, changed = not self.id, self.tracker.changed()
        if new and self.name:
            self.identifier = self.name.lower()[:32].replace(" ", "-") + uuid.uuid4().hex[:8].lower()
        if not new:
            for field in ["identifier"]:
                if getattr(self, field) and field in changed:
                    setattr(self, field, changed[field])
        super().save(*args, **kwargs)
