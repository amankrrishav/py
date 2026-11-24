# String Indexing in Python

text = "PYTHON"

# Visual Index Diagram:
#  Positive Index:   0   1   2   3   4   5
#  Characters:       P   Y   T   H   O   N
#  Negative Index:  -6  -5  -4  -3  -2  -1

print("Original String:", text)
print("Length of string (len):", len(text))

# 1. Positive Indexing (0-based, left to right)
print("\n--- Positive Indexing ---")
print("First character  (text[0]):", text[0])   # 'P'
print("Second character (text[1]):", text[1])   # 'Y'
print("Third character  (text[2]):", text[2])   # 'T'
print("Fifth character  (text[4]):", text[4])   # 'O'

# 2. Negative Indexing (Starts from -1 from the end, right to left)
print("\n--- Negative Indexing ---")
print("Last character        (text[-1]):", text[-1])  # 'N'
print("Second last character (text[-2]):", text[-2])  # 'O'
print("First via negative    (text[-6]):", text[-6])  # 'P'

# 3. Looping through string with indices
print("\n--- Characters with their indices ---")
for index in range(len(text)):
    print(f"Index {index} -> '{text[index]}' (Negative index: {index - len(text)})")

# 4. String Slicing Basics: [start:stop:step] (stop index is excluded)
print("\n--- Slicing Basics ---")
print("text[0:3] :", text[0:3])    # 'PYT'
print("text[2:5] :", text[2:5])    # 'THO'
print("text[:4]  :", text[:4])     # 'PYTH' (from start)
print("text[3:]  :", text[3:])     # 'HON'  (till end)
print("text[:]   :", text[:])      # 'PYTHON' (full string)
print("text[::-1]:", text[::-1])   # 'NOHTYP' (reversed string)
