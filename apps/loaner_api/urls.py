from rest_framework import routers

from apps.loaner_api.views import LoanerModelViewSet, ItemsLoanedModelViewSet, LoanHistoryModelViewSet

app_name = "loaner_api"

router = routers.DefaultRouter()
router.register(r"loaner", LoanerModelViewSet, basename="loaner"),
router.register(r"loaned_items", ItemsLoanedModelViewSet, basename="loaned_items")
router.register(r"loan_history", LoanHistoryModelViewSet, basename="loan_history")

urlpatterns = router.urls
