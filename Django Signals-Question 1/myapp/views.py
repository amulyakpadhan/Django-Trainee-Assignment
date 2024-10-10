from django.contrib.auth.models import User
from django.http import HttpResponse
import time

def create_user(request):
    start_time = time.time()

    # Creating a new user (this will trigger the post_save signal)
    user = User.objects.create(username='new_test_user1', password='password1234')

    end_time = time.time()

    print(f"User created and signal handled in {end_time - start_time} seconds.")

    return HttpResponse(f"User created and signal handled in {end_time - start_time} seconds.")
