# Logical Operators in Python: and, or, not

# 1. With Boolean Values
x = True
y = False

print("x and y:", x and y)       # False (True only if BOTH are True)
print("x or y :", x or y)        # True  (True if AT LEAST ONE is True)
print("not x  :", not x)         # False (reverses True to False)
print("not y  :", not y)         # True  (reverses False to True)

# 2. Combined with Relational Conditions
a = 20
b = 2

print("(a > 10) and (b < 5):", (a > 10) and (b < 5))  # True
print("(a > 10) and (b > 5):", (a > 10) and (b > 5))  # False
print("(a > 10) or (b > 5) :", (a > 10) or (b > 5))   # True
print("(a < 10) or (b > 5) :", (a < 10) or (b > 5))   # False
print("not (a > b)         :", not (a > b))           # False
