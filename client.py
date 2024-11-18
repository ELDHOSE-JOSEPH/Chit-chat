from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import ttk
import csv
import smtplib
import random
import pandas as pd
from functools import partial
import socket
import select
import errno
import math
import log
global na
global username
from socket import socket
global Lb1
c=0
x=0
m=0
button_identities = []

#
def writer(header, data, filename, option):
        with open (filename, "w", newline = "") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")
                
#recieve and store message
def receive():
    """Handles receiving of messages."""
    n=0
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            f=open("storage.csv",'a',newline='')      
            s=csv.writer(f)                            
            if n==1:
                a=msg
            if (n>1):
                c=msg
                Lb1.insert(END,c)
                l=[a,c]
                s.writerow(l)
            n=n+1             
            f.close()
            
        except OSError:  
            break

#sending messages
def send(event=None):  
    """Handles sending of messages."""
    msg = msgentry.get()
    msgentry.set("") 
    client_socket.send(bytes(msg, "utf8"))
    """Lb1.delete('0','end')
    insertlistboxsend()"""
    
#server close
def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


HOST = ''
PORT = 33000
if not PORT:
          PORT = 33000

else:
          PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
      
#graphics+display message        
def chat():     
    global f35
    global m
    global msg
    global msgentry    
    msgentry= StringVar()
    global msglist
    msglist= StringVar()
    global list1
    list1=[]
    global Lb1
    global searchentry
    searchentry = StringVar()
    
        

    if n==0:
        clearFrame(f1)
        
    if n==5:
        clearFrame(f6)
    if n==1:
        clearFrame(f3)
    
    f35=Frame(root,background="#22e6c5")
    f35.pack(side="top", expand=True, fill="both")    
    Button(f35,text="send",fg="#22e6c5",bg="black",width="8",height="1",font=("Kristen ITC",'8'),command=send).place(x=229,y=433)
    Button(f35,text=":",height="1",width="3",font=("Kristen ITC",'7'),bg="#22e6c5",fg="black",command=settings).place(x=265,y=7)
    Label(f35, text="Chit - Chat",fg="black",bg="#22e6c5",font=("Kristen ITC",'14')).place(x=10,y=3)
    f40=Frame(f35,width=320,bg="black",height=386).place(x=0,y=38)
    msg=Entry(f35, textvariable=msgentry, borderwidth="3",width="35")
    msg.place(x=5,y=435)
    global Lb1
    scrollbar = Scrollbar(f35, orient="vertical")
    Lb1= Listbox(f35, width=50, bg="black", yscrollcommand=scrollbar.set,fg="white",height=24)
    f=open("storage.csv",'r')
    s=csv.reader(f)
    for i in s:
            Lb1.insert(END, i[1])
    f.close()
    Lb1.insert(END, "Please enter your username before chatting")
    Lb1.place(x=0,y=38)
    scrollbar.config(command=Lb1.yview)
    scrollbar.pack(side="right", fill="y")
    m=20
     

#write user details
def signup_details():
    global x
    x=100
    global a
    global b
    global c
    global d
    global username
    f=open("chit - chat signup details.csv","a+",newline="")
    s_writer= csv.writer(f)
    Rec=[]
    a=name_entry.get()
    b=num_entry.get()
    c=username_entry.get()
    d=password_entry.get()
    Rec.append([a,b,c,d])
    for i in Rec:
        s_writer.writerow(i)
    f.close()
    
    if any(a)==False or any(b)==False or any(c)==False or any(d)==False:
        pass
    else:
        s=smtplib.SMTP("smtp.gmail.com", 25)
        s.starttls()
        s.login("chitchatcorperation@gmail.com","chitchat!@#")
        receiver=b
        message="Hi " + a +" We feel so happy and proud to welcome you as a member of the chit-chat community"
        s.sendmail("chitchatcorperation@gmail.com",receiver,message)
        chat()

#function to verify credentials of user    
def login_verification():
    global username
    username=username_login_entry.get()
   
    f=open("chit - chat signup details.csv","r")
    s_reader=csv.reader(f)
    for i in s_reader:
        if i[2]== username_login_entry.get():
            if i[3]==password_login_entry.get():
                chat()
            else:
                pass
        else:
            pass
    a=username_login_entry.get()
    b=password_login_entry.get()
    log.logged(a,b)
        
#send OTP via mail
def forget_pass():
    global c
    f=open("chit - chat signup details.csv","r")
    s_reader=csv.reader(f)
    for i in s_reader:
        c=random.randint(1000,9999)
        if i[0]== name_entry.get():
           if i[1]==username_entry.get():
               s=smtplib.SMTP("smtp.gmail.com", 25)
               s.starttls()
               s.login("chitchatcorperation@gmail.com","chitchat!@#")
               receiver=i[1]
               message="Hi " + i[0] +"Your OTP number is"+ str(c) +" please enter the OTP to change your password"
               s.sendmail("chitchatcorperation@gmail.com",receiver,message)
               OTP_generater()
           else:
               pass

#delete account
def delete_account():
    
    updatedlist=[]
    with open("chit - chat signup details.csv",newline="") as f:
      reader=csv.reader(f)
      username = username_entry.get()
      password = Password_entry.get() 
      
      for row in reader: 
            
                if row[2]!=username and row[3]!=password: 
                    updatedlist.append(row) 
      updatefile(updatedlist)

root = Tk()
root.geometry("320x470")
root.resizable(False,False)
root.title("chit - chat")
root.configure(bg='black')


f1=Frame(root,background="black")
f1.pack(side="top", expand=True, fill="both")

global n
n=0

#clear each frame
def clearFrame(a):
    for widget in a.winfo_children():
       widget.destroy()


    a.pack_forget()
    a.grid_forget()

#verify otp
def Forget_pass_chg_pass():
        
    if str(c) == otpentry.get():             
        forget_chg_password()
        
    else:
        pass

#change password while login        
def updatepassword():
        f=open("chit - chat signup details.csv",'r')
        s=csv.reader(f)
        a=name_entry.get()
        b=username_entry.get()
        d=newpassword_entry.get()
        l=[]
        for i in s:
                if i[0]==a:
                        if i[2]==b:
                                l.append([i[0],i[1],i[2],d])
                else:
                        l.append(i)
        f.close()
        f=open("chit - chat signup details.csv",'w',newline='')
        d=csv.writer(f)
        d.writerows(l)
        f.close()
        login()

#change password at settings
def updatepassword1():
        f=open("chit - chat signup details.csv",'r')
        s=csv.reader(f)
        a=name_entry.get()
        b=password_entry.get()
        d=newpassword_entry.get()
        l=[]
        for i in s:
                if i[0]==a:
                        if i[3]==b:
                                l.append([i[0],i[1],i[2],d])
                else:
                        l.append(i)
        f.close()
        f=open("chit - chat signup details.csv",'w',newline='')
        d=csv.writer(f)
        d.writerows(l)
        f.close()

#change username at settings     
def updateusername():
        f=open("chit - chat signup details.csv",'r')
        s=csv.reader(f)
        a=name_entry.get()
        b=username_entry.get()
        c=newusername_entry.get()
        l=[]
        for i in s:
                if i[0]==a:
                        if i[2]==b:
                                l.append([i[0],i[1],c,i[3]])
                else:
                        l.append(i)
        f.close()
        f=open("chit - chat signup details.csv",'w',newline='')
        d=csv.writer(f)
        d.writerows(l)
        f.close()

#otp entry page  
def OTP_generater():
    global f13
    global n

    n=13
    
    clearFrame(f4)

    
    f13=Frame(root,background="black")
    f13.pack(side="top", expand=True, fill="both")
    if n==15:
        clearFrame(f15)
        
    
    global newpassword_entry
    global otpentry
    global otpentry1
    global password_entry
    global na1

    otpentry1= StringVar()
    
    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f13,image=render,bg="black")
    img.image=render
    img.place(x=60,y=90)
    middleframe = Frame(f13,width="260",height="120",bg="#22e6c5",)
    middleframe.place(x=30,y=215)
    
  
    Label(f13,text="Forget Password",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Button(f13,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=forget_password).place(x=0,y=0)
    Label(f13, text="An OTP has been sent to your Email", fg="white", bg="black",font=("Kristen ITC", '8')).place(x=60, y=190)
    Label(middleframe,text="Enter OTP",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=58,y=10)
    otpentry = Entry(middleframe, textvariable=otpentry1, borderwidth=3, width=33)
    otpentry.place(x=26,y=43)
    Button(middleframe,text="Change Password",width="32",fg="#22e6c5",bg="black",font=("Kristen ITC",'8'),command=Forget_pass_chg_pass).place(x=13,y=80)
    
#graphics new password at login    
def forget_chg_password():
    global f15
    global n
    global newpassword_entry
    global name_entry
    global username_entry
    global username_entry1
    global newpassword_entry
    global name_entry9
    username_entry1 = StringVar()
    newpassword_entry1 = StringVar()
    name_entry9 = StringVar()
    n=15

    
    
    clearFrame(f13)
        
        

    f15=Frame(root,background="black")
    f15.pack(side="top", expand=True, fill="both")

    
    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f15,image=render,bg="black")
    img.image=render
    img.place(x=60,y=90)
    middleframe = Frame(f15,width="260",height="250",bg="#22e6c5",)
    middleframe.place(x=30,y=195)
    Label(f15,text="Change Password",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Label(middleframe,text="Enter Full Name :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=12,y=17)
    name_entry = Entry(middleframe, textvariable=name_entry9, borderwidth=3, width=33)
    name_entry.place(x=25,y=50)
    Label(middleframe,text="Current Username :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=16,y=80)
    username_entry = Entry(middleframe, textvariable=username_entry1, borderwidth=3, width=33)
    username_entry.place(x=25,y=110)
    Label(middleframe,text="New Password :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=5,y=140)
    newpassword_entry = Entry(middleframe, textvariable=newpassword_entry1, borderwidth=3, width=33)
    newpassword_entry.place(x=25,y=170)
    Button(middleframe,text="Change Password",width="33",fg="#22e6c5",bg="black",font=("Kristen ITC",'8'),command=updatepassword).place(x=10,y=210)
  
#graphics for delete acoount
def delete():
    global f12
    global n
    global username_entry1
    global newpassword_entry
    
    username_entry1 = StringVar()
    newpassword_entry1 = StringVar()
   
    n=7
    
    clearFrame(f6)

    
    f12=Frame(root,background="black")
    f12.pack(side="top", expand=True, fill="both")

    global username_entry
    global Password_entry

    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f12,image=render,bg="black")
    img.image=render
    img.place(x=60,y=50)
    middleframe = Frame(f12,width="240",height="150",bg="#22e6c5",)
    middleframe.place(x=40,y=285)
    Label(f12,text="Delete Account",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Button(f12,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=settings).place(x=0,y=0)
    Label(f12,text="Hi",height="2",width="10",fg="white",bg="black",font=("Kristen ITC",'7')).place(x=20,y=160)
    Label(f12,text="We are sorry to hear that you would like to delete.",height="1",width="38",fg="white",bg="black",font=("Kristen ITC",'7')).place(x=40,y=195)
    Label(f12,text="your account.If you want to delete your account ",height="1",width="36",fg="white",bg="black",font=("Kristen ITC",'7')).place(x=45,y=225)
    Label(f12,text="please enter the details below.",height="1",width="36",fg="white",bg="black",font=("Kristen ITC",'7')).place(x=45,y=255)
    Label(middleframe,text="Username ",height="1",width="10",font=("Kristen ITC",'8'),bg="#22e6c5",fg="black").place(x=10,y=15)
    username_entry = Entry(middleframe,textvariable=username_entry1,borderwidth="3",width="33")
    username_entry.place(x=17,y=33)
    Label(middleframe,text="Password ",height="1",width="10",font=("Kristen ITC",'8'),bg="#22e6c5",fg="black").place(x=10,y=60)
    Password_entry = Entry(middleframe,textvariable=newpassword_entry1, borderwidth="3",width="33")
    Password_entry.place(x=17,y=77)
    Button(middleframe,text="Delete Account",width="18",height="1",font=("Kristen ITC",'8'),fg="#22e6c5",bg="black",command=delete_account).place(x=50,y=110)


#graphics for change password at settings
def chg_password():
    global f9
    global n

    n=9
    
    clearFrame(f6)

   
    f9=Frame(root,background="black")
    f9.pack(side="top", expand=True, fill="both")

    global newpassword_entry
    global name_entry
    global password_entry
    global nameu1
    global password1
    global newpassword1
    nameu1 = StringVar()
    password1 = StringVar()
    newpassword1 = StringVar()
    


    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f9,image=render,bg="black")
    img.image=render
    img.place(x=60,y=90)
    middleframe = Frame(f9,width="260",height="250",bg="#22e6c5",)
    middleframe.place(x=30,y=195)
    Label(f9,text="Change Password",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Button(f9,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=settings).place(x=0,y=0)
    Label(middleframe,text="Enter Full Name :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=12,y=17)
    name_entry = Entry(middleframe,textvariable=nameu1, borderwidth="3",width="33")
    name_entry.place(x=25,y=50)
    Label(middleframe,text="Current Password :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=16,y=80)
    password_entry = Entry(middleframe,textvariable=password1, borderwidth="3",width="33")
    password_entry.place(x=25,y=110)
    Label(middleframe,text="New Password :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=5,y=140)
    newpassword_entry = Entry(middleframe,textvariable=newpassword1, borderwidth="3",width="33")
    newpassword_entry.place(x=25,y=170)
    Button(middleframe,text="Change Password",width="33",fg="#22e6c5",bg="black",font=("Kristen ITC",'8'),command=updatepassword1).place(x=10,y=210)

#graphics for change username at settings
def chg_username():
    global f8
    global n

    n=8
    
    clearFrame(f6)

    
    f8=Frame(root,background="black")
    f8.pack(side="top", expand=True, fill="both")

    
    global newusername_entry
    global name_entry
    global username_entry
    global nameu
    global usernameu
    global newusernameu
    nameu = StringVar()
    usernameu = StringVar()
    newusernameu = StringVar()
    
    
    middleframe = Frame(f8,width="260",height="250",bg="#22e6c5",)
    middleframe.place(x=30,y=195)
    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f8,image=render,bg="black")
    img.image=render
    img.place(x=60,y=90)
    Label(f8,text="Change Username",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Button(f8,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=settings).place(x=0,y=0)
    Label(middleframe,text="Enter Full Name :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=12,y=17)
    name_entry = Entry(middleframe,textvariable=nameu, borderwidth="3",width="33")
    name_entry.place(x=25,y=50)
    Label(middleframe,text="Current Username :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=16,y=80)
    username_entry = Entry(middleframe, textvariable=usernameu, borderwidth="3",width="33")
    username_entry.place(x=25,y=110)
    Label(middleframe,text="New Username :",height="2",width="15",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=5,y=140)
    newusername_entry = Entry(middleframe,textvariable=newusernameu, borderwidth="3",width="33")
    newusername_entry.place(x=25,y=170)
    Button(middleframe,text="Change Username",width="33",fg="#22e6c5",bg="black",font=("Kristen ITC",'8'),command=updateusername).place(x=10,y=210)

#logout
def logout():
        global n
        n=20
        f=open("login.csv",'w',newline='')
        login()

#to clear chatting screen
def clearchat():
        f=open("storage.csv",'w',newline='')


#graphics for settings
def settings():
    global f6
    global n
    global m
    if n==0:
        clearFrame(f1)
    if n==8:
        clearFrame(f8)
    if n==6:
        clearFrame(f2)
    if n==0:
        clearFrame(f1)
    if n==0:
        clearFrame(f1)
    if n==12:
        clearFrame(f7)
    if n==9:
        clearFrame(f9)
    if n==10:
        clearFrame(f10)
    if n==11:
        clearFrame(f11)
    if n==7:
        clearFrame(f12)
    if m==20:
        clearFrame(f35)         
    
    n=5
    f6=Frame(root,background="black")
    f6.pack(side="top", expand=True, fill="both")
    Label(f6,text="General Settings",height="2",width="35",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black").place(x=0,y=0)
    Button(f6,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=chat).place(x=0,y=0)
    Button(f6,text="Change Username",width="30",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black",command=chg_username).place(x=20,y=110)
    Button(f6,text="Change Password",width="30",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black",command=chg_password).place(x=20,y=170)
    Button(f6,text="Clear Chat",width="30",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black",command=clearchat).place(x=20,y=230)
    Button(f6,text="Delete Account",width="30",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black",command=delete).place(x=20,y=290) 
    Button(f6,text="log out",width="30",font=("Kristen ITC",'10'),bg="#22e6c5",fg="black",command=logout).place(x=20,y=350)
    
#graphics for forget password at login
def forget_password():
    global name
    global username
    global name_entry
    global username_entry
    global n
    global f4

    if n==0:
        clearFrame(f1)
    if n==13:
        clearFrame(f13)
    n=2
    
    f4=Frame(root,background="black")
    f4.pack(side="top", expand=True, fill="both")
    
    name=StringVar()
    username=StringVar()

    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f4,image=render,bg="black")
    img.image=render
    img.place(x=60,y=90)
    middleframe = Frame(f4,width="220",height="200",bg="#22e6c5",)
    middleframe.place(x=50,y=225)
    Label(f4,text="Forgot password",fg="black",bg="#22e6c5",font=("Kristen ITC",'10'),width="36",height="2").place(x=0,y=0)
    Button(f4,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=login).place(x=0,y=0)
    Label(f4,text="Enter the following details to retreive your password",fg="white",bg="black",font=("Kristen ITC","8")).place(x=13,y=210)
    name=Label(middleframe,text="Enter your full name",bg="#22e6c5",fg="black",font=("Kristen ITC",'10'))
    name.place(x=15,y=25)
    name_entry = Entry(middleframe, textvariable=name,width=30,borderwidth=3)
    name_entry.place(x=15,y=45)
    username_lable = Label(middleframe, text="Enter your Email ID",bg="#22e6c5",fg="black",font=("Kristen ITC",'10'))
    username_lable.place(x=15,y= 75)
    username_entry = Entry(middleframe, textvariable=username,width=30,borderwidth=3)
    username_entry.place(x=15,y=95)
    Button(middleframe, text="Generate OTP", height="1", width="26",fg="#22e6c5",font=("Kristen ITC",'8'),bg="black", command=forget_pass).place(x=14,y=145)
    

#graphics for signup page
def signup_screen():
    global name
    global num
    global username
    global password
    global name_entry
    global num_entry
    global username_entry
    global password_entry
    global n
    global f3
    clearFrame(f1)
    n=1
    f3=Frame(root,background="black")
    f3.pack(side="top", expand=True, fill="both")
    name = StringVar()
    num = StringVar()
    username = StringVar()
    password = StringVar()


    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(f3,image=render,bg="black")
    img.image=render
    img.place(x=60,y=50)
    middleframe = Frame(f3,width="220",height="250",bg="#22e6c5",)
    middleframe.place(x=50,y=195)
    Label(f3,text="Sign up", bg="#22e6c5", width="36", height="2",fg="black", font=("Kristen ITC", '10')).place(x=0,y=0)
    Button(f3,text="back",bg="#22e6c5",width="8",height="2",fg="black", font=("Kristen ITC",'8'),command=login).place(x=0,y=0)
    Label(f3, text="Sign up to chit - chat with your friends ", fg="white", bg="black",font=("Kristen ITC", '8')).place(x=52, y=170)
    name = Label(middleframe, text="Full Name", bg="#22e6c5", fg="black", font=("Kristen ITC", '8'))
    name.place(x=15, y=10)
    name_entry = Entry(middleframe, textvariable=name, width=30, borderwidth=3)
    name_entry.place(x=15, y=30)
    num = Label(middleframe, text="Enter your Email id", bg="#22e6c5", fg="black", font=("Kristen ITC", '8'))
    num.place(x=15, y=55)
    num_entry = Entry(middleframe, textvariable=num, width=30, borderwidth=3)
    num_entry.place(x=15, y=75)
    username_lable = Label(middleframe, text="Username", bg="#22e6c5", fg="black", font=("Kristen ITC", '8'))
    username_lable.place(x=15, y=100)
    username_entry = Entry(middleframe, textvariable=username, width=30, borderwidth=3)
    username_entry.place(x=15, y=120)
    password_lable = Label(middleframe, text="Password", bg="#22e6c5", fg="black", font=("Kristen ITC", '8'))
    password_lable.place(x=15, y=145)
    password_entry = Entry(middleframe, textvariable=password, show='*', width=30, borderwidth=3)
    password_entry.place(x=15, y=165)
    Button(middleframe, text="Sign up", width=10, height=1, fg="#22e6c5", bg="black", font=("Kristen ITC", '8'),command=signup_details).place(x=70, y=210)

#graphics for login page
def login():
    global n
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    global username

    if n==1:
        clearFrame(f3)
    if n==2:
        clearFrame(f4)
    if n==11:
        clearFrame(f11)
    if n==7:
        clearFrame(f12)
    if n==15:
        clearFrame(f15)
    if n==20:
        clearFrame(f6)

    load=Image.open("onlinelogomaker-083020-0857-7485-2000-transparent.png")
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render,bg="black")
    img.image=render
    img.place(x=60,y=50)

    username_verify = StringVar()
    password_verify = StringVar()

    Label(root, text="Login", font=("Kristen ITC", '10'),bg ="#22e6c5",fg="black",width="35",height="2").place(x=0, y=0)

    middleframe = Frame(root,width="208",height="200",bg="#22e6c5",)
    middleframe.place(x=55,y=170)
    
    Label(middleframe, text="Username", fg="black", bg="#22e6c5", font=("Kristen ITC", '8')).place(x=10, y=13)
    username_login_entry = Entry(middleframe, textvariable=username_verify, width=30, borderwidth=3)
    username_login_entry.place(x=10, y=33)
    
    Label(middleframe, text="Password", fg="black", bg="#22e6c5", font=("Kristen ITC", '8')).place(x=10, y=63)
    password_login_entry = Entry(middleframe, textvariable=password_verify, show='*', width=30, borderwidth=3)
    password_login_entry.place(x=10, y=83)

    Button(middleframe, text="Login", width=8, font=("Kristen ITC", '8'), height=1, fg="#22e6c5", bg="black",command=login_verification).place(x=70, y=120)

    Button(middleframe, text="forgot password ?", height="1", width="26", fg="#22e6c5", font=("Kristen ITC", '8'),bg="black", command=forget_password).place(x=8, y=155)
    bottomframe = Frame(root,width="320",height="100",bg="#22e6c5",)
    bottomframe.place(x=0,y=405)
    Label(bottomframe, text="Create new account", fg="black", bg="#22e6c5", width="20",font=("Kristen ITC",'10') ).place(x=30, y=16)
    Button(bottomframe, text="sign up", width=9, font=("Kristen ITC", '8'), height=1, fg="#22e6c5", bg="black",command=signup_screen).place(x=198, y=16)

    n=0

#tto check if user is logged in
y=log.log_check()
if y=='Yes':
    chat()
else:
    login()
root.mainloop()
