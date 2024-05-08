class Demo:
    def __init__(self):
        print("with no argument")

    def __init__(self, a):
        print("with one argument")

    def __init__(self, a, b):
        print("with two argument")


# d = Demo()         #TypeError: Demo.__init__() missing 2 required positional arguments: 'a' and 'b'

# d = Demo(10)        #TypeError: Demo.__init__() missing 1 required positional argument: 'b'

d = Demo(10, 20)      #With two argument