# Python4102OperatorOL
class Book:
    def __init__(self , pages):
        self.pages = pages

    def __add__(self, other): # magic method
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

b3 = b1+b2

print(b3)

