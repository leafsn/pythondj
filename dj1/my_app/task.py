import time
from celery import task


def cel(request):
    print(" time out ")
    time.sleep(5)
    print(" abd ")