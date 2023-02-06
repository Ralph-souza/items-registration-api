from rest_framework import serializers

from .models import ItemsModel, VideoItemsModel, PrintedItemsModel


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
            "owner_id",
            "owner_name",
            "created_at"
        )


class VideoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItemsModel
        fields = "__all__"
        read_only_fields = (
            "video_item_id",
            "video_item_type",
            "loaner_name",
            "created_at"
        )


class PrintedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintedItemsModel
        fields = "__all__"
        read_only_fields = (
            "printed_item_id",
            "printed_item_type",
            "loaner_name",
            "created_at"
        )
