from tkinter import *
root=Tk()
root.geometry('400x400')
lbl=Label(root,text='here will display what you wrote after clicked button')
lbl.grid()
txt=Entry(root,width='20')
txt.grid(row=2)
def clicked():
    res=txt.get()
    lbl.configure(text=res)
btn=Button(root,text='click me',command=clicked,fg='red')
btn.grid(row=3)
root.mainloop()