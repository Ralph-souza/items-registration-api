from rest_framework import serializers

from apps.loaner_api.models import LoanerModel, ItemsLoanedModel, LoanHistory


class LoanerModelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="loaner")
    name = serializers.CharField(source="loaner_name", max_length=250)
    email = serializers.EmailField(source="loaner_email")
    phone = serializers.CharField(source="loaner_phone", max_length=20)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = LoanerModel
        read_only_fields = (
            "id",
            "name",
            "email",
            "phone",
            "created_at",
        )


class ItemsLoanedModelSerializer(serializers.ModelSerializer):
    since = serializers.DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    class Meta:
        model = ItemsLoanedModel
        fields = [
            "id",
            "since",
        ]


class LoanHistoryModelSerializer(serializers.ModelSerializer):
    returned_at = serializers.DateField(format="%d-%m-%Y", required=False)

    class Meta:
        model = LoanHistory
        fields = [
            "id",
            "returned_at",
        ]
