import uuid

from django.db import models

from apps.user_api.models import UserModel
from apps.items_api.models import (GamesItemModel, PrintedItemModel,
                                   VideosItemModel)


class LoanerModel(models.Model):
    loaner = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    loaner_name = models.CharField(max_length=250, null=False)
    loaner_email = models.EmailField()
    loaner_phone = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loaner"
        verbose_name_plural = "Loaners"
        ordering = ("created_at",)

    def __str__(self):
        return self.loaner_name


class ItemsLoanedModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    loaner = models.ForeignKey(LoanerModel, on_delete=models.CASCADE)
    video_item = models.ForeignKey(VideosItemModel, on_delete=models.CASCADE)
    printed_item = models.ForeignKey(PrintedItemModel, on_delete=models.CASCADE)
    game_item = models.ForeignKey(GamesItemModel, on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Item loaned"
        verbose_name_plural = "Items loaned"


class LoanHistory(models.Model):
    loaner = models.ForeignKey(LoanerModel, on_delete=models.CASCADE)
    video_item = models.ForeignKey(VideosItemModel, on_delete=models.CASCADE)
    printed_item = models.ForeignKey(PrintedItemModel, on_delete=models.CASCADE)
    game_item = models.ForeignKey(GamesItemModel, on_delete=models.CASCADE)
    returned_at = models.DateTimeField()
