# String Slicing in Python
# Syntax: string[start : stop : step]
# - start: starting index (inclusive), defaults to 0
# - stop:  ending index (exclusive), defaults to len(string)
# - step:  stride / step size, defaults to 1

text = "HelloWorld"

# Visual Indices:
#  Index:    0  1  2  3  4  5  6  7  8  9
#  Char:     H  e  l  l  o  W  o  r  l  d
#  Neg:    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print("Original String:", text)
print("Length:", len(text))

# 1. Basic Slicing [start : stop] (stop is excluded)
print("\n--- Basic Slicing ---")
print("text[0:5] :", text[0:5])    # 'Hello'
print("text[5:10]:", text[5:10])   # 'World'
print("text[2:7] :", text[2:7])    # 'lloWo'

# 2. Omitting Start or Stop
print("\n--- Omitting Start or Stop ---")
print("text[:5]  :", text[:5])     # Start to index 4 -> 'Hello'
print("text[5:]  :", text[5:])     # Index 5 to end   -> 'World'
print("text[:]   :", text[:])      # Full shallow copy -> 'HelloWorld'

# 3. Slicing with Step [start : stop : step]
print("\n--- Slicing with Step ---")
print("text[::2]  :", text[::2])   # Every 2nd character -> 'Hlool'
print("text[1::2] :", text[1::2])  # Starting from index 1 -> 'elWrd'
print("text[0:8:3]:", text[0:8:3]) # Step of 3 -> 'Hlw'

# 4. Negative Index Slicing
print("\n--- Negative Indices in Slicing ---")
print("text[-5:]   :", text[-5:])    # Last 5 characters -> 'World'
print("text[:-5]   :", text[:-5])    # From start up to last 5 characters -> 'Hello'
print("text[-8:-3] :", text[-8:-3])  # Between -8 and -3 -> 'lloWo'

# 5. Reversing Strings with Negative Step
print("\n--- Reversing and Backward Steps ---")
print("text[::-1]   :", text[::-1])   # Entire string reversed -> 'dlroWolleH'
print("text[8:3:-1] :", text[8:3:-1]) # Backwards from index 8 to 4 -> 'lroW'

# 6. Slicing is Safe with Out-of-Bounds Indices
print("\n--- Out-of-Bounds Safety ---")
# Direct indexing text[100] raises IndexError, but slicing handles it cleanly:
print("text[0:100]  :", text[0:100])  # 'HelloWorld'
print("text[50:100] :", repr(text[50:100])) # '' (empty string)
