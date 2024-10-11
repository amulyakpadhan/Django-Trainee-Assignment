from django.contrib.auth.models import User
from django.http import HttpResponse
import threading

def create_user(request):
    current_thread = threading.current_thread().name
    print(f"View executed in thread: {current_thread}")

    # Creating a new user, which triggers the post_save signal
    user = User.objects.create(username='new_test_user1', password='12345')

    return HttpResponse("User created.")
