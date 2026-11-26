# Constructors in Python (__init__ method)
# A constructor is a special method automatically executed when an object is instantiated.
# In Python, the constructor is defined using the __init__() dunder method.

class Employee:
    # Constructor
    def __init__(self, name, salary, bond):
        print("Constructor called! Initializing new employee...")
        # 'self' refers to the specific instance being created
        self.name = name          # Instance attribute
        self.salary = salary      # Instance attribute
        self.bond = bond          # Instance attribute

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")


# Creating instances (arguments are automatically passed to __init__)
e1 = Employee("John", 3400, 3)
e2 = Employee("Alice", 4500, 2)

print("\n--- Accessing methods ---")
e1.get_info()
print("e1 Salary:", e1.get_salary())

e2.get_info()
print("e2 Salary:", e2.get_salary())
