from django.apps import AppConfig


class UserApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_api'  # Reminder: This name should be the same as the INSTALLED_APPS in settings.py


class CoreConfig(AppConfig):
    name = "apps.user_api"
