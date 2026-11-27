#write a Dog class with name and age, and a method bark() that prints "<name> says woof". Make two dogs and call bark() on each.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")   
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

d1 = Dog("Bruno", 1)
d1.bark()    
d1.describe()    