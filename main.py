from tkinter import *
from tkinter import messagebox

def middle(x):
    display_one(x)
    disable_buttons()
    sign(x)

def sign(x):
    global tracker
    tracker = x

def display_one(x):
    textbox.insert(END, x)

def clear():
    textbox.delete('1.0', END)

def disable_buttons():
    btn_8["state"] = "disabled"
    btn_12["state"] = "disabled"
    btn_13["state"] = "disabled"
    btn_14["state"] = "disabled"
    btn_15["state"] = "disabled"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x):
    return x * x

def calculate():
    textbox_input = textbox.get("1.0", END)
    counter = 0
    try:
        temp = textbox_input.split(tracker)
        counter = 1
    except:
        textbox.delete('1.0', END)
        textbox.insert(END, "Error. Sign not selected")

    answer = 0

    if counter == 1:
        if tracker == '+':
            answer = add(int(temp[0]), int(temp[1]))
        elif tracker == '-':
            answer = subtract(int(temp[0]), int(temp[1]))
        elif tracker == 'x':
            answer = multiply(int(temp[0]), int(temp[1]))
        elif tracker == '/':
            answer = divide(float(temp[0]), float(temp[1]))
        elif tracker == '*':
            answer = square(int(temp[0]))

        textbox.delete('1.0', END)
        textbox.insert(END, answer)

        btn_8["state"] = "active"
        btn_12["state"] = "active"
        btn_13["state"] = "active"
        btn_14["state"] = "active"
        btn_15["state"] = "active"



#Create & Configure root
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

Grid.rowconfigure(frame, 0, weight=1)
textbox = Text(frame, height=3)
textbox.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10)

#Create a 4x4 (rows x columns) grid of buttons inside the frame
Grid.rowconfigure(frame, 1, weight=4)

Grid.columnconfigure(frame, 0, weight=1)
btn_1 = Button(frame, text="1", command=lambda: display_one('1'))
btn_1.grid(row=1, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_2 = Button(frame, text="2", command=lambda: display_one('2'))
btn_2.grid(row=1, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_3 = Button(frame, text="3", command=lambda: display_one('3'))
btn_3.grid(row=1, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_4 = Button(frame, text="C", command=clear)
btn_4.grid(row=1, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 2, weight=4)

Grid.columnconfigure(frame, 0, weight=1)
btn_5 = Button(frame, text="4", command=lambda: display_one('4'))
btn_5.grid(row=2, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_6 = Button(frame, text="5", command=lambda: display_one('5'))
btn_6.grid(row=2, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_7 = Button(frame, text="6", command=lambda: display_one('6'))
btn_7.grid(row=2, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_8 = Button(frame, text="+", command=lambda: middle('+'))
btn_8.grid(row=2, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 3, weight=4)

Grid.columnconfigure(frame, 0, weight=1)
btn_9 = Button(frame, text="7", command=lambda: display_one('7'))
btn_9.grid(row=3, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_10 = Button(frame, text="8", command=lambda: display_one('8'))
btn_10.grid(row=3, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_11 = Button(frame, text="9", command=lambda: display_one('9'))
btn_11.grid(row=3, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_12 = Button(frame, text="-", command=lambda: middle('-'))
btn_12.grid(row=3, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 4, weight=4)

Grid.columnconfigure(frame, 0, weight=1)
btn_13 = Button(frame, text="X", command=lambda: middle('x'))
btn_13.grid(row=4, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_14 = Button(frame, text="/", command=lambda: middle('/'))
btn_14.grid(row=4, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_15 = Button(frame, text="*", command=lambda: middle('*'))
btn_15.grid(row=4, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_16 = Button(frame, text="=", command=calculate)
btn_16.grid(row=4, column=3, sticky=N+S+E+W)


mainloop()
