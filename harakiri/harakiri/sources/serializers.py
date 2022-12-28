from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from harakiri.sources.models import Source
from harakiri.users.models import User

SOURCE_FIELDS = ["id", "user", "name", "url", "branch", "tag", "path", "token", "description", "is_active"]


class SourceSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Source.objects.all(), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Source
        fields = SOURCE_FIELDS
