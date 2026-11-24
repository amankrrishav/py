# Prime Checker Function in Python

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

# Generating all primes between 2 and 50
print("Primes from 2 to 50:")
for i in range(2, 51):
    if is_prime(i):
        print(i, end=" ")
print()
