from django.apps import AppConfig


class LoanerApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loaner_api"


class CoreConfig(AppConfig):
    name = "apps.loaner_api"
