# constructor __int__()
'''
1. constructor is a special method in python
2. The name should be __init__(self)
3. It will execute automatically at the time of object creation
4. The main purpose of this is to initialize value
5. It will be called only once for a object.
6. constructor is optional to create, if we did not create any constructor in that case
    python create default const.
'''
# WAP to check functionality of a const.

class A:
    def __init__(self):
        print("hello from constructor")

a = A() #hello from constructor

