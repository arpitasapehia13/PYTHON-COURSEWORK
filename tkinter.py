from tkinter import *
root = Tk()

w = Canvas(root, width=500, height=300)

label = Label(root, text="My first tkinter program")
label1 = Label(root, text="i know how to use GUI").grid(row=0, column=0)
label.grid(row=0, column=1)
w.create_line(100, 35, 200, 35, width=5)
w.grid()

button = Button(root, text="submit")
button.grid(row=10, column=20)
e = Entry(root, width=50, bg="red", fg="white", borderwidth=5)
e.grid(row=1, column=1)

root.mainloop()
