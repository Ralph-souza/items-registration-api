from rest_framework import serializers

from .models import LoanerModel


class LoanerSerializer(serializers.ModelSerializer):
    video_items_loaned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    printed_items_loaned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = ("loaner_id", "video_items_loaned", "printed_items_loaned", "created_at")
