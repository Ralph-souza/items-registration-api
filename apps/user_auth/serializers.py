from rest_framework import serializers

from apps.user_auth.models import UserAuthModel


class UserAuthModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="auth_email", required=True)

    class Meta:
        model = UserAuthModel
        fields = [
            "id",
            "email",
        ]
