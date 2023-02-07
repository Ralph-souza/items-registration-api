from rest_framework import serializers

from .models import LoanerModel


class LoanerSerializer(serializers.ModelSerializer):
    loaned_video_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    loaned_printed_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = (
            "loaner",
            "loaned_video_item",
            "loaned_printed_item",
            "created_at",
            "updated_at"
        )
