# Function Scope in Python: Local vs Global Variables
# Python follows the LEGB Rule to resolve variable names:
# L: Local      (Inside the current function)
# E: Enclosing  (Inside enclosing/nested functions)
# G: Global     (At the module/script level)
# B: Built-in   (Python's built-in namespace: print, len, range, etc.)

# 1. Global Variable: Defined outside any function
x = "I am Global"

def test_scope():
    # 2. Local Variable: Defined inside a function
    # Only accessible inside this function!
    y = "I am Local"
    print("Inside test_scope():")
    print("  Local  y =", y)
    print("  Global x =", x)  # Can read global variable directly

test_scope()

print("\nOutside test_scope():")
print("  Global x =", x)

# Trying to access 'y' outside will raise NameError:
# print(y)  # NameError: name 'y' is not defined


# 3. Variable Shadowing (Local variable hides Global variable with the same name)
count = 10  # Global count

def shadow_demo():
    count = 99  # Local count — shadows the global one
    print("\nInside shadow_demo(): count =", count)  # Prints 99

shadow_demo()
print("Outside shadow_demo(): count =", count)  # Still 10! Global remains unchanged.


# 4. Enclosing Scope (Nested Functions)
def outer_function():
    msg = "Hello from Outer"  # Enclosing scope variable

    def inner_function():
        # Searches: Local -> Enclosing -> Global -> Built-in
        print("\nInside inner_function():", msg)

    inner_function()

outer_function()
