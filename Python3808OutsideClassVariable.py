#outside class using object reference variable
class Student:
    def __init__(self):
        self.name="Karan"
        self.address = "Agra"

    def stu(self):
        self.no = 989898
    
s = Student()
s.stu()

print(s.name)
print(s.address)
print(s.no)
