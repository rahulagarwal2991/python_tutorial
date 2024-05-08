class P:
    def __init__(self):
        print("Parent class")


class C(P):
    def __init__(self):
        print("Child class")

c = C() #Child class