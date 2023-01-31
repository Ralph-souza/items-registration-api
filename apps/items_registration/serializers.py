from rest_framework import serializers

from .models import UserModel, LoanerModel, ItemsModel, VideoItemsModel, PrintedItemsModel


class UserSerializer(serializers.ModelSerializer):
    user_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_video_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_printed_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "user_id",
            "name",
            "email",
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


class LoanerSerializer(serializers.ModelSerializer):
    video_items_loaned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    printed_items_loaned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = ("loaner_id", "video_items_loaned", "printed_items_loaned", "created_at")


class ItemsSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    video_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    printed_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ItemsModel
        fields = "__all__"
        read_only_fields = (
            "item_id",
            "video_items",
            "printed_items",
            "created_at",
            "owner_id",
            "owner_name"
        )


class VideoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItemsModel
        fields = "__all__"
        read_only_fields = (
            "video_item_id",
            "video_item_loaner",
            "video_item_loaned_to",
            "created_at",
            "updated_at"
        )


class PrintedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintedItemsModel
        fields = "__all__"
        read_only_fields = (
            "printed_item_id",
            "printed_item_loaner",
            "printed_item_loaned_to",
            "created_at",
            "updated_at"
        )
