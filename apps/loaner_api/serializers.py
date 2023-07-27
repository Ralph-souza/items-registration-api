from rest_framework import serializers

from apps.loaner_api.models import LoanerModel, ItemsLoanedModel, LoanHistory


class LoanerModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="loaner", required=False)
    name = serializers.CharField(source="loaner_name", max_length=250)
    birthday = serializers.DateField(source="loaner_birthday", format="%d-%m-%Y")
    gender = serializers.CharField(source="loaner_gender")
    email = serializers.EmailField(source="loaner_email")
    phone = serializers.CharField(source="loaner_phone", max_length=20)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False, read_only=True)

    class Meta:
        model = LoanerModel
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


class ItemsLoanedModelSerializer(serializers.ModelSerializer):
    game = serializers.CharField(source="game_item")
    printed = serializers.CharField(source="printed_item")
    video = serializers.CharField(source="video_item")
    since = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = ItemsLoanedModel
        fields = [
            "id",
            "game",
            "printed",
            "video",
            "since",
        ]


class LoanHistoryModelSerializer(serializers.ModelSerializer):
    game = ItemsLoanedModelSerializer(source="game_item", many=True)
    printed = ItemsLoanedModelSerializer(source="printed_item", many=True)
    video = ItemsLoanedModelSerializer(source="video_item", many=True)
    returned_at = serializers.DateField(format="%d-%m-%Y", required=False)

    class Meta:
        model = LoanHistory
        fields = [
            "id",
            "game",
            "printed",
            "video",
            "returned_at",
        ]
