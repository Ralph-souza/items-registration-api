from django.db import models

from apps.user_api.models import UserModel

from apps.items_api.choices import (GamesFormatChoices, GamesPlatformChoices, PrintedFormatChoices,
                                    PrintedTypeChoices, VideoFormatChoices,
                                    VideoTypeChoices)


class VideosItemModel(models.Model):
    video_item = models.AutoField(primary_key=True, editable=False)
    video_item_title = models.CharField(max_length=150, null=False)
    video_media_type = models.CharField(
        choices=VideoTypeChoices.choices, default=VideoTypeChoices.MOVIES, max_length=20
    )
    video_format_type = models.CharField(
        choices=VideoFormatChoices.choices,
        default=VideoFormatChoices.DVD,
        max_length=20,
    )
    main_actor = models.CharField(max_length=150, null=False)
    synopsis = models.TextField()
    released_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Video item"
        verbose_name_plural = "Video items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.video_item_title


class PrintedItemModel(models.Model):
    printed_item = models.AutoField(primary_key=True, editable=False)
    printed_item_title = models.CharField(max_length=150, null=False)
    printed_media_type = models.CharField(
        choices=PrintedTypeChoices.choices,
        default=PrintedTypeChoices.PHYSICAL,
        max_length=20,
    )
    printed_format_type = models.CharField(
        choices=PrintedFormatChoices.choices,
        default=PrintedFormatChoices.BOOK,
        max_length=20,
    )
    author = models.CharField(max_length=150, null=False)
    synopsis = models.TextField()
    edition = models.CharField(max_length=50)
    released_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Printed item"
        verbose_name_plural = "Printed items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.printed_item_title


class GamesItemModel(models.Model):
    game_item = models.AutoField(primary_key=True, editable=False)
    game_item_title = models.CharField(max_length=150, null=False)
    game_format_type = models.CharField(
        choices=GamesFormatChoices.choices,
        default=GamesFormatChoices.DIGITAL,
        max_length=20,
    )
    platform = models.CharField(
        choices=GamesPlatformChoices.choices,
        default=GamesPlatformChoices.PLAYSTATION_4,
        max_length=100
    )
    producer = models.CharField(max_length=150, null=False)
    synopsis = models.TextField()
    edition = models.CharField(max_length=250)
    released_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Game item"
        verbose_name_plural = "Games itens"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.game_item_title


class UserItemsModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video_item = models.ForeignKey(VideosItemModel, on_delete=models.CASCADE)
    printed_item = models.ForeignKey(PrintedItemModel, on_delete=models.CASCADE)
    game_item = models.ForeignKey(GamesItemModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ("-updated_at",)
