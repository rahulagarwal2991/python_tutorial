'''
Finally Block:

syntax:

try:
    // code
except Exception e:
    // code 
finally: 
    // code

'''

# try:
#     print(10/0)
# except :
#     print("Exception handling")
# finally: 
#     print("This is a message")

'''
try:
    stm1
    stm2
    stm3
except:
    stm4
finally:
    stm5
    stm6

'''

try:
    print(10/2," first")
    print(10/2, "second")
    print(10/2, "third")
    try:
        print(10/2," first")
        print(10/2, "second")
        print(10/2, "third")
    except :
        print(10/2, "fourth")
except :
    print(10/2, "fourth")
    try:
        print(10/2," first")
        print(10/2, "second")
        print(10/2, "third")
    except :
        print(10/2, "fourth")
finally: 
    print(10/2, "fifth")
    try:
        print(10/2," first")
        print(10/2, "second")
        print(10/2, "third")
    except :
        print(10/2, "fourth")

        