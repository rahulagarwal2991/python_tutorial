# WAP to print a square pattern by taking user input
# *
# * * 
# * * *
# * * * *
# * * * * *


# * * * * *
# * * * * 
# * * *
# * *
# *


# *
# * * 
# * * *
# * * * *
# * * * * *
# * * * * 
# * * *
# * *
# *

i = int(input("Enter the rows count"))

# or below logic
for j in range(1, i+1):
    for k in range(1, j+1):
        print( "*", end=" ")
    print()

for j in range(i-1, 0, -1):
    for k in range(1, j+1):
        print( "*", end=" ")
    print()
