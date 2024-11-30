from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.pack()


def myclick():
    label = Label(root, text="Hello!" + e.get())
    label.pack()


button = Button(root, text="Submit", command=myclick)
button.pack()


root.mainloop()
