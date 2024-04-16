# Python3408NestedFunction.py

# nested function
# we can declare a function inside function and such functions are called nested functions


def outer1():
    print("outer1 function")

    def sum(a, b):
        print(a+b)
        
    sum(10, 5)

def outer2():
    print("outer2 function")

    def sum(a, b):
        print(a-b)
        
    sum(10, 5)


outer1()
outer2()

# inner() # NameError: name 'inner' is not defined. Did you mean: 'iter'