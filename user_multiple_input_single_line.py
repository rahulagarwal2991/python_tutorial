# WAP to assign multiple value to multiple variables in a single line
# a, b, c = [100, 3000, 400]
# a, b, c = 100, 3000, 400
# print(a)
# print(b)
# print(c)

# WAP to take user input with space as sepaerator
# a, b = [int(x) for x in input("Enter 2 values").split()]
# working
# a, b = [int(x) for x in "10 20".split()]
# a, b = [int(x) for x in ["10", "20"] ]
# a, b = [10, 20]
# a = 10
# b = 20
# print(a)
# print(b)
## split() 

# WAP to read 3 float numbers from the keyboard with seperator ,  and print their sum
a, b, c = [float(x) for x in input("Enter 3 values").split(',')]
print(a)
print(b)
print(c)
# sum to be printed