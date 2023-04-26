from rest_framework import routers

from apps.user_auth.views import UserAuthModelViewSet

app_name = "user_auth"

router = routers.DefaultRouter()
router.register(r"user_auth", UserAuthModelViewSet, basename="user_auth"),

urlpatterns = router.urls
