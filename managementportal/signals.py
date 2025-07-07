# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import AspirantStudent
from .tasks import send_reminder

@receiver(post_save, sender=AspirantStudent)
def schedule_reminder(sender, instance, created, **kwargs):
    if created:
        send_reminder.apply_async((instance.id,), countdown=120)
        # countdown = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
        # send_reminder.apply_async((instance.id,), countdown=7 * 24 * 60 * 60)
        # countdown the commented is 7days
