from rest_framework import serializers

from apps.user_api.models import UserModel

from .models import (GamesItemModel, PrintedItemModel, UserItemsModel,
                     VideosItemModel)


class UserModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user_name")
    email = serializers.EmailField(source="user_email")

    class Meta:
        model = UserModel
        fields = [
            "name",
            "email",
        ]


class VideoItemModelSerializer(serializers.ModelSerializer):
    owner = UserModelSerializer(read_only=True)
    title = serializers.CharField(source="video_item_title")
    type = serializers.CharField(source="video_media_type")
    format = serializers.CharField(source="video_format_type")
    returned_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = VideosItemModel
        fields = [
            "owner",
            "title",
            "type",
            "format",
            "main_actor",
            "release_date",
            "status",
            "returned_at",
            "created_at",
            "updated_at",
        ]

    def get_owner(self, obj: UserModel) -> str:
        owner = obj.user
        if owner:
            return UserModelSerializer(owner).data
        return None


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
            "owner",
            "returned_at",
            "created_at",
            "updated_at",
        ]


class GameItemModelSerializer(serializers.ModelSerializer):
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
            "owner",
            "returned_at",
            "created_at",
            "updated_at",
        ]


class ItemsModelSerializer(serializers.Serializer):
    owner = serializers.SerializerMethodField()
    video = VideoItemModelSerializer(source="video_item")
    video_quantity = serializers.SerializerMethodField()
    printed = PrintedItemModelSerializer(source="printed_item")
    printed_quantity = serializers.SerializerMethodField()
    game = GameItemModelSerializer(source="game_item")
    game_quantity = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = UserItemsModel
        fields = [
            "owner",
            "video",
            "video_quantity,",
            "printed",
            "printed_quatity",
            "game",
            "game_quantity",
            "created_at",
            "updated_at",
        ]

    def get_video_quantity(self, obj: VideosItemModel) -> int:
        return obj.calculate_quantity()["video"]

    def get_printed_quantity(self, obj: PrintedItemModel) -> int:
        return obj.calculate_quantity()["printed"]

    def get_game_quantity(sefl, obj: GamesItemModel) -> int:
        return obj.calculate_quantity()["game"]
