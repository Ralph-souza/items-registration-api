from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework.viewsets import ModelViewSet

from apps.items_api.models import (GamesItemModel, PrintedItemModel, UserItemsModel, VideosItemModel)
from apps.items_api.serializers import (
    GameItemModelSerializer,
    UserItemsModelSerializer,
    PrintedItemModelSerializer,
    VideoItemModelSerializer
)


class VideoItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    serializer_class = VideoItemModelSerializer
    queryset = VideosItemModel.objects.all().order_by("-updated_at")


class PrintedItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = PrintedItemModel.objects.all().order_by("-updated_at")
    serializer_class = PrintedItemModelSerializer


class GameItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = GamesItemModel.objects.all().order_by("-updated_at")
    serializer_class = GameItemModelSerializer


class UserItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get"]
    serializer_class = UserItemsModelSerializer
    queryset = UserItemsModel.objects.all()
