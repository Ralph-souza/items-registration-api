from django.apps import AppConfig


class ItemsRegistrationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.items_registration"  # Reminder: This name should be the same as the INSTALLED_APPS in settings.py


class CoreConfig(AppConfig):
    name = "apps.items_registration"
