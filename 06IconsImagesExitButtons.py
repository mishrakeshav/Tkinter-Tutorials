from tkinter import * 
from  PIL import ImageTk,Image
root = Tk()
root.title("iamkeshavmishra7")
root.iconbitmap("favicon.ico")

my_img = ImageTk.PhotoImage(Image.open("cap.png"))
my_label = Label(image = my_img)
my_label.pack()
quit_button = Button(root, text = "Exit program", command = root.quit)
quit_button.pack()

root.mainloop()