# wap to display sum of command line arguments
#argv  -> this is used to access command line arguments
from sys import argv 
sum =0
args = argv[1:]

for x in args:
    sum += int(x) # sum = sum + x

print(sum)

# WAP to input string (names) and do concatination