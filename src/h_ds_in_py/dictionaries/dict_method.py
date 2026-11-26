# Dictionary Methods in Python
# Dictionaries store data in key:value pairs.
# Keys must be unique and immutable (strings, numbers, tuples).

student = {
    "name": "Aman",
    "age": 21,
    "course": "CSE",
    "gpa": 8.5
}
print("Original dictionary:")
print(student)

# 1. get() - Safely access value of a key
# Unlike student['gender'] which throws KeyError if key doesn't exist,
# get() returns None (or a custom default) without crashing.
print("\n--- get() ---")
print("name   :", student.get("name"))
print("gender :", student.get("gender"))                   # None
print("gender :", student.get("gender", "Not Specified")) # Custom default

# 2. keys() - Returns a view of all keys
print("\n--- keys() ---")
print("keys :", student.keys())

# 3. values() - Returns a view of all values
print("\n--- values() ---")
print("values :", student.values())

# 4. items() - Returns a view of all (key, value) tuple pairs
print("\n--- items() ---")
print("items :", student.items())

print("Iterating with items():")
for key, value in student.items():
    print(f"  {key} -> {value}")

# 5. update() - Updates existing keys or inserts new key-value pairs
print("\n--- update() ---")
student.update({"gpa": 8.9, "city": "Bengaluru"})
print("After update:", student)

# 6. pop() - Removes specific key and returns its value
print("\n--- pop() ---")
removed_age = student.pop("age")
print("Removed age :", removed_age)
print("After pop('age'):", student)

# Safe pop with default value if key doesn't exist:
print("Safe pop missing key:", student.pop("salary", "Key not found"))

# 7. popitem() - Removes and returns the last inserted item (key, value)
print("\n--- popitem() ---")
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem()  :", student)

# 8. setdefault() - Returns value if key exists; inserts key with default if not
print("\n--- setdefault() ---")
# 'name' already exists -> returns current value 'Aman'
print("Existing key :", student.setdefault("name", "Unknown"))
# 'status' does not exist -> adds 'status': 'Active' and returns 'Active'
print("New key      :", student.setdefault("status", "Active"))
print("After setdefault:", student)

# 9. copy() - Creates a shallow copy of the dictionary
print("\n--- copy() ---")
student_copy = student.copy()
print("Copied dict:", student_copy)

# 10. fromkeys() - Creates a new dictionary with specified keys and a common value
print("\n--- fromkeys() ---")
subjects = ["Maths", "Physics", "Python"]
marks_dict = dict.fromkeys(subjects, 0)
print("fromkeys():", marks_dict)

# 11. Membership check: 'in' operator (checks keys in O(1) time)
print("\n--- Membership 'in' ---")
print("'name' in student :", "name" in student)   # True
print("'Aman' in student :", "Aman" in student)   # False (checks keys, not values!)

# 12. len() - Number of key-value pairs
print("\nTotal keys (len):", len(student))

# 13. clear() - Removes all elements from dictionary
print("\n--- clear() ---")
student.clear()
print("After clear():", student) # {}
