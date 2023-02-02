from rest_framework import routers

from .views import UserViewSet

app_name = "user_api"

router = routers.DefaultRouter()

urlpatterns = [
    router.register(r"user/", UserViewSet, basename="user"),
]
