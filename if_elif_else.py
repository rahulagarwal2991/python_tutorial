# if cond:
#     statement
# elif cond:
#     statement
# elif cond:
#     statement
# elif cond:
#     statement
# else:
#     statement

# WAP to find grade of a student
marks = 55
if marks > 70:
    print("I Div")
elif marks > 60:
    print("II Div")
else:
    print("III Div")



user_input = input("enter value between 0 and 9: ")
user_input = int(user_input)

if user_input == 0:
    print("Zero")
elif user_input == 1:
    print("One")
else:
    print("Invalid")