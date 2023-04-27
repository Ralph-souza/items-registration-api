from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

documentation_view = get_schema_view(
    openapi.Info(
        title="user_api",
        default_version="v1",
        description="This is the user_api`s documentation page",
        contact=openapi.Contact(email="ralph_souza@hotmail.com"),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)
