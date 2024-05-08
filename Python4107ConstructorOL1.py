# Python4105MethodOLWorkingEX.py

class Demo:

    def __init__(self, a = None, b= None):

        if a == None:
            print("with no argument")
        elif b == None:
            print("with one argument")
        else:
            print("with two argument")


d = Demo() # with no argument

d = Demo(10) # with one argument

d = Demo(10, 20) #with two argument