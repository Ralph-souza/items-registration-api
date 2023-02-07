from rest_framework import serializers

from .models import ItemModel, VideoItemModel, PrintedItemModel


class ItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    video_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    printed_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    owner = serializers.UUIDField(format="hex")
    owner_name = serializers.CharField(max_length=250, allow_blank=True, allow_null=True, trim_whitespace=True)

    class Meta:
        model = ItemModel
        fields = "__all__"
        read_only_fields = (
            "item",
            "video_item",
            "printed_item",
            "owner",
            "owner_name",
            "created_at"
        )


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItemModel
        fields = "__all__"
        read_only_fields = (
            "video_item",
            "video_item_type",
            "loaner_name",
            "created_at"
        )


class PrintedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintedItemModel
        fields = "__all__"
        read_only_fields = (
            "printed_item",
            "printed_item_type",
            "loaner_name",
            "created_at"
        )
