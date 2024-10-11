import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_logging_signal_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal handler executed in thread: {current_thread}")
