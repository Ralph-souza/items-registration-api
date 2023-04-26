from rest_framework import serializers

from apps.user_auth.models import UserAuthModel


class UserAuthModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthModel
        fields = [
            "auth_email",
        ]
        read_only = [
            "auth_email",
        ]
