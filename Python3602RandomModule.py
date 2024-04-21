# random Module
# 1. random() function: 
from random import *


for i in range(10):
    print(random()) # it creates a unique value b/w 0 and 1
    
for i in range(10):
    print(randint(1000, 9999)) # it will generate a random interger value of a defined range including these values


for i in range(10):
    print(randint(1, 10))


for i in range(10):
    print(uniform(1, 10)) # it returns random float values b/w 2 given numbers (not included)

# randrange([start], end, [step])
 
for i in range(10):
    print(randrange(10))

for i in range(10):
    print(randrange(4,10, 2))

# choice():
# 
# 
list = ["karan", "swayam", "Rahul"]
for i in range(10):
    print(choice(list))

shuffle(list)
print(list)
