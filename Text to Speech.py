from tkinter import*
from gtts import gTTS
import os


def convert():

    text_convert=gTTS(text=text_e.get(),lang='en')
    text_convert.save("welcome.mp3")
    os.system("welcome.mp3")


t=Tk()

label_e=Label(t,text="ENTER TEXT YOU WANT AS SPEECH ",bg="black",fg="cyan",font="arial 18 bold").place(x=30,y=50)
text_e=Entry(t,font="lucida 14 bold")
text_e.place(x=30,y=100,height=100,width=440)
text_e.insert(0,'')


b=Button(t,text="CONVERT",command=convert,borderwidth=8,bg="blue",fg="white",font="arial 8 bold").place(x=200,y=208)

#Putting image in Title!!
# pic=PhotoImage(file="zpython.png")
# t.iconphoto(False,pic)
t.title("Text To Speech")
t.config(bg="cyan")
t.geometry("500x250")
t.mainloop()