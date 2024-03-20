# WAP to print a square pattern by taking user input
# A A A
# B B B
# C C C

# K A R 
# S A W
i = int(input("Enter the rows count"))

for j in range(1, i+1):
    for k in range(1,i+1):
        print( chr(64+j), end=" ")
    print()


    
