# returning multiple values from a function

def sum_sub(a, b):
    sum = a+b
    sub = a-b
    return sum, sub

x, y = sum_sub(10, 5)

print("The sum is ", x)
print("The sub is ", y)