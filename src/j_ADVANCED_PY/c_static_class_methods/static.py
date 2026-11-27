class Employeee:
    company = "Hp"
    def __init__(self,name,salary):
        self.name =name 
        self.salary =salary
    #instance method (by default)
    def print_info(self):
        info = f"The name of employee is {self.name } and salary is {self.salary}"
        print(info)

    #static method
    @staticmethod
    def sum(a,b):
        return a+b

    
    #class -method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_com_name(cls, new_company):
        cls.company = new_company


e1 = Employeee("Aman",250000)
print(e1.company)    #hp
Employeee.change_com_name("Acer")
print(e1.company)


