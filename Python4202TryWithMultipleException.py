# try with multiple exceptions

# way 1
# try:
#     a = int(input("Please enter value 1 "))
#     b = int(input("Please enter value 2 "))
#     print(a/b)
# except ZeroDivisionError as zd:
#     print("Error : ", zd) # 10 , 0 -> Error :  division by zero
# except ValueError as ve:
#     print("Error: ", ve) # 10 , ten -> Error:  invalid literal for int() with base 10: 'ten'


# # single except block to handle to multiple exception
# #way2
# try:
#     a = int(input("Please enter value 1 "))
#     b = int(input("Please enter value 2 "))
#     print(a/b)
# except (ZeroDivisionError,ValueError )as zd:
#     print("Error : ", zd) 


# Default exception block
try:
    a = int(input("Please enter value 1 "))
    b = int(input("Please enter value 2 "))
    print(a/b)
except (ZeroDivisionError) as zd:
    print("Error : ", zd) 
except: # default except 
    print("unkown Error")