from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.boilerplates.models import Boilerplate
from harakiri.users.models import User

BOILERPLATE_FIELDS = ["id", "owner", "name", "description", "type", "inputs", "outputs", "is_active"]


class BoilerplateSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Boilerplate.objects.all(), required=False)
    owner = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Boilerplate
        fields = BOILERPLATE_FIELDS
