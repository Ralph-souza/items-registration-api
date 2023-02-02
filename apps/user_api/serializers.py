from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    user_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_video_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_printed_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "user_id",
            "user_name",
            "user_email",
            "user_items",
            "user_video_items",
            "user_printed_items",
            "created_at",
            "updated_at"
        ]

        read_only_fields = (
            "user_id",
            "user_items",
            "user_video_items",
            "user_printed_items",
            "created_at",
            "updated_at"
        )
