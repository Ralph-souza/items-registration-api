from rest_framework import routers

from .views import ItemsViewSet, VideoItemsViewSet, PrintedItemsViewSet

app_name = "items_api"

router = routers.DefaultRouter()
router.register(r"item", ItemsViewSet, basename="item"),
router.register(r"video_item", VideoItemsViewSet, basename="video_item"),
router.register(r"printed_item", PrintedItemsViewSet, basename="printed_item"),

urlpatterns = router.urls
