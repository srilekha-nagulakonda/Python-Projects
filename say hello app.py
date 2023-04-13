from tkinter import *
mw=Tk()

mw.iconbitmap('flower.gif')

#title
mw.title('say hello')

def sayhello():
    name = userinput.get()
    greeting='hello '+name+' !'
    if name != '':
        text.config(text=greeting)
        userinput.delete(0,END)
    else:
        text.config(text='enter your name!')
userinput=Entry(mw,width=20,font=('Arial',20))
userinput.pack(padx=10,pady=10)

text=Label(mw,text='Enter your name!')
text.pack()

btn=Button(mw,text='say hello!',font=('Arial,20'),command=sayhello)
btn.pack(pady=10)


mw.mainloop()