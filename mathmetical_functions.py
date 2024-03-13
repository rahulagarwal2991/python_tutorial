# Math Module
#Module -> functions + variables and classes

# Example 1
# import math
# a = math.sqrt(25)
# print(a) #5.0
# print(math.pi) #3.141592653589793

# # Example 2
# import math as m
# a = m.sqrt(25)
# print(a) #5.0
# print(m.pi) #3.141592653589793

# Example 3
# from math import sqrt,pi
# a = sqrt(25)
# print(a) #5.0
# print(pi) #3.141592653589793

# print all math variable and functions
from cmath import inf
import math
math_attr = dir(math)
for a in math_attr:
    print(a)

#important functions
    ceil 
    floor
    pow
    factorial

#important variables
    pi
    e
    inf
    nan