from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (GamesItemModel, PrintedItemModel, UserItemsModel,
                     VideosItemModel)
from .serializers import (GameItemModelSerializer, ItemsModelSerializer,
                          PrintedItemModelSerializer, VideoItemModelSerializer)


class VideoItemsModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    serializer_class = VideoItemModelSerializer
    queryset = VideosItemModel.objects.all().order_by("-updated_at")

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


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

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
