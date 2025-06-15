# 5 Access Control

from functools import wraps

def restrict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and args[0] == "admin":
            return func(*args, **kwargs)
        print(f"Access denied in {func.__name__}")
    return wrapper

@restrict
def secret(user):
    """Secret function."""
    return "Secret data"

print(secret("admin"))   # Secret data
print(secret("user"))    # Access denied in secret
print(secret.__name__)   # secret
print(secret.__doc__)    # Secret function.

# restricts access with preserved metadata