from django.apps import AppConfig


class VolontuloAppConfig(AppConfig):
    name = 'apps.volontulo'

    def ready(self):
        from . import signals
