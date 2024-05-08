#Python4110ParentMethodAccess.py

class P:
    def __init__(self):
        print("Parent class")


class C(P):
    def __init__(self):
        print("Child class")
        super().__init__() #Parent class

c = C() #Child class