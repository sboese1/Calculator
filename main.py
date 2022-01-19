from tkinter import *

#Create & Configure root
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 4x4 (rows x columns) grid of buttons inside the frame
Grid.rowconfigure(frame, 0, weight=1)

Grid.columnconfigure(frame, 0, weight=1)
btn_1 = Button(frame)
btn_1.grid(row=0, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_2 = Button(frame)
btn_2.grid(row=0, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_3 = Button(frame)
btn_3.grid(row=0, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_4 = Button(frame)
btn_4.grid(row=0, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 1, weight=1)

Grid.columnconfigure(frame, 0, weight=1)
btn_5 = Button(frame)
btn_5.grid(row=1, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_6 = Button(frame)
btn_6.grid(row=1, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_7 = Button(frame)
btn_7.grid(row=1, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_8 = Button(frame)
btn_8.grid(row=1, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 2, weight=1)

Grid.columnconfigure(frame, 0, weight=1)
btn_9 = Button(frame)
btn_9.grid(row=2, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_10 = Button(frame)
btn_10.grid(row=2, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_11 = Button(frame)
btn_11.grid(row=2, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_12 = Button(frame)
btn_12.grid(row=2, column=3, sticky=N+S+E+W)


Grid.rowconfigure(frame, 3, weight=1)

Grid.columnconfigure(frame, 0, weight=1)
btn_13 = Button(frame)
btn_13.grid(row=3, column=0, sticky=N+S+E+W)

Grid.columnconfigure(frame, 1, weight=1)
btn_14 = Button(frame)
btn_14.grid(row=3, column=1, sticky=N+S+E+W)

Grid.columnconfigure(frame, 2, weight=1)
btn_15 = Button(frame)
btn_15.grid(row=3, column=2, sticky=N+S+E+W)

Grid.columnconfigure(frame, 3, weight=1)
btn_16 = Button(frame)
btn_16.grid(row=3, column=3, sticky=N+S+E+W)


mainloop()
