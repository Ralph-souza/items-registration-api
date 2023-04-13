from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserModelSerializer
