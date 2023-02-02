from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets


from .models import LoanerModel, ItemsModel, VideoItemsModel, PrintedItemsModel
from .serializers import (
    LoanerSerializer,
    ItemsSerializer,
    VideoItemsSerializer,
    PrintedItemsSerializer
)


class LoanerViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = LoanerModel.objects.all().order_by("created_at")
    serializer_class = LoanerSerializer


class ItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = ItemsModel.objects.all().order_by("created_at")
    serializer_class = ItemsSerializer


class VideoItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = VideoItemsModel.objects.all().order_by("-updated_at")
    serializer_class = VideoItemsSerializer


class PrintedItemsViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = PrintedItemsModel.objects.all().order_by("-updated_at")
    serializer_class = PrintedItemsSerializer
