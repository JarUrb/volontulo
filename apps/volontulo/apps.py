"""
.. module:: apps
"""

from django.apps import AppConfig


class VolontuloAppConfig(AppConfig):
    """Configuration for volontulo app."""
    name = 'apps.volontulo'

    def ready(self):
        # pylint: disable=unused-variable
        from . import signals
