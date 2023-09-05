from ..models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("pk", "username", "first_name", "last_name","email", "is_superuser", "is_staff")
        read_only_fields = ("pk", "is_superuser", "is_staff")
