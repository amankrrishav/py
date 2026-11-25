# Object Identity, Memory References & Mutability in Python
# In Python, variables are LABELS pointing to objects in memory (not memory boxes like in C++).

# 1. The id() Function: Memory Address of an Object
a = 1000
b = 1000

print("--- Object Identity with id() ---")
print("id(a):", id(a))
print("id(b):", id(b))

# 2. 'is' vs '==' (Identity vs Equality)
# '==' checks if VALUES are equal
# 'is' checks if both variables point to the EXACT SAME OBJECT in memory
print("\na == b (value comparison)   :", a == b)  # True
print("a is b (memory identity check):", a is b)  # False (different objects in memory)

# 3. Small Integer Caching / Interning
# Python pre-allocates and caches small integers from -5 to 256 for performance.
# Any variable assigned in this range points to the SAME memory address!
x = 250
y = 250
print("\n--- Small Integer Interning (-5 to 256) ---")
print("id(x) == id(y) for 250:", id(x) == id(y))  # True!
print("x is y for 250        :", x is y)          # True!

# 4. Immutable vs Mutable Variables
print("\n--- Mutability Concept ---")
# Integers, floats, strings, and tuples are IMMUTABLE.
# Modifying them actually creates a NEW object with a new id!
val = 10
print("Original val id:", id(val))
val += 1
print("After val += 1 id:", id(val))  # Different memory address!

# Lists and dictionaries are MUTABLE.
# Modifying them alters the object in-place (id remains the same):
my_list = [1, 2, 3]
print("\nOriginal list id:", id(my_list))
my_list.append(4)
print("After append id :", id(my_list))  # Exact same memory address!
