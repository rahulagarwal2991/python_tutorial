# WAP to print a square pattern by taking user input
# a a a
# b b b 
# c c c 

i = int(input("Enter the rows count"))

for j in range(1, i+1):
    for k in range(1,i+1):
        print( chr(64+j), end=" ")
    print()


    
