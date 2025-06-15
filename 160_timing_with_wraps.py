# 4 timing with wraps

from functools import wraps
import time

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start =  time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.6f} seconds")
        return result
    return wrapper

@timing
def compute():
    """Heavy computation"""
    sum(range(1000))
    return "Done"
print(compute())    # compute took 0.000022 seconds  Done
print(compute.__name__) # compute
print(compute.__doc__)  # Heavy computation

# Times execution with preserved metadata