from rest_framework import routers

from .views import ItemsViewSet, VideoItemsViewSet, PrintedItemsViewSet

app_name = "items_api"

router = routers.DefaultRouter()

urlpatterns = [
    router.register(r"items/", ItemsViewSet, basename="items"),
    router.register(r"video_items/", VideoItemsViewSet, basename="video_items"),
    router.register(r"printed_items/", PrintedItemsViewSet, basename="printed_items"),
]
