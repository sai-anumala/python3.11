from tkinter import *
root=Tk()
root.geometry('900x900')
lbl=Label(root,text="It's my first GU interface..")
lbl.grid()
def clicked():
    lbl.configure(text='you have just clicked!')
btn=Button(root,text="Click me",fg='red',bg='yellow',command=clicked)
btn.grid(row=0,column=1)
def used():
    res='you wrote'+txt.get()
    lbl.configure(root,text=res)
txt=Entry(root,width='20')
txt.grid(row=2,column=0)
btn2=Button(root,text='click here',fg='Green',bg='red',command=used)
btn2.grid(row=3)
root.mainloop()