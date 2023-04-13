from tkinter import *
#create window
main_window=Tk()
def clicked():
    label=Label(main_window,text='srilekha is creating window',font=('Arial',20),padx=30,pady=30)
    label.pack(side=TOP)

#creating button

button=Button(main_window,text='click me!',font=('Arial',16),padx=10,pady=15,command=clicked)
button.pack(pady=10,padx=10)

#creating input from user

user=Entry(main_window,width=50,font=('Arial',20))
user.pack(padx=50,pady=30)

main_window.mainloop()