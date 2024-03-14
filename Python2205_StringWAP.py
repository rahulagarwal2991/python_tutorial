# WAP to accept user input and print the char by index (using both +ve and -ve index)    
string = input("Enter a string")
j =0
for i in string:
    print("The char in +ve index " + str(j) + " and -ve index "+ str(j-len(string)) +" is " + str(i))
    j = j+1

#karanSwayam

# test
# 0123
#-4-3-2-1