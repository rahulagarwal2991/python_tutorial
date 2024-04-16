'''
 Types of arguments

def sum_sub(a, b):
   pass

sum_sub(10, 5)

Types of args
1. positional arguments:
'''
def sub(a, b):
    return a-b
   

sub(10, 5) # 5
sub(5, 10) # -5
'''
2. keyword argument
'''
def sub(a, b):
    return a-b
   

sub(a=10, b = 5) # 5
sub(b = 5,a= 10) # 5


'''
3. default argument

'''
def sub(a= 10, b =5):
    return a-b
   
sub() # 5
sub(7) # 2

'''
4. variable length argument

'''
# def dunction_name(*parameters):

def sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print(total)

sum() # 0
sum(10) # 10 
sum(10, 20) # 30 
sum(10, 20 , 30) # 60