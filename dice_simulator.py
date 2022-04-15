import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

gj = tk.Tk()
gj.geometry("500x500")
gj.title("DICE")
gj.configure(background="black")


a=Image.open("1.gif")
resized1=a.resize((200,200),Image.ANTIALIAS)
a1=ImageTk.PhotoImage(resized1)

b=Image.open("2.gif")
resized2=b.resize((200,200),Image.ANTIALIAS)
a2=ImageTk.PhotoImage(resized2)

c=Image.open("3.gif")
resized3=c.resize((200,200),Image.ANTIALIAS)
a3=ImageTk.PhotoImage(resized3)

d=Image.open("4.gif")
resized4=d.resize((200,200),Image.ANTIALIAS)
a4=ImageTk.PhotoImage(resized4)

e=Image.open("5.gif")
resized5=e.resize((200,200),Image.ANTIALIAS)
a5=ImageTk.PhotoImage(resized5)

f=Image.open("6.gif")
resized6=f.resize((200,200),Image.ANTIALIAS)
a6=ImageTk.PhotoImage(resized6)
def roll():
    lst=[a1,a2,a3,a4,a5,a6]
    l1=Label(gj,image=random.choice(lst))
    l1.place(x=20,y=20)

if __name__=="__main__":
    b1 = tk.Button(gj, text="Roll", command=lambda: roll()).pack()
gj.mainloop()