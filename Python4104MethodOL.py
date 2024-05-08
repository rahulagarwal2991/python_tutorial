class Demo:
    def a1(self):
        print("with no argument")

    def a1(self, a):
        print("with one argument")

    def a1(self, a, b):
        print("with two argument")

d = Demo()

# d.a1() # TypeError: Demo.a1() missing 2 required positional arguments: 'a' and 'b'

#d.a1(10) # TypeError: Demo.a1() missing 1 required positional argument: 'b'

d.a1(10, 20) #with two argument