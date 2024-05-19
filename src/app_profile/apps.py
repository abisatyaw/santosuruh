from django.apps import AppConfig


class AppProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_profile"

    def ready(self):
        import app_profile.signals
