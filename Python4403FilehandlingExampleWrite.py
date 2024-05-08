# Python4402FilehandlingExample.py
'''
write(str)
writelines(list of lines)

'''
f = open("sales.txt", 'w')
f.write("Python ")
f.write("is ")
f.write("a ")
f.write("very ")
f.write("good ")
f.write("language \n")


f.write("Python \n")
f.write(" is \n")
f.write(" a \n")
f.write(" very \n")
f.write(" good \n")
f.write(" language \n")

f.write("Python is a very good language \n \n")

f.close()

######
f = open("sales.txt", 'a')
list = ["ram \n", "shyam \n", "sita \n", "gita \n"]

f.writelines(list)
f.close()