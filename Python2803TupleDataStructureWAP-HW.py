# wap to sum up 2 tuples in a way
# ex 
# t1 = (10,20,30,40,50)
# t2 = (5, 4, 3, 2, 1)
# output (15,24,33,42,51)

t1 = (10,20,30,40,50)
t2 = (5, 4, 3, 2, 1)
length = len(t1)
t3 = []

for i in range(length):
    t3.append(t1[i]+ t2[i])

print(t3) # [15, 24, 33, 42, 51]

# t1 = eval(input("Enter a tuple"))
# print(t1)
# print(type(t1))