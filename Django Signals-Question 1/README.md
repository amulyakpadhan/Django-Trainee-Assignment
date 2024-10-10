# Topic: Django Signals

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


## Answer
By default, Django signals are executed synchronously. This means that the signal handlers (receivers) are executed as part of the main request/response cycle and block the process until they finish.

## Proving Django Signals Are Synchronous
We can prove this by introducing a delay inside the signal handler and measuring the total time taken to complete the user creation. If the signal handler were asynchronous, the total time would not include the delay from the signal handler.



## Steps to Prove:
To determine if Django signals are executed synchronously by default, we use a simple approach:

- We introduce a delay inside the signal handler using time.sleep(5). This simulates a slow-running process that takes 5 seconds to complete.
- We then measure the total time taken to create a User instance in a Django view. If the signal were asynchronous, the delay from the signal handler would not affect the total time for user creation. However, if the signal is synchronous, the total time should include the 5-second delay.
By observing the total execution time of the request, we can conclusively prove whether signals block the main execution flow (i.e., are synchronous) or allow the main flow to continue without waiting (i.e., are asynchronous).

### Signal Handler Code
The User model's post_save signal has a signal handler attached to it. The signal includes a 5-second delay using time.sleep() to simulate a slow process.
```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5)  # Simulating a slow process with a 5-second delay
    print("Signal handler finished.")
```
### View Code
The view creates a new User and calculates the time it takes to complete the process, including the signal handler's execution.
```python
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
```

### Test Output 
When accessing the /create-user/ URL, the output will clearly show that the total time taken includes the 5-second delay, proving that the signal handler is executed synchronously.

