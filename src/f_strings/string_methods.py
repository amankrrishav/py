# Common String Methods in Python
# Note: Strings are IMMUTABLE in Python.
# String methods do NOT modify the original string; they return a NEW string.

msg = "  Hello, Python World!  "
print("Original string:", repr(msg))

# 1. Changing Case
print("\n--- 1. Case Conversion ---")
text = "hello, python WORLD!"
print("upper()     :", text.upper())       # 'HELLO, PYTHON WORLD!'
print("lower()     :", text.lower())       # 'hello, python world!'
print("title()     :", text.title())       # 'Hello, Python World!' (capitalizes every word)
print("capitalize():", text.capitalize())  # 'Hello, python world!' (capitalizes first letter only)
print("swapcase()  :", text.swapcase())    # 'HELLO, PYTHON world!' (inverts uppercase/lowercase)

# 2. Stripping Whitespace
print("\n--- 2. Stripping Whitespace ---")
spaced = "   python   "
print("strip()  :", repr(spaced.strip()))   # 'python' (removes both ends)
print("lstrip() :", repr(spaced.lstrip()))  # 'python   ' (removes leading/left)
print("rstrip() :", repr(spaced.rstrip()))  # '   python' (removes trailing/right)

# Stripping custom characters
url = "https://example.com/"
print("Custom strip:", url.strip("/").removeprefix("https://"))

# 3. Finding & Counting
print("\n--- 3. Searching & Counting ---")
sentence = "learning python is fun and python is powerful"
print("count('python') :", sentence.count("python"))  # 2
print("find('python')  :", sentence.find("python"))   # 9 (index of first occurrence)
print("rfind('python') :", sentence.rfind("python"))  # 27 (index of last occurrence)
print("find('java')    :", sentence.find("java"))     # -1 (not found, does not raise error)

# index() works like find(), but raises ValueError if substring is not found:
# print(sentence.index("java"))  # -> ValueError: substring not found

# 4. Replacing Text
print("\n--- 4. Replacing Substrings ---")
phrase = "I like apples and apples are tasty"
print("replace all  :", phrase.replace("apples", "oranges"))
print("replace count:", phrase.replace("apples", "oranges", 1)) # replaces only the 1st match

# 5. Splitting and Joining
print("\n--- 5. Splitting and Joining ---")
csv_data = "apple,banana,mango,grapes"
fruits = csv_data.split(",")               # Splits into a list by comma
print("split(','):", fruits)

words = "Python is very readable".split()  # Splits by whitespace by default
print("split()   :", words)

# join() merges elements of a list into a single string using a delimiter
joined_str = " - ".join(fruits)
print("join()    :", joined_str)

# 6. Boolean Inspection Methods (is...)
print("\n--- 6. Inspection Methods (Returns True/False) ---")
filename = "report_2026.pdf"
print("startswith('report'):", filename.startswith("report")) # True
print("endswith('.pdf')    :", filename.endswith(".pdf"))     # True

print("'12345'.isdigit()   :", "12345".isdigit())             # True
print("'Python'.isalpha()  :", "Python".isalpha())            # True
print("'Py3'.isalnum()     :", "Py3".isalnum())               # True (alphanumeric)
print("'   '.isspace()     :", "   ".isspace())               # True

# 7. Immutability Demonstration
print("\n--- 7. String Immutability ---")
original = "hello"
modified = original.upper()
print("original after upper():", original) # still 'hello'
print("modified string        :", modified) # 'HELLO'
