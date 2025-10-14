from tkinter import *
from tkinter import messagebox
import os
from random import randint

def on_enter1(e):
    delete_btn.config(background="#DC143C",fg="white",cursor="hand2")
def on_leave1(e):
    delete_btn.config(background="red",fg="white",cursor="arrow")
def on_enter2(e):
    enter_btn.config(background="#ADFF2F",fg="white",cursor="hand2")
def on_leave2(e):
    enter_btn.config(background="yellow",fg="white",cursor="arrow")
def on_enter3(e):
    close_btn.config(background="#00FA9A",fg="white",cursor="hand2")
def on_leave3(e):
    close_btn.config(background="chocolate",fg="white",cursor="arrow")

def dell():
    player_entry.delete(0,END)
def close():
    win.destroy()
def click():
    try:
        random1 = randint(0,1)
        if random1 == 0:
            computer = "shir"
        if random1 == 1:
            computer = "khat"
        player = str(player_entry.get())
        pc = f"computer = {computer}"
        
        if player == "shir" and computer == "shir":
            natije = "computer is on system"
        if player == "khat" and computer == "shir":
            natije = "computer is on system"
        if player == "shir" and computer == "khat":
            natije = "computer is off system"
        if player == "khat" and computer == "khat":
            natije = "computer is off system"
        if computer == "khat":
            os.system("shutdown /s /t 11")
        
        new = Toplevel(win)
        new.title("natije")
        new.geometry("320x320")
        new.resizable(False,False)
        new.config(background="red")
        
        new_lable = Label(new,text=f"{pc} \n {natije}",font=("arial",17),bg="white",fg="blue",width=20)
        new_lable.pack(padx=10,pady=10)
        
        new_btn = Button(new,text="close",font=("arial",17),width=20,bg="green",fg="white",command=new.destroy)
        new_btn.pack(padx=10,pady=10)
    
        new.mainloop()    
    except ValueError:
        messagebox.showinfo("please enter your str")



win = Tk()
win.title("shir or khat")
win.geometry("500x500")
win.resizable(False,False)
win.config(background="black")


lable_pc = Label(win,text="computer: \n shir or khat:",font=("arial",17),bg="black",fg="green",width=20)
lable_pc.pack(padx=10,pady=10)

lable_player = Label(win,text="player",font=("arial",17),width=20,bg="black",fg="green")
lable_player.pack(padx=10,pady=10)

player_entry = Entry(win,bg="blue",fg="white",width=20,font=("arial",16),justify=CENTER)
player_entry.pack(padx=10,pady=10)

delete_btn = Button(win,text="delete",fg="white",bg="red",width=20,font=("arial",17),command=dell)
delete_btn.pack(padx=10,pady=10)

enter_btn = Button(win,text="Enter",width=20,font=("arial",17),bg="yellow",fg="green",command=click)
enter_btn.pack(padx=10,pady=10)

close_btn = Button(win,text="close",font=("arial",17),width=20,bg="chocolate",fg="white",command=close)
close_btn.pack(padx=10,pady=10)

delete_btn.bind("<Enter>",on_enter1)
delete_btn.bind("Leave",on_leave1)
enter_btn.bind("<Enter>",on_enter2)
enter_btn.bind("<Leave>",on_leave2)
close_btn.bind("<Enter>",on_enter3)
close_btn.bind("<Leave>",on_leave3)

win.mainloop()