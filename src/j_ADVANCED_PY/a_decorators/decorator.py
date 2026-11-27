# @decorator is a func which takes an existing func and turns to another func(as wrapper func) and return the wrapper 

def decorator(taken_func):
    def wrapper():
        print("This will be executed 1st")
        taken_func()
        print("This will be executed last")
    return wrapper

@decorator
def will_be_taken():
    print("this is a taken function wrapped in wrapper and executed")


will_be_taken()

'''
===============================================
'''
print("\n- - - - - - - - - - - - - - - - - - ")
def shout(taken_func1):
    def wrapper():
        print("*** LOUD MODE ***")
        taken_func1()
        print("************************")
    return wrapper

@shout
def say_hi():
    print("Hello Python")

say_hi()    


