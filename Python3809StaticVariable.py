# Static Variable

class A:
    outside_vraiable = 10 # static variable

    def __init__(self):
        self.inside_variable = 20

a  = A()
a1 = A()

print(a.outside_vraiable) # 10
print(a.inside_variable) # 20
print(a1.inside_variable) # 20

A.outside_vraiable = 11

a.inside_variable = 21

print(a.outside_vraiable) # 11
print(a1.outside_vraiable) #11

print(a.inside_variable) # 21
print(a1.inside_variable) # 20