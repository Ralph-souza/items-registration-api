from rest_framework import routers

from .views import (
    LoanerViewSet,
)

app_name = "items_registrations"

router = routers.DefaultRouter()

router.register(r"loaner", LoanerViewSet, basename="loaner")

urlpatterns = router.urls
