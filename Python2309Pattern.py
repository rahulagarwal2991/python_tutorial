# WAP to print a square pattern by taking user input
# 
# * * * * *
# * * * * 
# * * *
# * *
# *


i = int(input("Enter the rows count"))

for j in range(i, 0, -1): # (5,1,-1) [5,4,3,2] | (5,0,-1) [5,4,3,2,1]
    for k in range(1, j+1):
        print( "*", end=" ")
    print()
   
# for j in range(i+1, 1, -1): # (5,1,-1) [5,4,3,2] | (5,0,-1) [5,4,3,2,1]
#     for k in range(1, j):
#         print( "*", end=" ")
#     print()
