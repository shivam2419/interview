from tkinter import messagebox
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image



def mains():

    t5=Tk()
    t5=Toplevel()
    image=Image.open("zbuggati.png")
    newimg=image.resize((80,80))
    img6=ImageTk.PhotoImage(newimg)


    l=Label(t5,image=img6,borderwidth=3)
    l.place(x=10,y=10)

    Label(t5,text="0      100M       0",bg="black",fg="white",font="Lucia 18 bold").place(x=150,y=30)
    Label(t5,text="Posts     Followers      Following",bg="black",fg="white",font="Lucida 12 bold").place(x=140,y=60)

    ppname=username.get()
    Label(t5,text=ppname,bg="black",fg="white",font="arial 12 bold").place(x=10,y=120)


    txt="Write your own bio !!"
    Label(t5,text=txt,bg="black",fg="white",font="arial 10 ").place(x=10,y=150)

    b=Button(t5,text="Edit Profile",bg="grey",fg="white",border=0,font="arial 8 bold").place(x=10,y=200,height=20,width=380)


    #story thing...
    img=PhotoImage(file="zplus1.png")
    photoimage = img.subsample(2, 2)
    story=Button(t5,image=photoimage,bg="black").place(x=10,y=230)

    Label(t5,text="_______________________________________________________________________________",bg="black",fg="white").place(x=0,y=260)
    img1=PhotoImage(file="zgrid.png")
    story=Button(t5,image=img1,bg="black").place(x=60,y=300)

    img2=PhotoImage(file="zreel.png")
    story=Button(t5,image=img2,bg="black").place(x=180,y=300)

    img3=PhotoImage(file="ztag.png")
    story=Button(t5,image=img3,bg="black").place(x=300,y=300)

    t5.config(bg="black")
    t5.geometry("400x500")
    t5.mainloop()



t=Tk()
n=StringVar()
# t.iconbitmap("zpython.png")
#Instagram label !!
Label(t,text="Instagram",fon="forte 28 bold",bg="black",fg="white").place(x=100,y=150)




#Sign Up !!!!!

def sign_up():
    t1=Tk()

    Label(t1,text="Choose username",font="Calibri 22 bold",bg="black",fg="white").place(x=40,y=10)
    Label(t1,text="You can always change it later.",font="Calibri 10 bold",bg="black",fg="lightgrey").place(x=65,y=50)

    ee=Entry(t1,bg="dimgrey",fg="white",font="clibri 12 ",border=0)
    ee.place(x=20,y=100,height=40,width=260)
    ee.insert(0,"Username")

    def Next():
        conn=mysql.connector.connect(user="root",password="root@shivam2419",database="insta")
        cur=conn.cursor()
        cur.execute("Select name from info")
        str_ee=ee.get()
        tup_ee=tuple(str_ee.split(","))
        lst=[]
        for i in cur:
            lst.append(i) 
        if tup_ee in lst:
            messagebox.showinfo("!!","Username already exists..")
        else:
            t2=Tk()
            Label(t2,text="Create a password",font="Calibri 22 bold",bg="black",fg="white").place(x=40,y=10)
            Label(t2,text="For security,your password must\nbe 6 characters or more.",font="Calibri 10 bold",bg="black",fg="lightgrey").place(x=65,y=50)

            e1=Entry(t2,bg="dimgrey",fg="white",font="clibri 12 ",border=0)
            e1.place(x=20,y=100,height=40,width=260)
            e1.insert(0,"Password")
        


            def Next1():

                if len(e1.get())<7:
                    messagebox.showerror("!!","Password length must be more than 6")
                else:
                    t3=Tk()
                    txt="Welcome to Instagram\n"+ee.get()
                    Label(t3,text=txt,bg="black",fg="white",font="calibri 22 ").place (x=20,y=1)
                    Label(t3,text="We'll add the email and phone number \nfrom your account from the setting .You can \nupdate this info anytime in settings or\nenter new info now",fg="lightgray",bg="black").place(x=25,y=72)
                    
                    def execution():
                        conn=mysql.connector.connect(user="root",password="root@shivam2419",database="insta")
                        cur=conn.cursor()
                        query="Insert into info(Name,Password) VALUES('"+ee.get()+"','"+e1.get()+"')"
                        cur.execute(query)
                        cur.execute("commit")

                        txt=ee.get()+" Your account created successfully !!"
                        messagebox.showinfo("Account created",txt)
                        mains()

                        cur.close()
                        conn.close()
                #-----------------------------
                    def email():
                        ema=Entry(t3,bg="grey",fg="white",font="arial 8 bold")
                        ema.place(x=20,y=220,height=30,width=260)
                        ema.insert(0,"Enter Email-Id")

                        def submit_email():
                            conn=mysql.connector.connect(user="root",password="root@shivam2419",database="insta")
                            cur=conn.cursor()
                            query="Insert into info(email) VALUES('"+ema.get()+"') where name='"+username.get()+"' and password='"+password.get()+"';"
                            cur.execute(query)
                            cur.execute("commit")

                            txt=ee.get()+" Your account created successfully !!"
                            messagebox.showinfo("Account created",txt)


                        bemail=Button(t3,text="SUBMIT",bg="blue",fg="white",font="arial 10 bold",command=submit_email).place(x=200,y=300)

                b=Button(t3,text="Continue sign up",bg="blue",fg="white",border=0,command=execution).place(x=20,y=150,height=30,width=260)
                b=Button(t3,text="Add new phone or email",bg="black",fg="blue",border=0,command=email).place(x=20,y=190,height=30,width=260)

                Label(t3,text="We'll add private info from settings.See",bg="black",fg="grey",font="calibri 10").place(x=30,y=350)
                b=Button(t3,text="Term data Policy",bg="black",fg="azure",border=0,font="calibri 10 ").place(x=40,y=370)
                Label(t3,text="and",bg="black",fg="grey",font="calibri 10").place(x=140,y=370)
                b=Button(t3,text="Cookie Policy.",bg="black",fg="azure",border=0,font="calibri 10 ").place(x=170,y=370)
                t3.geometry("300x400")
                t3.config(bg="black")

                
            b=Button(t2,text="Next",bg="blue",fg="white",border=0,command=Next1).place(x=20,y=150,height=30,width=260)

            t2.geometry("300x400")
            t2.config(bg="black")
            t2.mainloop()



    b=Button(t1,text="Next",bg="blue",fg="white",border=0,command=Next).place(x=20,y=150,height=30,width=260)

    t1.config(bg="black")
    t1.geometry("300x400")




#LOGIN   !!!!!

def login():
    
    conn=mysql.connector.connect(user="root",password="root@shivam2419",database="insta")
    cur=conn.cursor()
    query="SELECT * from info WHERE password='"+password.get()+"' AND name='"+username.get()+"';"
    cur.execute(query)
    for i in cur:
        if (password.get() in i) and (username.get() in i):
            mains()

        else:
            messagebox.showerror("Error","Username OR Password is incorrect !!")


    cur.close()
    conn.close()



#User name ...
username=Entry(t,font="calibri 12 ",bg="dimgrey",border=0,fg="whitesmoke")
username.place(x=55,y=240,height=40,width=270)
username.insert(0,"Username")

#password!!
password=Entry(t,font="calibri 12",bg="dimgrey",border=0,fg="whitesmoke",show="*")
password.place(x=55,y=290,height=40,width=270)
password.insert(0,"Password")

#Login Button...
b=Button(t,text="Login",bg="blue",fg="white",font="lucida 10 bold",activebackground="black",border=0,command=login).place(x=55,y=345,width=270,height=40)
#forget password button !!
b2=Button(t,text="forget your login details?",fg="grey",bg="black",font=" lucida 8 ",border=0,activebackground="black").place(x=80,y=395)
b2=Button(t,text="Get help loggin in.",fg="azure",bg="black",font=" lucida 8 ",border=0,activebackground="black").place(x=200,y=395)
#Seperator ...
Label(t,text="______________________________________",bg="black",fg="grey").place(x=0,y=425)
Label(t,text="OR",bg="black",fg="grey",font="Arial 10 bold").place(x=175,y=430)
Label(t,text="______________________________________",bg="black",fg="grey").place(x=200,y=425)
#facebook logiin Section...
b3=Button(t,text="Log in with Facebook",bg="black",fg="blue",font="Arial 11 bold",border=0,activebackground="black").place(x=105,y=465)
#Sign Up System...
b4=Button(t,text="Don't have an account?",fg="grey",bg="black",font=" lucida 8 ",border=0,activebackground="black",command=sign_up).place(x=105,y=575)
b5=Button(t,text="Sign up.",fg="azure",bg="black",font=" lucida 8 ",border=0,activebackground="black",command=sign_up).place(x=225,y=575)

t.config(bg="black")
t.geometry("390x600")
t.mainloop()