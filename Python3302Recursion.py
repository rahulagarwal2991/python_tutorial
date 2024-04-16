'''
# recursion
factorial 5 => 5*4*3*2*1
# wap to find factorial of a number using recursion
'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))


5*fact(4)

5*4*fact(3)

'''
fact(5) => 5 * 4 * 3 * 2 * 1 => 120
fact(4) => 4 * 3 * 2 * 1
fact(3) => 3 * 2 * 1
fact(2) => 2 * 1
fact(1) => 1


'''