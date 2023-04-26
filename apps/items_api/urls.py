from rest_framework import routers

from apps.items_api.views import (GameItemsModelViewSet, ItemsModelViewSet,
                                  PrintedItemsModelViewSet,
                                  VideoItemsModelViewSet)

app_name = "items_api"

router = routers.DefaultRouter()
router.register(r"video_item", VideoItemsModelViewSet, basename="video_item"),
router.register(r"printed_item", PrintedItemsModelViewSet, basename="printed_item"),
router.register(r"game_item", GameItemsModelViewSet, basename="game_item"),
router.register(r"items", ItemsModelViewSet, basename="items"),

urlpatterns = router.urls
