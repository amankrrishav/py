# The 'global' and 'nonlocal' Keywords in Python

# 1. Why do we need the 'global' keyword?
# By default, a function can READ a global variable.
# BUT if you try to assign/rebind a global variable inside a function,
# Python treats it as a new LOCAL variable unless explicitly told otherwise.

counter = 0  # Global variable

def increment_with_global():
    global counter  # Explicitly tell Python to modify the global variable
    counter += 1
    print("Inside increment_with_global(): counter =", counter)

print("--- Using 'global' keyword ---")
print("Before increment:", counter)
increment_with_global()
increment_with_global()
print("After increment :", counter)  # Modified globally to 2!


# 2. Creating a Global Variable from inside a function
def define_global():
    global app_name
    app_name = "Python Roadmap App"

define_global()
print("\nGlobal created inside function:", app_name)


# 3. Best Practice: Prefer Return Values over Global Mutation
# Modifying globals makes code harder to test and debug.
# It is almost always better to pass arguments and return the result:
def pure_increment(val):
    return val + 1

score = 10
score = pure_increment(score)
print("\nBetter approach (pure function): score =", score)


# 4. The 'nonlocal' Keyword (Used in Nested / Enclosing Functions)
# 'nonlocal' binds to the nearest enclosing scope (not global)
def outer_counter():
    count = 0  # Enclosing variable

    def inner_increment():
        nonlocal count  # Refers to 'count' in outer_counter()
        count += 1
        return count

    print("\n--- Using 'nonlocal' keyword ---")
    print("Inner call 1:", inner_increment())
    print("Inner call 2:", inner_increment())
    print("Count in outer after calls:", count)

outer_counter()
