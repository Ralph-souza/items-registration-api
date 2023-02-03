from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import LoanerModel
from .serializers import LoanerSerializer


class LoanerViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "put", "delete"]
    queryset = LoanerModel.objects.all().order_by("-updated_at")
    serializer_class = LoanerSerializer
