import pymysql
from tkinter import messagebox
import re
from tkinter import *
import fetchtable as ft
import menu


def validate_inputs():
    user=name.get()
    passw=pass1.get()   

    if  (re.search("[0-9]",user)):
        messagebox.showerror("error","username should not have digit ")
    if not (re.search("[A-Z]",passw) and re.search("[a-z]",passw) and re.search("[0-9]",passw)):
        messagebox.showerror("error","password should contain at least one capital and small letter and one digit ")


    
    
def Sign_in():
    password=pass1.get()
    re_password=pass2.get()
    username=name.get()
    validate_inputs()
    if password=="":
        y.set("PLEASE ENETR PASSWORD")
        confirmation.config(text=y,fg="orange")
        
    elif(password==re_password):
        
        
        user=name.get()
        passw=pass1.get()


        # enter into table in database 
        loginerror(user,passw)

       

       # myconn=pymysql.connect(host="localhost",user="root",passwd="cha&@#12",database="login",charset="utf8",port=3306)
        #cursor=myconn.cursor()
        #cursor.execute("create table entries(sr_no int primary key auto_increment,username varchar(20),password varchar(15))")
        #cursor.execute("insert into entries values(null,'"+user+"','"+passw+"')")
        #myconn.commit()'''
        
    else:
        y.set(name.get()+"'s Password doesn't match")
        confirmation.config(text=y,fg="red")
        
    
    
def Login():
    password=pass1.get()
    re_password=pass2.get()
    validate_inputs()
    if password=="":

        messagebox.showinfo("info","PLEASE ENETR PASSWORD")
        #confirmation.config(text=y,fg="orange")
        
    elif(password==re_password):
        
        y.set(name.get()+"'s password Success")
        confirmation.config(text=y,fg="green")
        user=name.get()
        passw=pass1.get()
        print(f"The name entered by you is {user}")
        logintodb(user,passw)
        
        menu.open_restaurent()
        
        
        

    
        
    else:
        y.set(name.get()+"'s Password doesn't match")
        confirmation.config(text=y,fg="red")
        

def logintodb(user,passw):

    if passw:
        myconn=pymysql.connect(host="localhost",user="root",passwd="cha&@#12",database="login",charset="utf8",port=3306)
        cursor=myconn.cursor()

        entry=cursor.execute("select * from entries where username='"+user+"' and password='"+passw+"'")
        if entry :
           cursor.execute("select * from entries")
           for x in cursor:
                print(x)
           myconn.commit()

           name.delete(0,END)
           pass1.delete(0,END)
           pass2.delete(0,END)

           ft.display_data()

        else:
            messagebox.showerror("error"," sorry you don'nt have access\n please sign in  ")

def loginerror(user, passw):
    myconn=pymysql.connect(host="localhost",user="root",passwd="cha&@#12",database="login",charset="utf8",port=3306)
    cursor=myconn.cursor()

    entry=cursor.execute("select * from entries where username='"+user+"' and password='"+passw+"'")
    if entry:
        messagebox.showwarning("warning","you have aleready sign in ")
    else:
        cursor.execute("insert into entries values(null,'"+user+"','"+passw+"')")
        y.set(name.get()+"'s password Success \n sign-in successfully")
        confirmation.config(text=y,fg="green")
        myconn.commit()
    
    

top = Tk()
top.title("Password Changing Form")
top.geometry("300x400")


frame = Frame(top, bg="#f9a603", bd=5, relief="ridge")  
frame.place(x=0, y=0, width=420, height=550)

x=StringVar()
x.set("xyz")
y=StringVar()

# Labels and Entry Fields
Label(frame, text="Enter Username:",bg="#f9a603",  fg="white", font=("Arial", 10, "bold")).place(x=30, y=20)
name = Entry(frame, textvariable=x, bd=3, relief="solid", bg="#ffcccc", fg="black")
name.place(x=150, y=20)

Label(frame, text="Enter Password:",bg="#f9a603",  fg="white", font=("Arial", 10, "bold")).place(x=30, y=70)
pass1 = Entry(frame, bd=3, relief="groove", bg="#ffdddd", fg="black")
pass1.place(x=150, y=70)

Label(frame, text="Re-type Password:",bg="#f9a603",  fg="white", font=("Arial", 10, "bold")).place(x=30, y=120)
pass2 = Entry(frame, bd=3, relief="groove", bg="#ffdddd", fg="black")
pass2.place(x=150, y=120)

# Buttons
login = Button(frame, text="Login", command=Login, bg="#DC143C", fg="white", font=("Helvetica", 12, "bold"), relief="flat", cursor="hand2")
login.place(x=80, y=180)
login.bind("<Enter>", lambda e: login.config(bg="#ff6347"))
login.bind("<Leave>", lambda e: login.config(bg="#ff4500"))

sign_in = Button(frame, text="Sign-in", command=Sign_in, bg="#DC143C", fg="white", font=("Helvetica", 12, "bold"), relief="flat", cursor="hand2")
sign_in.place(x=180, y=180)
sign_in.bind("<Enter>", lambda e: sign_in.config(bg="#ff6347"))
sign_in.bind("<Leave>", lambda e: sign_in.config(bg="#ff4500"))

# Confirmation Message
confirmation = Label(frame, textvariable=y,bg="#f9a603", fg="white", font=("Helvetica", 14, "bold"))
confirmation.place(x=30, y=250, width=350)

top.mainloop()
