from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.pack()
Lb1 = Listbox(root)
Lb1.insert(1, "python")
Lb1.insert(2, "peri")
Lb1.insert(3, "c")
Lb1.insert(4, "php")
Lb1.insert(5, "jsp")
Lb1.insert(6, "ruby")

Lb1.pack()
#e = Entry(root, width=50)
# e.pack()


def myclick():
    label = Label(root, text="Hello!" + Lb1.get())
    label.pack()


button = Button(root, text="Submit", command=myclick)
button.pack()


root.mainloop()
