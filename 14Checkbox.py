from tkinter import * 

root = Tk()
def check():
    global var
    lbl = Label(root,text = var.get()).pack()
var = StringVar() 


c = Checkbutton(root,variable = var,text = "Check this box", onvalue = "Checked", offvalue = "UnChecked")
c.deselect() 
c.pack()

btn = Button(root,text = "Click here", command = check).pack()


root.mainloop()