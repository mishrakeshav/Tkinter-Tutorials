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
img6 = ImageTk.PhotoImage(Image.open("images/ironman.jpg"))
images = [img1,img2,img3,img4,img5,img6]
image_no= 0
my_label = Label(image = images[image_no])
my_label.grid(row = 0 , column = 0, columnspan = 3)


def forward():
    global image_no,images,my_label,status
    my_label.grid_forget()
    status.grid_forget()
    if image_no == len(images) -1 :
        image_no = 0 
    else:
        image_no += 1 
    my_label = Label(image = images[image_no])
    my_label.grid(row = 0 , column = 0, columnspan = 3)
    status = Label(root,text = "image {} of {}".format(image_no+1,len(images)), bd = 1,relief = SUNKEN,anchor =E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)


    
def back():
    global image_no,images
    global my_label,status
    if image_no == 0 :
        my_label.grid_forget()
        my_label = Label(image = images[image_no],state = DISABLED)
        my_label.grid(row = 0 , column = 0, columnspan = 3)  
    else:
        my_label.grid_forget()
        status.grid_forget()
        image_no -= 1 
        my_label = Label(image = images[image_no])
        my_label.grid(row = 0 , column = 0, columnspan = 3)
        status = Label(root,text = "image {} of {}".format(image_no+1,len(images)), bd = 1,relief = SUNKEN,anchor =E)
        status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)


forward_button = Button(root,text = ">>", command = forward)
quit_button = Button(root, text = "Exit program", command = root.quit)
back_button = Button(root,text = "<<",command = back)
status = Label(root,text = "image {} of {}".format(image_no+1,len(images)), bd = 1,relief = SUNKEN,anchor =E)


back_button.grid(row = 1 , column = 0)
quit_button.grid(row = 1, column = 1,pady = 10)
forward_button.grid(row =1, column = 2)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)
root.mainloop()