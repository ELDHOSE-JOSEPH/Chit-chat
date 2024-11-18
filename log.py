import csv
import os.path

def logged(a,b):
    '''
    a:entry.get from Login_username
    b:entry.get from Login_password
    '''
    f=open("login.csv",'w',newline='')
    s=csv.writer(f)
    s.writerow([a,b])
    f.close()

def log_check():
    if os.path.isfile("login.csv"):
        f=open("login.csv",'r')
        s=csv.reader(f)
        c=0
        for i in s:
            if any(i)==True:
                c=2
        if c==2:
            return("Yes")
        else:
            return("No")
        f.close()
    else:
        f=open("login.csv",'w',newline='')



