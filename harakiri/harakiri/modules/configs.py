from model_utils.choices import Choices

TYPE_CHOICES = Choices(
    ("iac", "Infrastructure as Code"),
    ("ci", "Continuous integration"),
)
SUBTYPE_CHOICES = Choices(
    ("terraform", "Terraform"),
    ("terragrunt", "Terragrunt"),
    ("terraspace", "Terraspace"),
    ("gitlab_ci", "Gitlab CI"),
    ("github_actions", "Github Actions"),
)
