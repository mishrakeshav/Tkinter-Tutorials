from tkinter import * 

root = Tk()

# mybutton = Button(root, text = "Click me",  padx = 50, pady = 50,state = DISABLED)
# fg - foreground color 
# bg - background color
# padx - width
# pady - height
mybutton = Button(root, text = "Click me", fg = "#ffffff",bg="#000000")
mybutton.pack()
root.mainloop()