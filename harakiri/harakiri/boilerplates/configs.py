from model_utils.choices import Choices

TYPE_CHOICES = Choices(
    ("iac", "Infrastructure as Code"),
    ("ci", "Continuous integration"),
)
SUBTYPE_CHOICES = Choices(
    ("terragrunt", "Terragrunt"),
    ("gitlab_ci", "Gitlab CI"),
    ("github_actions", "Github Actions"),
)
