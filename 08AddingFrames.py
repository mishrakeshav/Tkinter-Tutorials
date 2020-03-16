from tkinter import * 
from  PIL import ImageTk,Image
root = Tk()
root.title("iamkeshavmishra7")
root.iconbitmap("favicon.ico")

frame = LabelFrame(root,text="this is a frame...",padx = 50, pady = 50)
frame.pack(padx= 10,pady = 10)

button = Button(frame,text = "Dont click here ")
button2 = Button(frame, text = "or here..") 
button.grid(row = 0, column = 0)
button2.grid(row = 1,column = 1)

root.mainloop()