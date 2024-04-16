'''
Types of variables
1. Global Variable
2. local variable



 a = 10
b = 100


c = a+b
print(c) # 110

def sum():
    # a = 100
    # b = 200
    c = a+b
    print(c) # 300

sum()


c = a+b
print(c) # 110


###

d = 10

def modify():
    d = 20
    print(d)

print(d) # 10
modify() # 20
print(d) # 10


#######

# a = 10

def f1():
    a = 1111
    print(a)

def f2():
    print(a)


f1() # 1111
f2() # NameError: name 'a' is not defined

'''

###
a = 10

def f1():
    a = 1111
    print(a)
    print(globals()['a'])

def f2():
    print(a)


f1() # 1111
f2() # 10
