# 3 Error Handler

from functools import wraps

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper

@error_handler
def risky():
    """Risky operation."""
    raise ValueError("Failed")

print(risky())  # Error in risky: Failed  None
print(risky.__name__)   # risky
print(risky.__doc__)    # Risky operation.

# Handles errors with preserved metadata