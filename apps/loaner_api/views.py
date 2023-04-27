from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework.viewsets import ModelViewSet

from apps.loaner_api.models import LoanerModel, ItemsLoanedModel, LoanHistory
from apps.loaner_api.serializers import LoanerModelSerializer, ItemsLoanedModelSerializer, LoanHistoryModelSerializer


class LoanerModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    queryset = LoanerModel.objects.all()
    serializer_class = LoanerModelSerializer


class ItemsLoanedModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get"]
    queryset = ItemsLoanedModel.objects.all()
    serializer_class = ItemsLoanedModelSerializer


class LoanHistoryModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    http_method_names = ["get"]
    queryset = LoanHistory.objects.all()
    serializer_class = LoanHistoryModelSerializer
