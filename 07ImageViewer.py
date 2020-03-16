from tkinter import * 
from  PIL import ImageTk,Image
root = Tk()
root.title("iamkeshavmishra7")
root.iconbitmap("favicon.ico")

img1 = ImageTk.PhotoImage(Image.open("images/cap.png"))
img2 = ImageTk.PhotoImage(Image.open("images/batman.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/joker.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/spider.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/cap.gif"))
images = [img1,img2,img3,img4,img5]
image_no= 0
my_label = Label(image = images[image_no])
my_label.grid(row = 0 , column = 0, columnspan = 3)


def forward():
    global image_no,images,my_label
    my_label.grid_forget()
    if image_no == len(images) -1 :
        image_no = 0 
    else:
        image_no += 1 
    my_label = Label(image = images[image_no])
    my_label.grid(row = 0 , column = 0, columnspan = 3)
def back():
    global image_no,images
    
    if image_no == 0 :
        my_label = Label(image = images[image_no],state = DISABLED)
        my_label.grid(row = 0 , column = 0, columnspan = 3)  
    else:
        my_label.grid_forget()
        image_no -= 1 
        my_label = Label(image = images[image_no])
        my_label.grid(row = 0 , column = 0, columnspan = 3)
     
forward_button = Button(root,text = ">>", command = forward)
quit_button = Button(root, text = "Exit program", command = root.quit)
back_button = Button(root,text = "<<",command = back)

back_button.grid(row = 1 , column = 0)
quit_button.grid(row = 1, column = 1)
forward_button.grid(row =1, column = 2)

root.mainloop()