from django.test import TestCase

from apps.items_api.models import ItemModel, PrintedItemModel, VideoItemModel


class TestItemModel(TestCase):
    @staticmethod
    def create_item(video_item_payload):
        return ItemModel.objects.create(video_item_payload)

    def test_item_creation(self, item_payload):
        item = self.create_item(item_payload)
        self.assertTrue(isinstance(item, ItemModel))
        self.assertEqual(item.__unicode__(), item.owner_name)


class TestVideoItemModel(TestCase):
    @staticmethod
    def create_video_item(video_item_payload):
        return VideoItemModel.objects.create(video_item_payload)

    def test_video_item_creation(self, video_item_payload):
        video_item = self.create_video_item(video_item_payload)
        self.assertTrue(isinstance(video_item, VideoItemModel))
        self.assertEqual(video_item.__unicode__(), video_item.video_item_title)


class TestPrintedItemModel(TestCase):
    @staticmethod
    def create_printed_item(printed_item_payload):
        return PrintedItemModel.objects.create(printed_item_payload)

    def test_printed_item_creation(self, printed_item_payload):
        printed_item = self.create_printed_item(printed_item_payload)
        self.assertTrue(isinstance(printed_item, PrintedItemModel))
        self.assertEqual(printed_item.__unicode__(), printed_item.printed_item_title)
