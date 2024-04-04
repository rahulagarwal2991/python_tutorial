# WAP to enter students name and percentage of marks in dictionary and display them on screen

# dict_students_data = {
#     "ram"  : 90,
#     "shyam": 91,
#     "sita" : 92,
#     "geeta": 93,
# }
dict_students_data = {}
i = 1
while i == 1:
  name        = input("enter student name : ")
  percentage  = input("enter percentage : ")
  dict_students_data[name] = percentage
  i = int(input("Press 1 to continue and press any key to exit"))

for x in dict_students_data:
  print( "Student name : " , x ," marks percentage ", dict_students_data[x])


# Student name :  RamJi  marks percentage  99
# Student name :  shyamJi  marks percentage  99
# Student name :  test  marks percentage  89
# Student name :  test2  marks percentage  90
# Student name :  test3  marks percentage  89