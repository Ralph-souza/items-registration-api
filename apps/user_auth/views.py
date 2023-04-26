from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework.viewsets import ModelViewSet

from apps.user_auth.models import UserAuthModel
from apps.user_auth.serializers import UserAuthModelSerializer


class UserAuthModelViewSet(OptimizedQuerySetMixin, ModelViewSet):
    queryset = UserAuthModel.objects.all()
    serializer_class = UserAuthModelSerializer
