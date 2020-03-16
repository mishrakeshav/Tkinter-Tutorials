from tkinter import * 

root = Tk()

mylabel1 = Label(root, text = "This is label 1")
mylabel2 = Label(root, text = "                                       ")
mylabel3 = Label(root, text = "This is label 2")

mylabel1.grid(row = 0, column = 0)
mylabel2.grid(row = 1, column = 1)
mylabel3.grid(row = 1, column = 5)

root.mainloop()