# Dictionary Comprehension in Python
# A concise, single-line way to create dictionaries.

# Syntax:
# {key_expression : value_expression for item in iterable}


# 1. Basic Example: Numbers and their squares (1 to 5)

# The normal for-loop way:
squares_loop = {}
for x in range(1, 6):
    squares_loop[x] = x ** 2
print("Using normal for loop:", squares_loop)

# The dict comprehension way (same thing in one line!):
squares_comp = {x: x ** 2 for x in range(1, 6)}
print("Using comprehension    :", squares_comp)


# 2. Example: Names and their length
names = ["Aman", "Rishav", "Python", "Code"]

# Creates: {'Aman': 4, 'Rishav': 6, 'Python': 6, 'Code': 4}
name_lengths = {name: len(name) for name in names}
print("\nWord lengths:", name_lengths)


# 3. With an 'if' condition (Filtering)
# Syntax: {key: value for item in iterable if condition}

# Store squares of only EVEN numbers from 1 to 10:
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print("\nEven squares (1 to 10):", even_squares)


# 4. Transforming an existing dictionary
# Convert prices from USD to INR (e.g. 1 USD = 85 INR)
prices_usd = {"apple": 2, "banana": 1, "mango": 3}

prices_inr = {fruit: price * 85 for fruit, price in prices_usd.items()}
print("\nPrices in USD:", prices_usd)
print("Prices in INR:", prices_inr)


# 5. Using if - else inside comprehension
# Syntax: {key: (value_if_true if condition else value_if_false) for ...}
scores = {"Aman": 85, "Rahul": 42, "Pooja": 90, "Simran": 35}

results = {name: ("Pass" if mark >= 50 else "Fail") for name, mark in scores.items()}
print("\nExam Results:", results)
