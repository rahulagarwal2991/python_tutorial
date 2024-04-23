# rollno, gender, subjects, age, fn, mn, gurdn, add...

class MyClass:
    def __init__(self, name, age): # __init__ method
        print("this is executed")
        self.name = name
        self.age = age

obj1 = MyClass("Karan", 22) # here obj1 is reference variable
obj2 = MyClass("Swayam", 22) # object

print(obj1.name)
print(obj1.age)

print(obj2.name)
print(obj2.age)