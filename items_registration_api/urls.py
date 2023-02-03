from django.contrib import admin
from django.urls import include, re_path

from .docs import documentation_view


urlpatterns = [
    re_path(r"admin/", admin.site.urls),
    re_path(r"^v1/docs/", documentation_view.with_ui("swagger"), name="documentation"),
    re_path(r"^v1/", include("apps.user_api.urls")),
    re_path(r"^v1/", include("apps.items_api.urls")),
    re_path(r"^v1/", include("apps.loaner_api.urls")),
]
