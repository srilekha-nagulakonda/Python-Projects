from tkinter import *
mw=Tk()

label1= Label(mw,text='Telugu world',font=('Arial',20))
label2= Label(mw,text='Welcome to pycham',font=('Arial',20))
label1.grid(row=0,column=0)
label2.grid(row=1,column=2)

btn=Button(mw,text='click me!')
btn.grid(row=2,column=1, pady=20 , padx=10)

mw.mainloop()