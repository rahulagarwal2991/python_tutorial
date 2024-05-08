'''
# Python4201ExceptionHandling.py

1. syntax exception

x = 10
if x ==10:
    print "Hello" #SyntaxError: Missing parentheses in call to 'print'.

2. runtime exception
print(10/0) #ZeroDivisionError

'''
# SyntaxError
# print("Hi")
# x = 10
# if x ==10:
#     print "Hello" #SyntaxError: Missing parentheses in call to 'print'.


'''
File "/Users/rahul/python/Python4201ExceptionHandling.py", line 18
    print "Hello" #SyntaxError: Missing parentheses in call to 'print'.
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
'''

# Run time error:
# print("Hi")
# x = 10
# if x ==10:
#     print (10/0)

'''
Hi
Traceback (most recent call last):
  File "/Users/rahul/python/Python4201ExceptionHandling.py", line 31, in <module>
    print (10/0)
           ~~^~
ZeroDivisionError: division by zero
'''
'''
Syntax:
try:
    block of code
except ExceptionType:
    block of code
'''


try:
    print (10/0)
except ZeroDivisionError:
    print("Error")


# try:
#     print("Hi")
#     x = 10
#     if x ==10:
#         print (10/0)
# except ZeroDivisionError:
#     print("Number divisble by 0 is not possible")

# print("Hello")




# try:
#     print("Hi")
#     x = 10
#     if x ==10:
#         print (10/0)
# except ZeroDivisionError as m:
#     print("Number divisble by 0 is not possible because of ", m)

# print("Hello")

