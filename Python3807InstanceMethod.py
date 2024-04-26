#Inside instance method by using self variable
class Student:
    def __init__(self):
        self.name="Karan"
        self.address = "Agra"

    def stu(self):
        self.no = 989898
    
s = Student()
s.stu()

print(s.__dict__)

