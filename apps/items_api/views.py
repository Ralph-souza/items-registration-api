from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework.viewsets import ModelViewSet

from apps.items_api.models import (GamesItemModel, PrintedItemModel, UserItemsModel,
                     VideosItemModel)
from apps.items_api.serializers import (GameItemModelSerializer, ItemsModelSerializer,
                          PrintedItemModelSerializer, VideoItemModelSerializer)


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


class ItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get"]
    serializer_class = ItemsModelSerializer
    queryset = UserItemsModel.objects.all()
