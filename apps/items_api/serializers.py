from rest_framework import serializers

from apps.items_api.models import (GamesItemModel, PrintedItemModel, UserItemsModel,
                     VideosItemModel)


class VideoItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="video_item", required=False)
    title = serializers.CharField(source="video_item_title")
    type = serializers.CharField(source="video_media_type")
    format = serializers.CharField(source="video_format_type")
    released_at = serializers.DateField(format="%d-%m-%Y", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = VideosItemModel
        fields = [
            "id",
            "title",
            "type",
            "format",
            "main_actor",
            "synopsis",
            "released_at",
            "created_at",
            "updated_at",
        ]


class PrintedItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="printed_item", required=False)
    title = serializers.CharField(source="printed_item_title")
    type = serializers.CharField(source="printed_media_type")
    format = serializers.CharField(source="printed_format_type")
    released_at = serializers.DateField(format="%d-%m-%Y", required=False)
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
            "synopsis",
            "edition",
            "released_at",
            "created_at",
            "updated_at",
        ]


class GameItemModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="game_item", required=False)
    title = serializers.CharField(source="game_item_title")
    format = serializers.CharField(source="game_format_type")
    released_at = serializers.DateField(format="%d-%m-%Y", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = GamesItemModel
        fields = [
            "id",
            "title",
            "format",
            "producer",
            "synopsis",
            "edition",
            "released_at",
            "created_at",
            "updated_at",
        ]


class ItemsModelSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = UserItemsModel
        fields = [
            "quantity",
            "created_at",
            "updated_at",
        ]
