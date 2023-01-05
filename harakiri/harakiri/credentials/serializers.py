from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.credentials.models import Credential
from harakiri.users.models import User

CREDENTIAL_FIELDS = [
    "id",
    "user",
    "cloud",
    "name",
    "description",
    "aws_access_key_id",
    "aws_secret_access_key",
]


class CredentialSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Credential.objects.all(), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Credential
        fields = CREDENTIAL_FIELDS
