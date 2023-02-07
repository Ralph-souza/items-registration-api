from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    user_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_video_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_printed_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "user",
            "user_name",
            "user_email",
            "user_item",
            "user_video_item",
            "user_printed_item",
            "created_at",
            "updated_at"
        ]

        read_only_fields = (
            "user",
            "user_item",
            "user_video_item",
            "user_printed_item",
            "created_at",
            "updated_at"
        )
