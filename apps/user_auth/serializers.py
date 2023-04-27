from rest_framework import serializers

from apps.user_auth.models import UserAuthModel


class UserAuthModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAuthModel
        fields = [
            "id",
            "auth_email",
        ]
