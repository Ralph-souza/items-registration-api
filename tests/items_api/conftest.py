import pytest

from .factories import ItemFactory, VideoItemFactory, PrintedItemFactory


@pytest.fixture
def item():
    return ItemFactory()


@pytest.fixture
def video_item():
    return VideoItemFactory()


@pytest.fixture
def printed_item():
    return PrintedItemFactory()


@pytest.fixture
def item_payload():
    return {
        "item_type": "video",
        "video_items": [
            {
                "video_item_title": "Some title",
            }
        ],
        "owner": "fbbf9e4a-f241-4650-b58d-716833bd8d55",
        "owner_name": "Some owner name"
    }


@pytest.fixture
def item_invalid_payload():
    return {
        "item_type": None,
        "video_items": [
            {
                "video_item_title": "Some title",
            }
        ],
        "owner": None,
        "owner_name": "Some owner name"
    }


@pytest.fixture
def video_item_payload():
    return {
        "video_item_title": "Some title",
        "video_media_type": "movies",
        "video_media_format": "dvd",
        "main_actor": "Some actor",
        "status": "not_loaned"
    }


@pytest.fixture
def video_item_invalid_payload():
    return {
        "video_item_title": None,
        "video_media_type": None,
        "video_media_format": "dvd",
        "main_actor": "Some actor",
        "status": "not_loaned"
    }


@pytest.fixture
def printed_item_payload():
    return {
        "printed_item_title": "Some title",
        "printed_media_type": "movies",
        "printed_media_format": "dvd",
        "main_actor": "Some actor",
        "status": "not_loaned"
    }


@pytest.fixture
def printed_item_invalid_payload():
    return {
        "printed_item_title": None,
        "printed_media_type": None,
        "printed_media_format": "dvd",
        "author": "Some author",
        "status": "not_loaned"
    }
