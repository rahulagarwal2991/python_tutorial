# WAP to find a value is even or odd using if else statement

value = int(input("enter any interger value"))
# way 1
if value % 2 == 0 : # 0 == 0 -> True
    print("even")
else: 
    print("odd")

# way 2

if value % 2 : # 0 -> false
    print("odd")
else: 
    print("even")


    # 4 % 2 == 0 -> 4 is even
    # 0 == 0 # False == False # 2==2 -> true # 1==1 -> true # 0 == 0 -> true # False == False -> True

    # 4 % 2 -> 0