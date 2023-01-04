from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from model_utils import FieldTracker

from harakiri.boilerplates.models import Boilerplate
from harakiri.core.aws import AWS_REGIONS
from harakiri.core.models import STATUS, BaseModel
from harakiri.credentials.models import Credential
from harakiri.projects.models import Project
from harakiri.sources.models import Source


class Deployment(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    credential = models.ForeignKey(Credential, null=True, blank=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.SET_NULL)
    boilerplate = models.ForeignKey(Boilerplate, on_delete=models.CASCADE)

    name = models.CharField("Name", max_length=128, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)

    # aws
    aws_region = models.CharField("AWS_REGION", max_length=16, choices=AWS_REGIONS, null=True, blank=True)
    environment = models.CharField("Environment", max_length=10, null=False, blank=False)

    # source overwrite
    branch = models.CharField("Branch", max_length=32, null=True, blank=True)
    tag = models.CharField("Tag", max_length=32, null=True, blank=True)
    path = models.CharField("Path", max_length=64, null=True, blank=True)

    # boilerplate
    inputs = models.JSONField("Inputs", encoder=DjangoJSONEncoder, null=True, blank=True)
    outputs = models.JSONField("Outputs", encoder=DjangoJSONEncoder, null=True, blank=True)

    tracker = FieldTracker()

    class Meta:
        app_label = "deployments"
        verbose_name_plural = "Deployments"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} (deployment {self.id})"

    def launch(self, inputs=None):
        from harakiri.deployments.configs import DEPLOYMENTS

        return History.launch(DEPLOYMENTS[self.boilerplate.type], inputs=inputs or self.inputs, **{"deployment": self})

    def save(self, *args, **kwargs):
        new, changed = not self.id, self.tracker.changed()
        self.environment = "".join(filter(str.isalnum, self.environment)).lower()
        if not new:
            for field in ["aws_region", "environment"]:
                if getattr(self, field) and field in changed:
                    setattr(self, field, changed[field])
        super().save(*args, **kwargs)


class History(BaseModel):
    deployment = models.ForeignKey(Deployment, on_delete=models.CASCADE)
    inputs = models.JSONField("Inputs", encoder=DjangoJSONEncoder, null=True, blank=True)
    outputs = models.JSONField("Outputs", encoder=DjangoJSONEncoder, null=True, blank=True)
    msg = models.TextField("msg", null=True, blank=True)
    task_id = models.CharField("task_id", max_length=128, null=True)
    attempt = models.IntegerField("Attempt", default=0)
    status = models.CharField("Status", max_length=16, choices=STATUS, default=STATUS.pending, db_index=True)
    logs = models.TextField("Logs", null=True, blank=True)

    class Meta:
        app_label = "deployments"
        verbose_name_plural = "Histories"
        ordering = ["-id"]

    def __str__(self):
        return f"history_{self.id}"

    @classmethod
    def launch(cls, task, inputs=None, **kwargs):
        inputs = inputs or {}
        history = cls(**kwargs)
        history.inputs = inputs
        history.save()

        task_id = task.apply_async(kwargs={"history_id": history.id}).task_id
        history.task_id = task_id
        history.save(update_fields=["task_id"])
        return history
