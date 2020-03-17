from tkinter import * 

root = Tk()
root.title("Sliders")
root.geometry("400x400")

horizontal = Scale(root,from_= 0, to = 300)
horizontal.pack() 

vertical = Scale(root,from_ = 0 , to = 300,orient=HORIZONTAL)
vertical.pack()

def slide():
    root.geometry(str(vertical.get()) + "x" +str(horizontal.get()))
btn = Button(root,text = "Click Me!",command = slide)
btn.pack()

root.mainloop()