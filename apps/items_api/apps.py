from django.apps import AppConfig


class ItemsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.items_api'


class CoreConfig(AppConfig):
    name = "apps.items_api"
