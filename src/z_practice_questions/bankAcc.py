#build a class of bank account with deposit (amt) and get_balance . 

class demo_bank_acc:

    def __init__ (self,balance):   
        self.balance = balance
        


    def deposit(self,amount):
        self.balance = self.balance + amount
        

    def get_balance(self):
        return f"your current balance is {self.balance}" "\nthank you!"

    def withdraw(self,amount):
        self.balance = self.balance - amount

acc1 = demo_bank_acc(0) 
acc1.deposit(100)
print(acc1.get_balance())
acc1.withdraw(10)
print(acc1.get_balance())
