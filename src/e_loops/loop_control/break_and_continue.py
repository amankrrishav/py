# Loop Control Statements: break and continue

# 1. break: Exits the loop immediately
print("--- break example (stops when i == 3) ---")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 2. continue: Skips the current iteration
print("\n--- continue example (skips when i == 3) ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
