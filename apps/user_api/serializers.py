from rest_framework import serializers

from .models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="user", required=False)
    user = serializers.CharField(source="user_name")
    email = serializers.EmailField(source="user_email")
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = UserModel
        fields = ["id", "user", "email", "created_at", "updated_at"]
