# loop with else block
# inside loop execution if break statement not executed,
# then only else part will be executed

data =[100, 200, 1000, 300]
for i in data:
    if(i > 500):
        print("you can not add product more than 500 rs ")
        break
    print(i)
else:
    print("you don't break the loop")

print("out of loop")