import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5)  # Simulate a slow task by sleeping for 5 seconds
    print("Signal handler finished.")
