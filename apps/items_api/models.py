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
    video_items = models.ForeignKey(
        "VideoItemsModel",
        default=None,
        related_name="video_item_titles",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    printed_items = models.ForeignKey(
        "PrintedItemsModel",
        default=None,
        related_name="printed_item_titles",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    owner_id = models.ForeignKey(
        "user_api.UserModel",
        default=None,
        related_name="users_ids",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    owner_name = models.ForeignKey(
        "user_api.UserModel",
        default=None,
        related_name="users_names",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Items"
        ordering = ("-updated_at",)


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
    release_date = models.CharField(max_length=10, null=True)
    main_actor = models.CharField(max_length=250, null=False)
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    loaner_name = models.ForeignKey(
        "loaner_api.LoanerModel",
        default=None,
        related_name="video_loaner_names",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    loaned_date = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    returned_status = models.CharField(max_length=50, default=None, choices=RETURNED_CHOICES, blank=True, null=True)
    returned_at = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
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
    release_date = models.CharField(max_length=10, null=True)
    edition = models.CharField(max_length=10, blank=True, null=True)
    author = models.CharField(max_length=250, null=False)
    status = models.CharField(max_length=20, default="no", choices=STATUS_CHOICES, null=False)
    loaner_name = models.ForeignKey(
        "loaner_api.LoanerModel",
        default=None,
        related_name="printed_loaner_names",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    loaned_date = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    returned_status = models.CharField(max_length=50, default=None, choices=RETURNED_CHOICES, blank=True, null=True)
    returned_at = models.DateTimeField(
        default=None,
        editable=True,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Printed Items"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.printed_item_title
