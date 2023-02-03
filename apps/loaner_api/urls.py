from rest_framework import routers

from .views import LoanerViewSet

app_name = "loaner_api"

router = routers.DefaultRouter()

urlpatterns = [
    router.register(r"loaner/", LoanerViewSet, basename="loaner"),
]
