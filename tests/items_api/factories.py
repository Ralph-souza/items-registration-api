import uuid

from factory.django import DjangoModelFactory
from django.utils import timezone

from apps.items_api.models import ItemModel, VideoItemModel, PrintedItemModel


class ItemFactory(DjangoModelFactory):
    item = int
    item_type = "video"
    video_item = ""
    printed_item = ""
    owner = str(uuid.uuid4())
    owner_name = "Some owner name"
    created_at = timezone.now()

    class Meta:
        model = ItemModel


class VideoItemFactory(DjangoModelFactory):
    video_item = int
    video_item_title = "Some title"
    video_media_type = "movies"
    video_media_format = "dvd"
    main_actor = "Some actor"
    status = "not_loaned"
    created_at = timezone.now()

    class Meta:
        model = VideoItemModel


class PrintedItemFactory(DjangoModelFactory):
    printed_item = int
    printed_item_title = "Some title"
    printed_media_type = "movies"
    printed_media_format = "dvd"
    author = "Some author"
    status = "not_loaned"
    created_at = timezone.now()

    class Meta:
        model = PrintedItemModel
