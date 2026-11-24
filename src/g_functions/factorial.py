# Factorial Function in Python

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Test the function
n = 5
print(f"Factorial of {n} is: {factorial(n)}")
