def sum (a,b):
    ''' this is a doc string ''' # written right after the function definition
    c=a+b
    return c

print (sum(10,20))
print(sum.__doc__)

# we can have multi line docstring
def calculate_power(base, exponent):
    """
    Calculates the result of a base raised to an exponent.

    Parameters:
        base (int or float): The number to multiply.
        exponent (int): The power to raise the base to.

    Returns:
        int or float: The calculated power value.
    """
    return base ** exponent

print("Power result:", calculate_power(2, 5))
print("\n--- Accessing docstring via .__doc__ ---")
print(calculate_power.__doc__)


# 1. Using Python's built-in help() function
print("--- Using help() ---")
help(calculate_power)


# 2. Key Rule: Docstring MUST be the FIRST statement in the function body!
def incorrect_docstring():
    x = 10
    """This will NOT be recognized as a docstring because code came before it!"""
    return x

print("Incorrect docstring result:", incorrect_docstring.__doc__)  # Prints: None


# 3. Docstring vs Regular Comments (#)
# - Comments (#): Completely ignored by Python bytecode; used for developer notes.
# - Docstrings: Stored in memory as the __doc__ attribute; accessible at runtime
#   by documentation generators (Sphinx, pydoc) and IDE tooltips.


# 4. Standard Conventions (PEP 257):
# - Always use triple double quotes: """Docstring here"""
# - For single-line docstrings, keep closing quotes on the same line:
def square(n):
    """Return the square of number n."""
    return n * n

print("\nSingle-line docstring:", square.__doc__)


