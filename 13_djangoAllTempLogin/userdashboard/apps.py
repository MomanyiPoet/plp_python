from django.apps import AppConfig


class UserdashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userdashboard'

    def ready(self):
        from userdashboard import signals
