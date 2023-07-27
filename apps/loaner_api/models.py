import uuid

from django.db import models

from apps.user_api.models import UserModel
from apps.items_api.models import (GamesItemModel, PrintedItemModel,
                                   VideosItemModel)

from apps.loaner_api.choices import LoanerGenderChoices


class LoanerModel(models.Model):
    loaner = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    loaner_name = models.CharField(max_length=250, null=False)
    loaner_birthday = models.DateField(blank=False, null=False)
    loaner_gender = models.CharField(
        choices=LoanerGenderChoices.choices,
        max_length=6,
        blank=False,
        null=False
    )
    loaner_email = models.EmailField()
    loaner_phone = models.CharField(max_length=18, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = "Loaner"
        verbose_name_plural = "Loaners"
        ordering = ("created_at",)

    def __str__(self):
        return self.loaner_name


class ItemsLoanedModel(models.Model):
    owner = models.ForeignKey(
        "user_api.UserModel",
        related_name="user_relation",
        on_delete=models.CASCADE
    )
    loaner = models.ForeignKey(
        "loaner_api.LoanerModel",
        related_name="loaner_relation",
        on_delete=models.CASCADE
    )
    game_item = models.ForeignKey(
        "items_api.GamesItemModel",
        related_name="games_relation",
        on_delete=models.CASCADE
    )
    printed_item = models.ForeignKey(
        "items_api.PrintedItemModel",
        related_name="printed_relation",
        on_delete=models.CASCADE
    )
    video_item = models.ForeignKey(
        "items_api.VideosItemModel",
        related_name="video_relation",
        on_delete=models.CASCADE
    )
    since = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Item loaned"
        verbose_name_plural = "Items loaned"


class LoanHistory(models.Model):
    loaner = models.ForeignKey(
        "loaner_api.LoanerModel",
        related_name="loaner_names",
        on_delete=models.CASCADE
    )
    game_item = models.ForeignKey(
        "items_api.GamesItemModel",
        related_name="games_names",
        on_delete=models.CASCADE
    )
    printed_item = models.ForeignKey(
        "items_api.PrintedItemModel",
        related_name="printed_names",
        on_delete=models.CASCADE
    )
    video_item = models.ForeignKey(
        "items_api.VideosItemModel",
        related_name="videos_names",
        on_delete=models.CASCADE
    )
    returned_at = models.DateTimeField()
