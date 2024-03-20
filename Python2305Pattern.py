# WAP to print a square pattern by taking user input
# 3 2 1
# 3 2 1
# 3 2 1

i = int(input("Enter the rows count"))

for j in range(1, i+1):
    for k in range(i,0, -1):
        print(k, end=" ")
    print()


    
