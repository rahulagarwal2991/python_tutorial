#Inside constructor by using self variable
class Student:
    def __init__(self):
        self.name="Karan"
        self.address = "Agra"
        self.no = 989898

    
s = Student()
print(s.__dict__) #{'name': 'Karan', 'address': 'Agra', 'no': 989898}

