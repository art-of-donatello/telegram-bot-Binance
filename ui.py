import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = listboxa.curselection()
	return itemSelected

def btnClickFunction():
	tInput.insert=("test")
	return

root = Tk()

# This is the section of code which creates the main window
root.geometry('863x582')
root.configure(background='#F0F8FF')
root.title('Hello')


# This is the section of code which creates the a label
test=Label(root, text='parite', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=50, y=44)


# This is the section of code which creates a listbox
listboxa=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
listboxa.insert('0', 'Waffles')
listboxa.place(x=169, y=156)

# This is the section of code which creates a button
Button(root, text='Button text!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=116, y=84)

# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=111, y=50)

root.mainloop()
