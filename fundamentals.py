# fundamental data types vs immmutability
#PVM (parallel virtual machine)

a = 10
b = 10

# a same b 
# a memory address b memory address 

c = a is b
print(c) #True

print(id(a))#4470091592
print(id(b))#4470091592