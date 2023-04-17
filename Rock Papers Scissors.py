from tkinter import *
import random
from tkinter import messagebox

win=Tk()

lst=["ROCK","PAPER","SCISSOR"]

userscore=0
pcscore=0

def rock():
    def result_win():
        messagebox.showinfo("CONGRATULATIONS","Congratulations "+ name_e.get()+" YOU WIN !!")
    def result_loose():
        messagebox.showinfo("LOOSE","Oops  ,"+ name_e.get()+" YOU LOOSE !!")

    global userscore,pcscore

    user_e.delete(0,END)
    computer_e.delete(0,END)
    show="ROCK"
    user_e.insert(0,show)

    pc=""+random.choice(lst)
    computer_e.insert(0,pc)

    if user_e.get()=="ROCK" and computer_e.get()=="PAPER":
        pcscore=pcscore+10
        pcscore=str(pcscore)
        computer_score.delete(0,END)
        computer_score.insert(0,pcscore)
        pcscore=int(pcscore)
        
    if user_e.get()=="ROCK" and computer_e.get()=="SCISSOR":
        userscore=userscore+10
        userscore=str(userscore)
        user_scorel.delete(0,END)
        user_scorel.insert(0,userscore)
        userscore=int(userscore)

    if userscore==100 :
        result_win()
    if pcscore==100 :
        result_loose()
        



def paper():
    def result_win():
        messagebox.showinfo("CONGRATULATIONS ","Congtratulations"+ name_e.get()+" YOU WIN !!")
    def result_loose():
        messagebox.showinfo("LOOSE","Oops  ,"+ name_e.get()+" YOU LOOSE !!")

    global userscore,pcscore
    user_e.delete(0,END)
    computer_e.delete(0,END)
    show="PAPER"
    user_e.insert(0,show)

    pc=""+random.choice(lst)
    computer_e.insert(0,pc)

    if user_e.get()=="PAPER" and computer_e.get()=="SCISSOR":
        pcscore=pcscore+10
        pcscore=str(pcscore)
        computer_score.delete(0,END)
        computer_score.insert(0,pcscore)
        pcscore=int(pcscore)
        
    if user_e.get()=="PAPER" and computer_e.get()=="ROCK":
        userscore=userscore+10
        userscore=str(userscore)
        user_scorel.delete(0,END)
        user_scorel.insert(0,userscore)
        userscore=int(userscore)

    if userscore==100 :
       result_win()

    if pcscore==100 :
       result_loose()



def scissor():
    def result_win():
        messagebox.showinfo("CONGRATULATIONS","Congratulations"+ name_e.get()+" YOU WIN !!")
    def result_loose():
        messagebox.showinfo("LOOSE","Oops  ,"+ name_e.get()+" YOU LOOSE !!")

    
    global userscore,pcscore

    user_e.delete(0,END)
    computer_e.delete(0,END)
    show="SCISSOR"
    user_e.insert(0,show)

    pc=""+random.choice(lst)
    computer_e.insert(0,pc)

    if user_e.get()=="SCISSOR" and computer_e.get()=="ROCK":
        pcscore=pcscore+10
        pcscore=str(pcscore)
        computer_score.delete(0,END)
        computer_score.insert(0,pcscore)
        pcscore=int(pcscore)
        
    if user_e.get()=="SCISSOR" and computer_e.get()=="PAPER":
        userscore=userscore+10
        userscore=str(userscore)
        user_scorel.delete(0,END)
        user_scorel.insert(0,userscore)
        userscore=int(userscore)

    if userscore==100 :
        result_win()


    if pcscore==100 :
        result_loose()





label=Label(win,text='** ROCK PAPER SCISSOR **',font="arial 20 bold").place(x=10,y=10)
user_l=Label(win,text="  USER  ",bg="purple",fg="black",font="arial 14 bold").place(x=10,y=80)
computer_l=Label(win,text="COMPUTER",bg="yellow",fg="black",font="arial 14 bold").place(x=250,y=80)

user_e=Entry(win,font="lucida 10 bold")
user_e.place(x=40,y=150,height=40,width=100)

vs_l=Label(win,text='VS',bg="black",fg="white",font="lucida 18 bold").place(x=160,y=155)

computer_e=Entry(win,font="lucida 10 bold")
computer_e.place(x=220,y=150,height=40,width=100)

choose_l=Label(win,text=" CHOOSE ",bg="dark cyan",fg="white",font="lucida 20 bold").place(x=120,y=230)

rock_b=Button(win,text="ROCK ",bg="white",fg="black",font="britannic 14 bold",command=rock,borderwidth=10).place(x=10,y=300)
paper_b=Button(win,text=" PAPER ",bg="white",fg="black",font="britannic 14 bold",command=paper,borderwidth=10).place(x=140,y=300)
scissor_b=Button(win,text="SCISSOR",bg="white",fg="black",font="britannic 14 bold",command=scissor,borderwidth=10).place(x=280,y=300)

name_l=Label(win,text="NAME",bg="blue",fg="black",font="arial 14 bold").place(x=10,y=450)
name_e=Entry(win,font="forte 14 bold")
name_e.place(x=100,y=450)


user_scorel=Label(win,text=" SCORE ",bg="purple",fg="black",font="arial 16 bold").place(x=10,y=380)
user_scorel=Entry(win,font="calibri 14 bold")
user_scorel.place(x=110,y=380,height=30,width=40)

computer_score=Label(win,text=" SCORE ",bg="yellow",fg="black",font="arial 16 bold").place(x=250,y=380)
computer_score=Entry(win,font="calibri 14 bold")
computer_score.place(x=350,y=380,height=30,width=40)




win.title("** STONE PAPER SCISSORS **")
win.geometry("400x500")
win.config(bg="black")
win.mainloop()