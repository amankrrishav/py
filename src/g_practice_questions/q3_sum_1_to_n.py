# Problem: Ask for a number and print the sum from 1 to num

n = int(input("Enter a num: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum from 1 to {n}: {total}")
