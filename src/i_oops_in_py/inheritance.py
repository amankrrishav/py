# Inheritance in Python
# Inheritance allows a child (derived) class to inherit attributes and methods
# from a parent (base) class, promoting code reusability.


# 1. Single Inheritance & super()
print("--- 1. Single Inheritance & super() ---")

class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        print(f"Employee: {self.name} | Salary: {self.salary} | Company: {self.company}")


# Programmer inherits from Employee: class ChildClass(ParentClass)
class Programmer(Employee):
    default_lang = "Python"

    def __init__(self, name, salary, language):
        # super().__init__() calls the parent class constructor
        super().__init__(name, salary)
        self.language = language

    # Method Overriding: Child provides its own version of get_info()
    def get_info(self):
        super().get_info()  # Calls parent's get_info()
        print(f"  Primary Language: {self.language}")

    def code(self):
        print(f"{self.name} is writing {self.language} code.")


emp = Employee("Aman", 50000)
prog = Programmer("Rishav", 75000, "Python")

emp.get_info()
print()
prog.get_info()
prog.code()


# 2. Multiple Inheritance (Child inherits from more than one parent)
print("\n--- 2. Multiple Inheritance ---")

class FrontendDev:
    def build_ui(self):
        print("Building responsive UI with React")

class BackendDev:
    def build_api(self):
        print("Building REST APIs with FastAPI")

# FullStack inherits from both FrontendDev and BackendDev
class FullStackDev(FrontendDev, BackendDev):
    def deploy(self):
        print("Deploying full-stack application to cloud")

dev = FullStackDev()
dev.build_ui()
dev.build_api()
dev.deploy()


# 3. Multilevel Inheritance (Grandparent -> Parent -> Child)
print("\n--- 3. Multilevel Inheritance ---")

class Person:
    def __init__(self, country):
        self.country = country

class Manager(Employee):
    def manage_team(self):
        print(f"Manager {self.name} is running the sprint review.")

mgr = Manager("Sara", 95000)
mgr.get_info()
mgr.manage_team()


# 4. Built-in Type Checks: isinstance() and issubclass()
print("\n--- 4. Type & Subclass Verification ---")
print("is prog an Employee?    :", isinstance(prog, Employee))     # True
print("is prog a Programmer?   :", isinstance(prog, Programmer))   # True
print("is emp a Programmer?    :", isinstance(emp, Programmer))    # False

print("is Programmer a subclass of Employee?:", issubclass(Programmer, Employee)) # True
print("is Employee a subclass of Programmer?:", issubclass(Employee, Programmer)) # False
