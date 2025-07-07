from django.apps import AppConfig


class ManagementportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'managementportal'

    def ready(self):
        import managementportal.signals
