from tkinter import * 

root = Tk()
root.title("Calculator")

e = Entry(root,width = 40, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10 , pady = 10)
first_number = ""
math = None 
def button_click(number):
    currnt = e.get()
    e.delete(0,END)
    e.insert(0,str(currnt) + str(number))

def button_add():
    global first_number
    global math 
    math = "addition"
    first_number = int(e.get())
    e.delete(0,END) 
def button_subtract():
    global first_number
    global math 
    math = "subtraction"
    first_number = int(e.get())
    e.delete(0,END) 
def button_multiply():
    global first_number
    global math 
    math = "multiplication"
    first_number = int(e.get())
    e.delete(0,END) 
def button_divide():
    global first_number
    global math 
    math = "division"
    first_number = int(e.get())
    e.delete(0,END) 


def button_equal():
    second_number = int(e.get())
    e.delete(0,END)
    if math == "addition":
        e.insert(0,first_number + second_number)
    elif math == "multiplication":
        e.insert(0,first_number*second_number) 
    elif math == "subtraction":
        e.insert(0,first_number-second_number)
    elif math == "division":
        e.insert(0,first_number/second_number)

def button_clear():
    global first_number
    first_number = "" 
    e.delete(0,END)



btn_1 = Button(root, text = "1", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(1))
btn_2 = Button(root, text = "2", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(2))
btn_3 = Button(root, text = "3", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(3))
btn_4 = Button(root, text = "4", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(4))
btn_5 = Button(root, text = "5", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(5))
btn_6 = Button(root, text = "6", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(6))
btn_7 = Button(root, text = "7", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(7))
btn_8 = Button(root, text = "8", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(8))
btn_9 = Button(root, text = "9", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(9))
btn_0 = Button(root, text = "0", padx = 40, pady = 20,bg="#d1f5d3", command = lambda: button_click(0))
btn_clear = Button(root, text = "Clear", padx = 79, pady = 20,bg="#d1f5d3", command = button_clear)
btn_equal = Button(root, text = "=", padx = 91, pady = 20,bg="#d1f5d3", command = button_equal)
btn_add = Button(root, text = "+", padx = 39, pady = 20,bg="#d1f5d3", command = button_add)

btn_subtract = Button(root, text = "-", padx = 41, pady = 20,bg="#d1f5d3", command = button_subtract)
btn_multiply = Button(root, text = "*", padx = 43, pady = 20,bg="#d1f5d3", command = button_multiply)
btn_divide = Button(root, text = "/", padx = 40, pady = 20,bg="#d1f5d3", command = button_divide)


btn_1.grid(row = 3, column = 0)
btn_2.grid(row = 3, column = 1)
btn_3.grid(row = 3, column = 2)

btn_4.grid(row = 2, column = 0)
btn_5.grid(row = 2, column = 1)
btn_6.grid(row = 2, column = 2)

btn_7.grid(row = 1, column = 0)
btn_8.grid(row = 1, column = 1)
btn_9.grid(row = 1, column = 2)

btn_0.grid(row = 4, column = 0)

btn_clear.grid(row = 4, column = 1,columnspan = 2)
btn_equal.grid(row = 5, column = 0,columnspan = 2)
btn_add.grid(row = 5, column = 2)

btn_subtract.grid(row = 6, column = 0)
btn_multiply.grid(row = 6, column = 1)
btn_divide.grid(row = 6, column = 2)
root.mainloop()