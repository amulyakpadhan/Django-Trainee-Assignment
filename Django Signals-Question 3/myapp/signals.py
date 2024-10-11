from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def error_signal_handler(sender, instance, **kwargs):
    print("Signal handler triggered.")
    raise Exception("Signal handler error")  # Simulate an error
