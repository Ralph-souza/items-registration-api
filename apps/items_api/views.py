from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework import viewsets

from .models import ItemModel, VideoItemModel, PrintedItemModel
from .serializers import ItemSerializer, VideoItemSerializer, PrintedItemSerializer


class ItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = ItemModel.objects.all().order_by("-updated_at")
    serializer_class = ItemSerializer


class VideoItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = VideoItemModel.objects.all().order_by("-updated_at")
    serializer_class = VideoItemSerializer


class PrintedItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = PrintedItemModel.objects.all().order_by("-updated_at")
    serializer_class = PrintedItemSerializer
