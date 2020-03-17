# The different message boxes you can use are:
# - showinfo -- returns ok
# - showwarning -- returns ok
# - showerror --returns ok
# - askquestion - returns 'yes' if yes else 'no'
# - askokcancel return 1 if ok else  0
# - askyesno -- returns 1 if yes else 0
from tkinter import * 
from tkinter import messagebox
root = Tk()

def popup():
    response = messagebox.showinfo("This is the title! ", "Hello World! ")
    label = Label(root,text = response)
    label.pack()

button = Button(root, text = "Popup",   command = popup)

button.pack()
root.mainloop()