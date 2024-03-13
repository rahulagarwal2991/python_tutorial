# Type casting
# #1. int() : 
# a= 10.11
# print(type(a)) #<class 'float'>
# b = int(a)
# print(type(b)) #<class 'int'>

#HW
#True
#False
#"100"
#"10.5"
#'100'
#"ten"
#"0B1111"

a= "100"
print(type(a)) #<class 'str'>
b = int(a)
print(b) # 100
print(type(b)) #<class 'int'>



#float()
# 10
# 10+5j
# True
# False
# "10"
# "10.5"
# "ten"
# "0B1111"

a= 10
print(type(a)) 
b = float(a)
print(b) 
print(type(b))

#complex()
#Form 1: complex(x)
# a= 10.5
# b= complex(a)
# print(b) #(10.5+0j)
# 10
# True
# False
# "10"
# "10.5"
# "ten"
# "0B1111"

# Form 2 complex(x,y)
# x= 2
# y =-5
# a = complex(x,y)
# print(a) #(2-5j)

# #HW
# x= True
# y =False
# a = complex(x,y)
# print(a) # share output

#bool()

# 0
# 1
# 10
# 10.5
# 0.0
# 10-2j
# 0+5j
# 0+0j
# "True"
# "False"
# ""

# a= 10
# print(type(a)) #<class 'int'>
# b = str(a)
# print(type(b)) #<class 'str'>

# 10.5
# 10+5j
# True