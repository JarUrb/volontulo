"""
.. module:: signals
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create apps.volontulo.models.UserProfile object
    when django.contrib.auth.models.User object screated.
    """
    # pylint: disable=unused-argument
    if created:
        UserProfile.objects.get_or_create(user=instance)
