


# python3 Python2703ListDataStructureAliasNCloning.py
# Alias and Cloning
# Alias : The process of giving another reference variable to the existing list is called aliasing

# ALIAS
x = [10,20,30,40,50]
y = x # here y is called as alias
y[1] = 200
print(x) #[10,20,30,40,50] #[10,200,30,40,50]
# here the problem is that whenever we change the value of y 
# then the changes will also reflect in x.

#CLONING
# To overcome this problem we can use cloning 
# 1. By using slice operator
x = [10,20,30,40,50]
y = x[:] # here y is called as alias
y[1] = 200
print(x) #[10, 20, 30, 40, 50]

# By using copy method
x = [10,20,30,40,50]
y = x.copy() # here y is called as alias
y[1] = 200
print(x) #[10, 20, 30, 40, 50]
print(y) #[10, 200, 30, 40, 50]

