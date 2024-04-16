# function decorators

def decor(func):
    def inner(x):
        if int(x) <= 0:
            print("invalid number")
        else:
            func(x)
    return inner


# @decor
def printMobileNumber(x):
    print(x)


printMobileNumber(999991234)

printMobileNumber(0)