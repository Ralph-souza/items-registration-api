from rest_framework import serializers

from apps.user_api.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="user", required=False)
    name = serializers.CharField(source="user_name")
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
