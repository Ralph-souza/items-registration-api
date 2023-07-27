from rest_framework import serializers

from apps.user_api.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="user", required=False)
    birthday = serializers.DateField(format="%d-%m-%Y")
    email = serializers.EmailField(required=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "name",
            "birthday",
            "gender",
            "email",
            "phone",
            "created_at",
            "updated_at",
        ]
