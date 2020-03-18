from tkinter import * 

root = Tk()
root.geometry("400x400")
def check():
    global var
    lbl = Label(root,text = var.get()).pack()
var = StringVar() 
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
var.set(options[0])
drop = OptionMenu(root,var,*options)
drop.pack()

btn = Button(root,text = "Click here", command = check).pack()


root.mainloop()