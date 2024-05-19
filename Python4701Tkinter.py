#Python4701Tkinter.py
from tkinter import *;
from tkinter import ttk;
# set up base
tk = Tk()

#menu options
menu = Menu(tk)
tk.config(menu = menu)

#file menu
filemenu = Menu(menu)
menu.add_cascade(label= "File", menu= filemenu)
# sub menu
filemenu.add_command(label="New File")
filemenu.add_command(label="New Window")
filemenu.add_command(label="Open...")

#help menu
helpmenu = Menu(menu)
menu.add_cascade(label= "Help", menu= helpmenu)
#sub menu
helpmenu.add_command(label="gets Started")
helpmenu.add_command(label="Show All Commands")
helpmenu.add_command(label="Documentation")

#title
tk.title("Custom for for feedback")

#heading
Label(tk, text= "Form").grid(row=0)

#label and text box
Label(tk,text="Name").grid(row=1)
e1 = Entry(tk)
e1.grid(row=1, column=1)

#checkBox
var1 = IntVar()
Checkbutton(tk,text='Local', variable= var1).grid(row=2)
var2 = IntVar()
Checkbutton(tk,text='Non local', variable= var2).grid(row=3)

# radio button
var3 = IntVar()
Radiobutton(tk,text="Male", variable=var3, value=1).grid(row= 4)
Radiobutton(tk,text="Female", variable=var3, value=2).grid(row= 5)

#ListBox
Lb = Listbox()
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C programming')
Lb.insert(4, 'c++')
Lb.insert(5, 'Others')

Lb.grid(row= 6)

#combo box
ttk.Combobox(tk, values=["option1", "option2", "option3"]).grid(row= 7)

#text box
Text(tk, height=5, width=50).grid(row=8)


#button
Button(tk, text="submit", width=25).grid(row=9)


#show popup
tk.mainloop()
