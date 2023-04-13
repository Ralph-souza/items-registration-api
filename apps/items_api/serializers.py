from rest_framework import serializers

from .models import GamesItemModel, ItemModel, PrintedItemModel, VideoItemModel


class VideoItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="video_item", required=False)
    title = serializers.CharField(source="video_item_title")
    type = serializers.CharField(source="video_media_type")
    format = serializers.CharField(source="video_format_type")
    returned_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = VideoItemModel
        fields = [
            "id",
            "title",
            "type",
            "format",
            "main_actor",
            "released_date",
            "status",
            "returned_at",
            "created_at",
            "updated_at",
        ]


class PrintedItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="printed_item", required=False)
    title = serializers.CharField(source="printed_item_title")
    type = serializers.CharField(source="printed_media_type")
    format = serializers.CharField(source="printed_format_type")
    returned_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = PrintedItemModel
        fields = [
            "id",
            "title",
            "type",
            "format",
            "author",
            "released_date",
            "status",
            "returned_at",
            "created_at",
            "updated_at",
        ]


class GameItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="game_item", required=False)
    title = serializers.CharField(source="game_item_title")
    format = serializers.CharField(source="game_format_type")
    returned_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = GamesItemModel
        fields = [
            "id",
            "title",
            "type",
            "format",
            "producer",
            "released_date",
            "status",
            "returned_at",
            "created_at",
            "updated_at",
        ]


class ItemModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="item", required=False)
    video = VideoItemModelSerializer(source="video_item")
    printed = PrintedItemModelSerializer(source="printed_item")
    game = GameItemModelSerializer(source="game_item")
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = ItemModel
        fields = ["id", "video", "printed", "game", "created_at", "updated_at"]
