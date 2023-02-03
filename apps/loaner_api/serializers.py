from rest_framework import serializers

from .models import LoanerModel


class LoanerSerializer(serializers.ModelSerializer):
    loaned_videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    loaned_prints = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = (
            "loaner_id",
            "loaned_videos",
            "loaned_prints",
            "created_at",
            "updated_at"
        )
