import tkinter
import validate
from tkinter import *
import face_Recognition
import sendet
import time

def label():
    l1=Label(tk)
    l1.config(font='Bold 20', text='Enter your name::-')
    l1.grid(row=0,column=0)
    enu1=Entry(tk)
    enu1.config(width=20,bg='BLACK',font='arial 15',fg='White',borderwidth=10)
    enu1.grid(row=0,column=1)
    l2 = Label(tk)
    l2.config(font='Bold 20', text='Enter your voters Id::-')
    l2.grid(row=1,column=0)
    enu2 = Entry(tk)
    enu2.config(width=20, bg='BLACK', font='arial 15', fg='White',show='*',borderwidth=10)
    enu2.grid(row=1,column=1)
    b1=Button(tk)
    b1.config(text='Submit',width=8,borderwidth=5,command=lambda:validate.find_Det(enu1,enu2,tk))
    b1.grid(row=1,column=2)
def ent_mail(tk):
    gl=Label(tk,text="Enter your Gmail",font='arial 20',fg="Black",borderwidth=15)
    gl.grid(row=2,column=0)
    ge=Entry(tk)
    ge.config(bg='black',fg='white',font='arial 15',width=30,borderwidth=5)
    ge.grid(row=2,column=1)
    gb=Button(tk)
    gb.config(text='Enter',fg='Black',width=5,borderwidth=5,command=lambda:sendet.send_emil(ge,tk))
    gb.grid(row=2,column=2)


def done(tk):
    lib=Label(tk)
    lib.config(text="You have already voted thankyou::-",fg='green',bg='yellow',font='arial 20')
    lib.grid(row=2,column=0)
    tk.after(4000,lambda:lib.destroy())
    lib.config(bg="white",fg="White")
def none(tk):
    nonl=Label(tk)
    nonl.config(text="False information/not registered",bg='yellow',fg='red',font='arial 20')
    nonl.grid(row=2,column=1)
    tk.after(4000,lambda:nonl.destroy())
def sent_det(tk,otp):
    s1=Label(tk)
    s1.config(text="OTP on above email sent",fg="green",bg="yellow",font="arial 15")
    s1.grid(row=2,column=3)
    tk.after(4000,lambda:s1.destroy())
    s2=Label(tk)
    s2.config(text="Enter OTP",font="Arial 15",fg="black")
    s2.grid(row=3,column=0)
    e1=Entry(tk)
    e1.config(width=30,bg="Black",fg="White",borderwidth=5,font="Arial 15")
    e1.grid(row=3,column=1)
    b1=Button(tk,width=10,text="Enter",fg='Red',bg="black",command=lambda:check(e1,otp,tk))
    b1.grid(row=3,column=2)
def check(e1,otp,tk):
    if(e1.get()!=otp):
        w=0
        l1=Label(tk,text="Wrong otp")
        l1.config(fg="red",bg="Black",font="Arial 15")
        l1.grid(row=3,column=3)
        tk.after(4000,lambda:l1.destroy())
    else:
        pass

if __name__=='__main__':
    tk = tkinter.Tk()
    tk.iconbitmap("collog.ico")
    tk.title('Smart Voting System')
    tk.geometry('1500x1500')
    label()
    tk.mainloop()