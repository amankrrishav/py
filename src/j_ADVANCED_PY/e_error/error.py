# Error & Exception Handling in Python

# 1. Basic try - except Block
# Prevents program crash and allows graceful recovery when an error occurs
print("--- 1. Basic try - except ---")
try:
    num = int("abc")  # Raises ValueError: invalid literal for int()
except Exception as e:
    print("Caught an error:", e)


# 2. Handling Specific Exceptions
# Best practice: catch specific errors instead of a generic 'except Exception'
print("\n--- 2. Handling Specific Exceptions ---")
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")
except ValueError:
    print("Error: Invalid numeric value!")
except TypeError:
    print("Error: Operation performed on incompatible types!")


# 3. try - except - else - finally
# - try:     Code that might raise an exception
# - except:  Executes IF an error occurs
# - else:    Executes ONLY IF no error occurs in try
# - finally: ALWAYS executes (useful for cleanup like closing files or DB connections)
print("\n--- 3. try - except - else - finally ---")
def divide_numbers(x, y):
    try:
        ans = x / y
    except ZeroDivisionError:
        print("  [except]  : Cannot divide by zero!")
    else:
        print(f"  [else]    : Success! {x} / {y} = {ans}")
    finally:
        print("  [finally] : Cleanup executed (always runs).")

print("Test 1 (Valid Division):")
divide_numbers(10, 2)

print("\nTest 2 (Zero Division):")
divide_numbers(10, 0)


# 4. Raising Exceptions Manually (raise keyword)
# Use 'raise' when business logic or validation rules are violated
print("\n--- 4. Raising Exceptions (raise) ---")
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 120:
        raise ValueError("Age is unrealistic!")
    print(f"Valid age registered: {age}")

try:
    set_age(21)
    set_age(-5)  # Triggers ValueError
except ValueError as err:
    print("Caught manually raised exception:", err)


# 5. Custom / User-Defined Exceptions
# Build domain-specific exceptions by inheriting from Python's built-in Exception class
print("\n--- 5. Custom User-Defined Exception ---")
class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds available bank balance."""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw Rs.{amount}. Current balance is only Rs.{self.balance}."
            )
        self.balance -= amount
        print(f"Withdrawn Rs.{amount}. Remaining balance: Rs.{self.balance}")

account = BankAccount(5000)

try:
    account.withdraw(2000)  # Works: balance becomes 3000
    account.withdraw(4000)  # Raises InsufficientFundsError
except InsufficientFundsError as err:
    print("Caught custom exception:", err)
