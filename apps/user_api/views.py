from drf_jsonmask.views import OptimizedQuerySetMixin

from rest_framework.viewsets import ModelViewSet

from apps.user_api.models import UserModel
from apps.user_api.serializers import UserModelSerializer

class UserModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
