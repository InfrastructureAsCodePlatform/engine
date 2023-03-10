from harakiri.core.terragrunt import TerragruntLogs
from harakiri.deployments.tasks.ci import CI
from harakiri.deployments.tasks.iac import IaC
from harakiri.modules.models import SUBTYPE_CHOICES, TYPE_CHOICES

DEPLOYMENTS = {
    TYPE_CHOICES.iac: IaC(),
    TYPE_CHOICES.ci: CI(),
}

LOGGERS = {
    SUBTYPE_CHOICES.terragrunt: TerragruntLogs,
}
