from tkinter import * 

root = Tk()


e = Entry(root,width = 50)
e.pack()
e.insert(0,"Enter your name")
def f():
    mylabel = Label(root,text = "Hello "+ e.get())
    mylabel.pack()

mybutton = Button(root, text = "Click me",command = f)
mybutton.pack()
root.mainloop()