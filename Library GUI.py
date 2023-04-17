from tkinter import*
import time
import random


num="1234567890"
num=str(num)


dt=time.strftime("%d %m, %Y")
win=Tk()

english=["HoneyBee "," HoneyComb ", "Grammar "]
hindi=["shitij","kritika","vistaas","grammar"]
maths=["class 6","class 7","class 8","class 9","class 10"]
science=["class 6","class 7","class 8","class 9","class 10"]
python=["python for beginners","python Advanced"]
c=["c for beginners","c Advanced"]

def booklist():
    books=["English","Hindi","Maths","Science","Python","C"]
    print(books)

def bookscategory():
    cate=Tk()
    e=Text(cate,font="calinri 10 bold")
    e.place(x=0,y=0,height=300,width=300)
    english="ENGLISH  "
    hindi="HINDI  "
    maths="MATHS "
    science="SCIENCE "
    python="PYTHON "
    c=" C "
    total="AVAILABLE BOOKS ARE :- \n\n"+english+"\n\n"+hindi+"\n\n"+maths+"\n\n"+science+"\n\n"+python+"\n\n"+c+"\n\n"+"FOR MORE DETAILS GO IN BOOK LIST CHART >>"
    e.insert(END,total)
    cate.geometry("300x300")
    cate.mainloop()




#BOOKLIST FUNCTION !!
def booklist():
    lst=Tk()
    lst_l=Label(lst,text="Which Book List You Want ",bg="white",fg="black",font="arial 12 bold").place(x=10,y=50)
    lst_e=Entry(lst,font="calibri 12 bold")
    lst_e.place(x=30,y=80,height=40,width=150)
    lst.geometry("300x200")
    lst.config(bg="orange")
    
    def main():
        english="ENGLISH :- HoneyBee , HoneyComb , Grammar "
        hindi="HINDI :- Vistaas , Shitij , Kritika , Grammar "
        maths="MATHS :- Class 6 , Class 7 , Class 8 , Class 9 , Class 10"
        science="SCIENCE :- Class 6 , Class 7 , Class 8 , Class 9 , Class 10"
        python="PYTHON :- Python for beginners , Python Advanced"
        c=" C :- C for beginners , C Advanced"

        lst_1=Tk()
        res_e=Text(lst_1,font="lucida 12 bold")
        res_e.place(x=0,y=0,height=200,width=300)
        if lst_e.get()=="english":
            res_e.insert(END,english)
        elif lst_e.get()=="hindi":
            res_e.insert(END,hindi)
        elif lst_e.get()=="maths":
            res_e.insert(END,maths)
        elif lst_e.get()=="science":
            res_e.insert(END,science)
        elif lst_e.get()=="python":
            res_e.insert(END,python)
        elif lst_e.get()=="c":
            res_e.insert(END,c)
        lst_1.geometry('290x190')
        lst_1.config(bg='cyan')
        lst_1.mainloop()
    b=Button(lst,text="ENTER",bg="red",fg="white",font="arial 10 bold",command=main).place(x=70,y=140)


#ISSUE FUNTION !!
def issue():
    issue1=Tk()
    subject_l=Label(issue1,text="ENTER SUBJECT NAME ",bg="cyan",fg="black",font="lucida 12 bold").place(x=10,y=50)
    subject_e=Entry(issue1,font="lucida 16 bold")
    subject_e.place(x=230,y=50)
    book_l=Label(issue1,text="ENTER BOOK NAME ",bg="cyan",fg="black",font="lucida 12 bold").place(x=10,y=150)
    book_e=Entry(issue1,font="lucida 16 bold")
    book_e.place(x=230,y=150)
    issue1.config(bg="yellow")
    issue1.geometry("500x300")
    

    
    def main():
        issue1_tk=Tk()
        e_t=Text(issue1_tk,font="lucida 10 bold")
        e_t.place(x=0,y=0,height=100,width=300)
        issue1_tk.geometry("300x100")
        issue1_tk.config(bg="cyan")
        issue1_tk.title("ISSUE BOOK")
        if subject_e.get()=="english":
            if book_e.get() in english:
                i="issued"
                e_t.insert(END,i)
        elif subject_e.get()=="hindi":
            if book_e.get() in hindi:
                i="issued"
                e_t.insert(END,i)
    
        elif subject_e.get()=="science":
            if book_e.get() in science:
                i="issued"
                e_t.insert(END,i)
        
        elif subject_e.get()=="maths":
            if book_e.get() in maths:
                i="issued"
                e_t.insert(END,i)

        elif subject_e.get()=="python":
            if book_e.get() in python:
                i="issued"
                e_t.insert(END,i)
        
        elif subject_e.get()=="c":
            if book_e.get() in c:
                i="issued"
                e_t.insert(END,i)
        else:
            a="Sorry Either You Have entered wrong OR book isn't Available !!"
            e_t.insert(END,a)
        
        for i in range(4):
            rand_num=random.randint(1000,10000)
            rand_num=str(rand_num)
        pin="\n\n"+"PIN :- "+rand_num
        e_t.insert(END,pin)
        wr=open("library","a")
        write_1=name_e.get()+"\t\t"+class_e.get()+" ISSUED \t"+"Book \t\t"+subject_e.get() +"\t\t"+ book_e.get()+"\t\t"+"       **>> DATE "+dt+"    PIN "+rand_num+"\n"
        wr.write(write_1)
        issue1_tk.mainloop()
    enter_button=Button(issue1,text="SUBMIT",bg="white",fg="black",font="lucida 10 bold",borderwidth=8,command=main).place(x=100,y=250)
    issue1.mainloop()
      
#Retun Function !!
def vaapis():
    return1=Tk()
    subject_l=Label(return1,text="Which Book you Want To Return",bg="white",fg="black",font="lucida 10 bold")
    subject_l.place(x=40,y=10)
    book_e=Entry(return1,text="lucida 10 bold")
    book_e.place(x=80,y=50)
    rand=Label(return1,text="Enter Pin",bg="white",fg="black",font="lucida 10 bold")
    rand.place(x=10,y=105)
    rand_e=Entry(return1,font="lucida 12 bold")
    rand_e.place(x=80,y=100,height=30,width=50)
    return1.config(bg="blue")
    return1.geometry("300x200")
    return1.title("Return")   
    def main():
        issue1_tk=Tk()
        e=Text(issue1_tk,font="lucida 10 bold")
        e.place(x=0,y=0,height=100,width=300)
        issue1_tk.geometry("300x100")
        issue1_tk.config(bg="cyan")
        issue1_tk.title("RETURN BOOK")
        returned_total="\n"+name_e.get()+"\t\t"+class_e.get()+"\t\tReturned  \t"+book_e.get()+"\t"+"On "+ dt
        f=open("library","r")
        lines=f.readlines()
        returned=open("Returned","a")
        old=open("library","w")
        for line in lines:
            if book_e.get() in line and name_e.get() in line and rand_e.get() in line:
                returned.write(returned_total)
                e.insert(END,"Returned !!")
            else:
                old.write(line)
    b=Button(return1,text='ENTER',bg="grey",fg="black",font="arial 8 bold",command=main).place(x=90,y=150)
    return1.mainloop()




#MAIN LABELLING !!


name_l=Label(win,text="Enter Name ",bg="cyan",fg="black",font="lucida 10 bold").place(x=10,y=10)
name_e=Entry(win,text="lucida 10 bold")
name_e.place(x=100,y=10)

class_l=Label(win,text="Enter Class ",bg="cyan",fg="black",font="lucida 10 bold").place(x=10,y=60)
class_e=Entry(win,text="lucida 12 bold")
class_e.place(x=100,y=60)

servicce_l=Label(win,text="SERVICES",bg="black",fg="white",font="arial 14 bold").place(x=150,y=130)

#1st service...
servicce_1=Label(win,text="1. ",bg="black",fg="white",font="arial 12 bold").place(x=10,y=180)
service_name1=Label(win,text="Book Issue",bg="black",fg="white",font="lucida 10 bold").place(x=50,y=180)
b_1=Button(win,text="Press",bg="red",fg="white",font="lucida 10 bold",command=issue).place(x=300,y=180)

#2nd service...
service_name2=Label(win,text="Book Return ",bg="black",fg="white",font="lucida 10 bold").place(x=50,y=230)
servicce_2=Label(win,text="2. ",bg="black",fg="white",font="arial 12 bold").place(x=10,y=230)
b_2=Button(win,text="Press",bg="red",fg="white",font="lucida 10 bold",command=vaapis).place(x=300,y=230)

#3rd service...
service_name3=Label(win,text="Book Category",bg="black",fg="white",font="lucida 10 bold").place(x=50,y=280)
servicce_3=Label(win,text="3. ",bg="black",fg="white",font="arial 12 bold").place(x=10,y=280)
b_3=Button(win,text="Press",bg="red",fg="white",font="lucida 10 bold",command=bookscategory).place(x=300,y=280)

#4th service...
service_name4=Label(win,text="Book List",bg="black",fg="white",font="lucida 10 bold").place(x=50,y=330)
servicce_4=Label(win,text="4. ",bg="black",fg="white",font="arial 12 bold").place(x=10,y=330)
b_4=Button(win,text="Press",bg="red",fg="white",font="lucida 10 bold",command=booklist).place(x=300,y=330)

#5th service...
service_name5=Label(win,text="Exit",bg="black",fg="white",font="lucida 10 bold").place(x=50,y=380)
servicce_5=Label(win,text="5. ",bg="black",fg="white",font="arial 12 bold").place(x=10,y=380)
b_4=Button(win,text="Press",bg="red",fg="white",font="lucida 10 bold",command=quit).place(x=300,y=380)

#Putting image in Title!!
pic=PhotoImage(file="zpython.png")
win.iconphoto(False,pic)
win.config(bg="black")
win.title("Library Managment System")
win.geometry("400x450")
win.mainloop()