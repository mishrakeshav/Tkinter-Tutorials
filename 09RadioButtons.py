from tkinter import * 
from  PIL import ImageTk,Image
root = Tk()
root.title("iamkeshavmishra7")
root.iconbitmap("favicon.ico")


# r = IntVar() 
# r.set(1)
# Radiobutton(root,text = "option 1 ", value = 1, variable = r).pack(anchor = W)
# Radiobutton(root,text = "option 2 ", value = 2, variable = r).pack(anchor = W)
# Radiobutton(root,text = "option 3 ", value = 3, variable = r).pack(anchor = W)
# Radiobutton(root,text = "option 4 ", value = 4, variable = r).pack(anchor = W)
# Radiobutton(root,text = "option 5 ", value = 5, variable = r).pack(anchor = W)
mylabel = Label(root,text = "")
# def clicked(value):
#     global mylabel 
#     mylabel.pack_forget()
#     mylabel = Label(root,text = "Option {}".format(value))
#     mylabel.pack()
     
# btn = Button(root,text = "Click Me!", command = lambda: clicked(r.get()))


# Using loop
r = StringVar() 
r.set("Maths")
subjects = ["Maths","Python","COA","CN","OS","AT"]
for subject in subjects:
    Radiobutton(root,text = subject, value = subject, variable = r).pack(anchor = W)

def clicked(value):
    global mylabel 
    mylabel.pack_forget()
    mylabel = Label(root,text = value)
    mylabel.pack()
     
btn = Button(root,text = "Click Me!", command = lambda: clicked(r.get()))
btn.pack()
root.mainloop()