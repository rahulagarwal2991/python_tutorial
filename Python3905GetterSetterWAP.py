class Student: 
    all_marks ={}

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    def display(self):
        print(self.getName())
        print(self.getMarks())
        

    def grade(self):
        if self.getMarks() >= 60:
            print("Ist Div")
        elif self.getMarks() >=50:
            print("II Div")
        else:
            print("Fail")
        
n = int(input("Enter No of students"))

for i in range(n):
    name = input("Enter student name")
    marks = int(input("Enter Marks"))
    
    s = Student()
    s.setName(name)
    s.setMarks(marks)
    s.display()
    s.grade()
    


