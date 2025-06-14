# 1 metadata preserver

from functools import wraps

def preserver(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserver
def example():
    """Example function"""
    return "Example"

print(example())
print(example.__name__)
print(example.__doc__)

"""
Example
example
Example function
"""

# demonstrates metadata preservation

