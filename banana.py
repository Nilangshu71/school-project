
from tkinter import *
import mysql.connector 
fan = mysql.connector.connect(host= "localhost",user = 'root1', passwd = 'root',database = 'school')
cursor= fan.cursor()
def submitact():
    userid = user.get()
    Name = name.get()
    password = passw.get()
    cursor.execute("insert into userdetails values(userid,Name,password)")
    savequery=cursor.execute('select * from userdetails')
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query Executed successfully")
    except:
        fan.rollback()
        print("Error occured")

window = Tk()

window.title('window 1')
window.geometry("900x600+10+20")
Label(window,text= 'WELCOME TO BASIC EVENT MANAGEMENT SERVICES').pack()
Label(window,text= 'FOR NEW USERS --V').pack()
Label(window,text= "Enter the USERID you want to use").pack()
user= Entry(window).pack()
Label(window,text= 'CAUTION: USERID MUST BE UNIQUE').pack()
Label(window,text= "Enter your NAME").pack()
name=Entry(window).pack()
Label(window,text= "Enter your password").pack()
passw= Entry(window).pack()
Label(window,text= 'please use a strong password').pack()
Button(window,text='ADD NEW USER',bg='blue',command=submitact).pack()
Label(window,text= "For Existing users--V").pack()
Label(window,text= "ENTER YOUR USERID").pack()
Entry(window,).pack()

window.mainloop()
