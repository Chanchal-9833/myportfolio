import pymysql
from tkinter import messagebox
import re
from tkinter import *
import fetchtable as ft

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
    
    

top=Tk()
top.title("Password changing form")
top.geometry("400x500")
top.configure(bg="lightblue") 
x=StringVar()
x.set("xyz")
y=StringVar()

label1=Label(top,text="Enter username:")
label1.place(x=100,y=100)

name=Entry(top,textvariable=x)
name.place(x=200,y=100)

label2=Label(top,text="Enter password:")
label2.place(x=100,y=150)

pass1=Entry(top)
pass1.place(x=200,y=150)

label3=Label(top,text="re-type password:")
label3.place(x=100,y=200)

pass2=Entry(top)
pass2.place(x=200,y=200)

login=Button(top,text="login",command=Login)
login.place(x=150,y=250)

sign_in=Button(top,text="Sign-in",command=Sign_in)
sign_in.place(x=200,y=250)

confirmation=Label(top,textvariable=y)
confirmation.place(x=120,y=300)
top.mainloop()
