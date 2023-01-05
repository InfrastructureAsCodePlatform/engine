from model_utils import Choices

ENVIRONMENTS = Choices(
    ("dev", "Development"),
    ("test", "Testing"),
    ("stage", "Staging"),
    ("pre_prod", "Pre-production"),
    ("prod", "Production"),
    ("live", "Live"),
)
