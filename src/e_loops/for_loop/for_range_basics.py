# for Loop with range() in Python

# 1. range(stop) - runs 0 to stop-1
print("--- range(5) ---")
for i in range(5):
    print(i, end=" ")
print()

# 2. range(start, stop)
print("\n--- range(1, 11) ---")
for i in range(1, 11):
    print(i, end=" ")
print()

# 3. range(start, stop, step)
print("\n--- range(1, 10, 2) [odd numbers] ---")
for i in range(1, 10, 2):
    print(i, end=" ")
print()
