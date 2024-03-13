# special operator
# 1 identity operator
    # 1. is
    # 2. is not
    # r1 is r2
    # r1 is not r2
# 2 Membership operator
  

# r1 = 10
# print(id(r1)) #4395929416
# r2 = 10
# print(id(r2)) #4395929416
# print(r1 is r2) # True


# r1 = 10
# print(id(r1)) #4395929416
# r2 = 10.0
# print(id(r2)) #4338501968
# print(r1 is r2) # False

## is not 
# r1 = 10
# print(id(r1)) #4358094664
# r2 = 10.0
# print(id(r2)) #4351330640
# print(r1 is not r2) # True

####
list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
print(id(list1)) #4348187712
print(id(list2)) #4348380288
print(list1 is list2) #False
print(list1 is not list2) #True
print(list1 == list2) #True
# is -> address comparision
# == -> content comparision