from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import UserModel
from .serializers import UserSerializer


class UserViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = UserModel.objects.all().order_by("created_at")
    serializer_class = UserSerializer
