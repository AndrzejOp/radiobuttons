from tkinter import *


code = ["code1", "code2", "code3"]

def choose():
    if x.get() == 0:
        print("Your choice: code1")
    elif x.get() == 1:
        print("Your choice: code2")
    elif x.get() == 2:
        print("Your choice: code3")
    else:
        print("Your choice: nothing")

window = Tk()

code1image = PhotoImage(file='code1.png')
code2image = PhotoImage(file='code2.png')
code3image = PhotoImage(file='code3.png')

code_images = [code1image,code2image,code3image]


x = IntVar()
for i in range(len(code)):
    radiobutton = Radiobutton(window,
                              text=code[i],
                              variable=x,
                              value=i,
                              padx=30,
                              font=('Impact', 20),
                              image=code_images[i],
                              compound=LEFT,
                              indicatoron=0,
                              width=480,
                              command=choose)

    radiobutton.pack(anchor=W)

window.mainloop()