from tkinter import *


def conv(): 
    gram = float (e1_value.get()) * 1000
    pound = float(e1_value.get()) *  2.20462
    ounce =  float(e1_value.get()) * 35.274
    t1.delete("1.0",END)
    t1.insert(END,gram )
   
    t2.delete("1.0",END)
    t2.insert(END,pound)

    t3.delete("1.0",END)
    t3.insert (END, ounce)


window = Tk() #creating window
b1 = Button(window, text='run', command=conv) #Button creation
b1.grid(row=0, column=0)


e1_value  = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row= 1, column= 0,)


t1 = Text(window, height= 5, width = 30)
t1.grid(row=2, column=0)

t2 = Text(window, height= 5, width = 30)
t2.grid(row=3, column=0)

t3 = Text(window, height= 5, width = 30)
t3.grid(row=4, column=0)

window.mainloop()