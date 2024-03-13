# output statement
print()

# form 1 : print() without any argument

# form 2 : print() with any argument

print("hello" + " world")
print(10+2)

# form 3 : print with variable name of arguments
a, b,c = 10, 20 , 30
print("The variable names are ", a, b, c) #The variable names are  10 20 30

# default seperator is space.

print("The variable names are ", a, b, c, sep=':') #The variable names are :10:20:30

print("The variable names are ", a, b, c, sep='-') #The variable names are -10-20-30

# form 4: print with end attribute
print("hello")
print("python")
print("programmer")
# if we want print the data in same line we can do that also using end attribute

print("hello", end= '-')
print("python", end = '-')
print("programmer")

# the default value for end attribute is \n which is new line character


# form 5 print(object) ex : list tuple set etc
list = [1, 2,3,4 ,5 ,6] 
tuple = (1, 2,3,4 ,5 ,6)
print(type(list))
print(type(tuple))
print(list)
print(tuple)

#form 6 print(string , valriable list)
# we can use print stmt with string and any number of arguments
name = "GWG"
age = 1
course_1 = "java"
course_2 = "python"
print("Hello my name is ", name, "and my age is", age)
print("we are learning here ", course_1 , " and ", course_2)


# form 7 formatted string
# %i, %d => int 
# %f  => float
# %s => string

# ex print("format string",%(variable list))

a = 10
b = 20
c = 30
print("%d" %a) #10
print("The value of a = %i" %a) #The value of a = 10

print("The value of a = %d, b= %d and c is %d" %(a,b,c))
#The value of a = 10, b= 20 and c is 30

str_1 = "hello"
str_2 = "GWG"
str_3 = "karan"
print("The value of first string is %s second is %s third is %s" %(str_1, str_2, str_3))
#The value of first string is hello second is GWG third is karan

# form 8 print with replacement operator {}
name = "GWG"
age = 10
course = "python"
print("Hello {0} my age is {1} and i am learning {2}".format(name, age , course)) #Hello GWG my age is 10 and i am learning python
print("Hello {a} my age is {b} and i am learning {c}".format(a= name, b = age , c= course)) #Hello GWG my age is 10 and i am learning python