# decorators with arguments



def repeat(n):
    def decorator(taken_func):
        def wrapper(a):
            for i in range(n):
                taken_func(a)
        return wrapper
    return decorator

@repeat(3)
def used_func(a):
    print(f"Hi, Lucia {a}.")

used_func("and Aman")                
