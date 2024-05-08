# Python4105MethodOLWorkingEX.py

class Demo:

    def a1(self, a = None, b= None):

        if a == None:
            print("with no argument")
        elif b == None:
            print("with one argument")
        else:
            print("with two argument")

d = Demo()

d.a1() # with no argument

d.a1(10) # with one argument

d.a1(10, 20) #with two argument