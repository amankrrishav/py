# Problem: Print all prime numbers from 2 to 50 using nested loops

print("Prime numbers from 2 to 50:")
for i in range(2, 51):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
print()
