# WAP to find value minimum of 3 values
a = int(input("Enter first value: "))
b = int(input("Enter Second value: "))
c = int(input("Enter third value: "))

min = a if a < b and a < c else b if b < c else c
print("Minimum value is :  ", min)