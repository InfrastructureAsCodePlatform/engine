from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.blades.models import Blade
from harakiri.environments.models import Environment
from harakiri.users.models import User

BLADE_FIELDS = ["id", "user", "environment", "name", "description"]


class BladeSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Blade.objects.all(), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    environment = PrimaryKeyRelatedField(queryset=Environment.objects.all())

    class Meta:
        model = Blade
        fields = BLADE_FIELDS
