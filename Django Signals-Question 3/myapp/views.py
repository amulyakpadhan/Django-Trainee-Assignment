from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import transaction

# def create_user(request):
#     try:
#         with transaction.atomic():
#             user = User.objects.create(username='test_user1', password='password123')
#             print("User creation attempted.")
#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}")

#     # Check if the user was actually created in the database
#     user_exists = User.objects.filter(username='test_user').exists()

#     if user_exists:
#         print("User was created despite the signal handler error.")
#         return HttpResponse("User was created despite the signal handler error.")
#     else:
#         print("User creation failed due to signal handler error, no user was created.")
#         return HttpResponse("User creation failed due to signal handler error, no user was created.")

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import transaction

def create_user(request):
    user_created = False
    error_message = ""

    try:
        with transaction.atomic():
            user = User.objects.create(username='test_user', password='password123')
            print("User creation attempted.")
            user_created = True  # Track if user creation was attempted successfully
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)

    # Check if the user was actually created in the database
    user_exists = User.objects.filter(username='test_user').exists()

    if user_exists:
        print("User was created despite the signal handler error.")
        return HttpResponse("User was created despite the signal handler error.")
    else:
        print("User creation failed due to signal handler error, no user was created.")
        return HttpResponse("User creation failed due to signal handler error, no user was created.")

