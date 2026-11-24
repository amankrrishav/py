# String Representation with Quotes in Python

# 1. Single and Double Quotes (Both work identically in Python)
s1 = 'Hello, World!'
s2 = "Hello, World!"
print("Single quote string:", s1)
print("Double quote string:", s2)

# 2. Quotes inside Quotes (Without backslash escaping)
# Use double quotes if your string contains a single quote / apostrophe
sentence1 = "It's a wonderful day!"
print(sentence1)

# Use single quotes if your string contains double quotes
sentence2 = 'He said, "Python is awesome!"'
print(sentence2)

# 3. Escaping Quotes with Backslash (\' and \")
escaped_single = 'It\'s also possible to escape single quotes.'
escaped_double = "He said, \"Escaping double quotes works too!\""
print(escaped_single)
print(escaped_double)

# 4. Triple Quotes (''' or """) for Multi-line Strings
multi_line_str = """This is a multi-line string.
It preserves line breaks
and indentation automatically."""
print("\nMulti-line string:")
print(multi_line_str)

# 5. Raw Strings (r"" or r'') - Ignores escape characters
path = r"C:\users\aman\new_folder"
print("\nRaw string path (r'...'):", path)
