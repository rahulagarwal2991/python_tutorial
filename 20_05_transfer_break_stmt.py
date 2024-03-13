# 1. Break : we can use break statements inside loops to break loop execution on some condition

for i in range(1, 21):
    if i == 7:
        break
    print(i)

print("hello")


data =[100, 200, 1000, 300]
for i in data:
    if(i > 500):
        print("you can not add product more than 500 rs ")
        break


# 1
# 2
# 3
# 4
# 5
# 6


# 2 . continue: we can use continue statement 
# to skip current iteration and continue other iterations


for i in range(1, 21):
    if i == 7:
        continue
    print(i)

print("hello")
