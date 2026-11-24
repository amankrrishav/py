# Problem: Factorial of a number using loop & countdown display

n = int(input("Type a num: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"Factorial of {n}: {fact}")

print("Countdown:")
for j in range(n, 0, -1):
    print(j, end=" ")
print()
