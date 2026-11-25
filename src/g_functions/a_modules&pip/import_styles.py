# Import Syntax & the __name__ == '__main__' Idiom in Python

# 1. Standard import: module_name.function()
import math
print("Standard import:", math.sqrt(25))

# 2. Alias import using 'as' (great for long module names)
import math as m
print("Aliased import :", m.floor(7.8))

# 3. Import specific functions or constants directly using 'from ... import'
from math import pi, sin
print("Direct import  : pi =", round(pi, 4))

# 4. Import all symbols using '*' (Generally DISCOURAGED: pollutes namespace)
# from math import *

# 5. Understanding __name__ == "__main__"
# When a Python script is run directly, its special variable __name__ is set to "__main__".
# When it is imported by another script, __name__ is set to the module's filename (e.g. "import_styles").
#
# This idiom lets a file act both as an executable script AND as an importable module:
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("\n--- Running directly as main program ---")
    print("__name__ is:", __name__)
    print(greet("Aman"))
else:
    print("\n--- Loaded as an imported module ---")
    print("__name__ is:", __name__)
