from django.db import models
from django.utils import timezone

from .choices import (
    VIDEO_MEDIA_TYPE_CHOICES,
    PRINTED_MEDIA_TYPE_CHOICES,
    VIDEO_MEDIA_FORMAT_CHOICES,
    PRINTED_MEDIA_FORMAT_CHOICES,
    GAMES_MEDIA_FORMAT_CHOICES,
    STATUS_CHOICES
)


class VideoItemModel(models.Model):
    video_item = models.AutoField(primary_key=True, editable=False)
    video_item_title = models.CharField(max_length=250, null=False)
    video_media_type = models.CharField(
        max_length=250,
        default="movies",
        choices=VIDEO_MEDIA_TYPE_CHOICES,
        null=False
    )
    video_format_type = models.CharField(
        max_length=50,
        default="dvd",
        choices=VIDEO_MEDIA_FORMAT_CHOICES,
        null=False
    )
    main_actor = models.CharField(max_length=250, null=False)
    release_date = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    returned_date = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Video Item"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.video_item_title


class PrintedItemModel(models.Model):
    printed_item = models.AutoField(primary_key=True, editable=False)
    printed_item_title = models.CharField(max_length=250, null=False)
    printed_media_type = models.CharField(
        max_length=250, 
        default="physical", 
        choices=PRINTED_MEDIA_TYPE_CHOICES, 
        null=False
    )
    printed_format_type = models.CharField(
        max_length=50, 
        default="book", 
        choices=PRINTED_MEDIA_FORMAT_CHOICES, 
        null=False
    )
    author = models.CharField(max_length=250, null=False)
    release_date = models.CharField(max_length=10, null=True)    
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    returned_date = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Printed Item"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.printed_item_title
    

class GamesItemModel(models.Model):
    game_item = models.AutoField(primary_key=True, editable=False)
    game_item_title = models.CharField(max_length=250, null=False)
    game_format_type = models.CharField(
        max_length=50, 
        default="digital", 
        choices=GAMES_MEDIA_FORMAT_CHOICES, 
        null=False
    )
    producer = models.CharField(max_length=250, null=False)
    release_date = models.CharField(max_length=10, null=True)    
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    returned_date = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Game Item"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.game_item_title
    

class ItemModel(models.Model):
    item = models.AutoField(primary_key=True, editable=False)
    video_item = models.ForeignKey(VideoItemModel, default=None, editable=False,  related_name="video_items", blank=True, null=True, on_delete=models.CASCADE)
    printed_item = models.ForeignKey(PrintedItemModel, default=None, editable=False,  related_name="printed_items", blank=True, null=True, on_delete=models.CASCADE)
    game_item = models.ForeignKey(GamesItemModel, default=None, editable=False,  related_name="game_items", blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Item"
        ordering = ("-updated_at",)
