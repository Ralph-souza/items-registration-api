from django.db import models
from django.utils import timezone


from .choices import (
    ITEM_TYPE_CHOICES,
    VIDEO_MEDIA_TYPE_CHOICES,
    PRINTED_MEDIA_TYPE_CHOICES,
    VIDEO_MEDIA_FORMAT_CHOICES,
    PRINTED_MEDIA_FORMAT_CHOICES,
    STATUS_CHOICES,
    RETURNED_CHOICES
)


class ItemsModel(models.Model):
    item_id = models.AutoField(primary_key=True, null=False)
    item_type = models.CharField(max_length=50, choices=ITEM_TYPE_CHOICES, default="video", null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Items"
        ordering = ("created_at",)


class VideoItemsModel(models.Model):
    video_item_id = models.AutoField(primary_key=True, editable=False)
    video_item_title = models.CharField(max_length=250, null=False)
    video_media_type = models.CharField(
        max_length=250,
        default="games",
        choices=VIDEO_MEDIA_TYPE_CHOICES,
        null=False
    )
    video_format_type = models.CharField(
        max_length=50,
        default="dvd",
        choices=VIDEO_MEDIA_FORMAT_CHOICES,
        null=False
    )
    release_date = models.DateTimeField(default=None, editable=True)
    main_actor = models.CharField(max_length=250, null=False)
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    loaned_date = models.DateTimeField(default=None, editable=True)
    returned_status = models.CharField(max_length=50, default=None, choices=RETURNED_CHOICES, blank=True, null=True)
    returned_at = models.DateTimeField(default=None, editable=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Video Items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.video_item_title


class PrintedItemsModel(models.Model):
    printed_item_id = models.AutoField(primary_key=True, editable=False)
    printed_item_title = models.CharField(max_length=250, null=False)
    printed_media_type = models.CharField(
        max_length=250, 
        default="games", 
        choices=PRINTED_MEDIA_TYPE_CHOICES, 
        null=False
    )
    printed_format_type = models.CharField(
        max_length=50, 
        default="dvd", 
        choices=PRINTED_MEDIA_FORMAT_CHOICES, 
        null=False
    )
    release_date = models.DateTimeField(default=None, editable=True)
    edition = models.CharField(max_length=10, blank=True, null=True)
    author = models.CharField(max_length=250, null=False)
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    loaned_date = models.DateTimeField(default=None, editable=True)
    returned_status = models.CharField(max_length=50, default=None, choices=RETURNED_CHOICES, blank=True, null=True)
    returned_at = models.DateTimeField(default=None, editable=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Printed Items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.printed_item_title
