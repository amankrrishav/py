# Constants and the NoneType in Python
from typing import Final

# 1. Constants in Python
# Unlike C++ ('const int X = 10;'), Python does not have a language-level 'const' keyword.
# Instead, Python uses a NAMING CONVENTION: all-uppercase names indicate constants.
PI = 3.14159265359
GRAVITY = 9.8
MAX_CONNECTIONS = 100
DATABASE_URL = "postgres://localhost:5432/mydb"

print("--- Constants by Convention ---")
print("PI             :", PI)
print("MAX_CONNECTIONS:", MAX_CONNECTIONS)

# Modern Python (3.8+) supports type hinting for constants using 'Final':
# Static type checkers (like mypy) will flag reassignments as errors:
APP_VERSION: Final = "1.0.0"
print("APP_VERSION    :", APP_VERSION)


# 2. The 'None' Object (NoneType)
# 'None' represents the absence of a value or null in Python (like nullptr/NULL in C++).
result = None

print("\n--- The NoneType ---")
print("Value       :", result)
print("Type of None:", type(result))  # <class 'NoneType'>

# 3. Checking for None: Always use 'is' or 'is not' (Identity check)
# Do NOT use '== None' (PEP 8 standard)
if result is None:
    print("Result has not been computed yet!")

# 4. Common Use Cases for None:
# A) Default function argument placeholder for optional parameters
def connect(timeout=None):
    if timeout is None:
        timeout = 30  # Default timeout
    return f"Connecting with timeout = {timeout}s"

print(connect())       # Uses 30s
print(connect(10))     # Uses 10s

# B) Functions that don't return an explicit value implicitly return None
def do_something():
    print("Action executed")

ret_val = do_something()
print("Implicit return of a void function:", ret_val)  # None
