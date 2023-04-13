from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import GamesItemModel, ItemModel, PrintedItemModel, VideoItemModel
from .serializers import (GameItemModelSerializer, ItemModelSerializer,
                          PrintedItemModelSerializer, VideoItemModelSerializer)


class ItemsModelViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = ItemModel.objects.all().order_by("-updated_at")
    serializer_class = ItemModelSerializer


class VideoItemsModelViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = VideoItemModel.objects.all().order_by("-updated_at")
    serializer_class = VideoItemModelSerializer


class PrintedItemsModelViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = PrintedItemModel.objects.all().order_by("-updated_at")
    serializer_class = PrintedItemModelSerializer


class GameItemsModelViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = GamesItemModel.objects.all().order_by("-updated_at")
    serializer_class = GameItemModelSerializer
