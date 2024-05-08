# Operator Overloading
class Student:
    def __init__(self, name, marks ):
        self.name = name
        self.marks = marks

    def __gt__(self, other): # greater than
        return self.marks > other.marks


    def __le__(self, other): # less than equal to 
        return self.marks <= other.marks
    
print("10 > 20 ", 10>20) # False
s1 = Student("Karan", 99)
s2 = Student("swayam", 98)
print("s1 > s2", s1 > s2) # True
print("s2 > s1", s2 > s1) #False
print("s1 <= s2", s1 <= s2) # False
print("s2 <= s1", s2 <= s1) #True


