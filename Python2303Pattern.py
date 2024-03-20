# WAP to print a square pattern by taking user input
# 1 1 1
# 2 2 2
# 3 3 3

i = int(input("Enter the rows count"))

for j in range(1, i+1):
    for k in range(1,i+1):
        print(j, end=" ")
    print()


    
