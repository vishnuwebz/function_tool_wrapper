# 2 logging with wraps

from functools import wraps
import datetime

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{datetime.datetime.now()}: {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

@log
def process():
    """Process data."""
    return "Processed"


print(process())    # 2025-06-15 22:09:56.696156: process called    Processed
print(process.__name__) # process
print(process.__doc__)  # Process data.

# Log calls with preserved metadata
