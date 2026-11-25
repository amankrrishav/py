# Variable Naming Rules & Multiple Assignment in Python
import keyword

# 1. Naming Rules in Python:
# - Must start with a letter (a-z, A-Z) or an underscore (_)
# - Cannot start with a digit (e.g. 1name is invalid)
# - Can only contain alphanumeric characters and underscores (A-z, 0-9, _)
# - Variable names are CASE-SENSITIVE ('age', 'Age', and 'AGE' are 3 different variables)
# - Cannot be a Python reserved keyword

age = 21
Age = 25
AGE = 30
print("Case sensitivity check:", age, Age, AGE)

_user_id = 101       # Leading underscore is valid (often indicates internal/private)
user_name = "aman"   # Snake_case is the standard Python convention (PEP 8)

# 2. Python Reserved Keywords
print("\n--- Python Reserved Keywords (Total:", len(keyword.kwlist), ") ---")
print(", ".join(keyword.kwlist[:12]), "...")

# 3. Multiple Assignment in a Single Line
x, y, z = 10, 20, 30
print("\nMultiple Assignment: x =", x, ", y =", y, ", z =", z)

# 4. Assigning the Same Value to Multiple Variables
a = b = c = 100
print("Chained Assignment : a =", a, ", b =", b, ", c =", c)

# 5. Pythonic Variable Swap (No temporary variable needed!)
# In C++: temp = x; x = y; y = temp;
# In Python:
first = "A"
second = "B"
print("\nBefore Swap: first =", first, ", second =", second)

first, second = second, first  # Tuple packing & unpacking under the hood
print("After Swap : first =", first, ", second =", second)

# 6. Unpacking with Asterisk (*)
numbers = [1, 2, 3, 4, 5]
head, *tail = numbers
print("\nUnpacking [1, 2, 3, 4, 5]:")
print("head:", head)  # 1
print("tail:", tail)  # [2, 3, 4, 5]
