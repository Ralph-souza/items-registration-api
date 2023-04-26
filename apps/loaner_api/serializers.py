from rest_framework import serializers

from .models import LoanerModel


class LoanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanerModel
        fields = "__all__"
        read_only_fields = (
            "loaner",
            "created_at",
            "updated_at",
        )
