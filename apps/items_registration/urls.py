from rest_framework import routers

from .views import (
    UserViewSet,
    LoanerViewSet,
    ItemsViewSet,
    VideoItemsViewSet,
    PrintedItemsViewSet
)

app_name = "items_registrations"

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"loaner", LoanerViewSet, basename="loaner")
router.register(r"items", ItemsViewSet, basename="items")
router.register(r"video_items", VideoItemsViewSet, basename="video_items")
router.register(r"printed_items", PrintedItemsViewSet, basename="printed_items")

urlpatterns = router.urls
