class Employee:
    def __init__ (self,name,salary):
        self.name = name 
        self.salary =salary

    @property
    def first_name(self):
        l1 = self.name.split(" ")
        # print(l1) # will print none
        return l1

    @first_name.setter
    def first_name(self,first):
        l1 = self.name.split(" ")
        new_name = f"{first} {l1[1]}"
        self.name = new_name    

e1 = Employee("Aman Rishav",250000)

''' we dont want this -->

print(e1.first_name())
e1.make_first_name("Kr")
print(e1.name)
'''
print(e1.first_name)
e1.first_name = "Kumar"
print(e1.name)
