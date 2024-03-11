from django.apps import AppConfig


class MaintableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maintable'

    def ready(self):
        pass


