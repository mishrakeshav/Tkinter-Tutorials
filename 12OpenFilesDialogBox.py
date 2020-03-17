from tkinter import * 
from PIL import ImageTk,Image
from tkinter import filedialog 

root = Tk()
root.title("My APP")
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "/images",title = "Select a file", filetypes = (("png files", "*.png"),("all files","*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    mylabel1 = Label(root,text =root.filename).pack()
    mylabel  = Label(image=my_image).pack()

btn = Button(root,text = "Open File", command = open).pack()
root.mainloop()