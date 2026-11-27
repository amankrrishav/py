class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} and {self.salary}"  # Use return, not print

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"  # Use return, not print

    def __len__(self):
        return len(self.name)


e1 = Employee("Aman", 250000)

print(e1.name, e1.salary)  # Aman 250000
print(str(e1))             # Aman and 250000 (or simply: print(e1))
print(repr(e1))            # Employee(name='Aman', salary=250000)
print(len(e1))             # 4
