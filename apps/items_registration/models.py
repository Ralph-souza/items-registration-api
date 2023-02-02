import uuid

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
    item_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    item_type = models.CharField(max_length=50, choices=ITEM_TYPE_CHOICES, blank=False, null=False, default=None)
    video_items = models.ForeignKey(
        "VideoItemsModel",
        related_name="videos_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    printed_items = models.ForeignKey(
        "PrintedItemsModel",
        related_name="prints_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    created_at = models.DateTimeField(default=timezone.now)
    # owner_id = models.ForeignKey(related_name="user_ids", on_delete=models.CASCADE)
    # owner_name = models.ForeignKey( related_name="names", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Items"
        ordering = ("created_at",)


class VideoItemsModel(models.Model):
    video_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    video_item_title = models.CharField(max_length=250, blank=False, null=False)
    video_item_type = models.ForeignKey(ItemsModel, related_name="items_types", on_delete=models.CASCADE)
    video_media_type = models.CharField(
        max_length=250,
        choices=VIDEO_MEDIA_TYPE_CHOICES,
        blank=False,
        null=False,
        default=None
    )
    video_format_type = models.CharField(
        max_length=50,
        choices=VIDEO_MEDIA_FORMAT_CHOICES,
        blank=False,
        null=False,
        default=None
    )
    launched_at = models.DateTimeField(default=None)
    actor_name = models.CharField(max_length=250, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default="not_loaned")
    loaned_since = models.DateTimeField(default=None)
    returned = models.CharField(max_length=50, choices=RETURNED_CHOICES, default="yes")
    returned_at = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, null=True, blank=True)

    class Meta:
        verbose_name = "Video Items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.video_item_title


class PrintedItemsModel(models.Model):
    printed_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    printed_item_title = models.CharField(max_length=250, blank=False, null=False)
    printed_item_type = models.ForeignKey(ItemsModel, related_name="item_types", on_delete=models.CASCADE)
    printed_media_type = models.CharField(
        max_length=250,
        choices=PRINTED_MEDIA_TYPE_CHOICES,
        blank=False,
        null=False,
        default=None
    )
    printed_media_format = models.CharField(
        max_length=250,
        choices=PRINTED_MEDIA_FORMAT_CHOICES,
        blank=False,
        null=False,
        default=False
    )
    launched_at = models.DateTimeField(default=None)
    author_name = models.CharField(max_length=250, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default="not_loaned")
    loaned_since = models.DateTimeField(default=None)
    returned = models.CharField(max_length=50, choices=RETURNED_CHOICES, default="yes")
    returned_at = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, null=True, blank=True)

    class Meta:
        verbose_name = "Printed Items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.printed_item_title


class LoanerModel(models.Model):
    loaner_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    loaner_name = models.CharField(max_length=250, blank=False, null=False)
    loaner_email = models.EmailField(max_length=150, blank=False, null=False)
    loaner_phone = models.CharField(max_length=20, blank=False, null=False)
    video_items_loaned = models.ForeignKey(
        VideoItemsModel,
        related_name="video_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    printed_items_loaned = models.ForeignKey(
        PrintedItemsModel,
        related_name="printed_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Loaner"

    def __str__(self):
        return self.loaner_name
