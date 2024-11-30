from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text="brown", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)


root.mainloop()
