from tkinter import * 
from PIL import ImageTk,Image
root = Tk()
root.title("root window")


def open():
    global my_img 
    top = Toplevel()
    top.title("This is the top window!")
    my_img = ImageTk.PhotoImage(Image.open("images/cap.png"))
    my_label = Label(top,image = my_img)
    my_label.pack()
    btn2 = Button(top,text = "Close", command = top.destroy).pack()

button = Button(root,text="Click to open window", command = open).pack()
root.mainloop()