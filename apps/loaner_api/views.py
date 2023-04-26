from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import LoanerModel
from .serializers import LoanerSerializer


class LoanerViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    queryset = LoanerModel.objects.all()
    serializer_class = LoanerSerializer
