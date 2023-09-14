from tkinter import*
from tkinter import messagebox
import mysql.connector
import qrcode
import pandas as pd
import smtplib, ssl
from PIL import ImageTk,Image
from pyqrcode import create
import pyqrcode
import tkinter as tk

root=Tk()
root.geometry("600x600")
root.title("BACKERY MANAGEMENT SYSTEM")

def view():
    top1 = Tk()
    top1.geometry("700x500")
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bakery"
    )

    my_conn = db.cursor()
    my_conn.execute("SELECT * FROM lists ")
    i = 0
    for details in my_conn:
        for j in range(len(details)):
            e = Entry(top1, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i = i+1
    db.commit()
    db.close()
    top1.mainloop()

def insert():
    a=s1.get()
    b=s2.get()
    c=s3.get()
    d=s4.get()
    e=s5.get()
    
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bakery")

    mycursor = mydb.cursor()
    sql="insert into lists(customer_id,price,stock,expiry_date,selling_record) values (%s,%s,%s,%s,%s)"
    val=(a,b,c,d,e)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Record","Insert Successfully..!!")

def update():
    root=Tk()
    root.geometry("400x400")
    root.title("UPDATE PAGE")
    def up():
        a=s1.get()
        b=s2.get()
        c=s3.get()
        d=s4.get()
        e=s5.get()
        
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bakery"
            )
        mycursor=mydb.cursor()
        sql="UPDATE lists SET price=%s,stock=%s,expiry_date=%s,selling_record=%s WHERE customer_id=%s"
        val=(a,b,c,d,e)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Record","update Successfully...!!")
        mydb.close()

    e1=IntVar()
    e2=StringVar()
    e3=StringVar()
    e4=StringVar()
    e5=StringVar()
   
    a1=Label(root,text="customer_id")
    a1.grid(row=0,column=0)
    
    e1=Entry(root)
    e1.grid(row=0,column=1)

    
    a2=Label(root,text="price")
    a2.grid(row=1,column=0)
    
    e2=Entry(root)
    e2.grid(row=1,column=1)
    
    a3=Label(root,text="stock")
    a3.grid(row=2,column=0)
    
    e3=Entry(root)
    e3.grid(row=2,column=1)
    
    a4=Label(root,text="expiry_date")
    a4.grid(row=3,column=0)
    
    e4=Entry(root)
    e4.grid(row=3,column=1)

    a5=Label(root,text="selling_record")
    a5.grid(row=4,column=0)
    
    e5=Entry(root)
    e5.grid(row=4,column=1)

    b11=Button(root,text="update",command=up)
    b11.grid(row=6,column=1)

    root.mainloop()
   
def delete():
    over=Tk()
    over.geometry("250x250")
    over.title("DELETE PAGE")

    def last():
        customer_id=h1.get()

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bakery"
            )
        mycursor=mydb.cursor()
        sql="DELETE FROM lists WHERE customer_id=%s"
        val=(customer_id)
        mycursor.execute(sql,(val,))
        mydb.commit()
        messagebox.showinfo("Record","delete Successfully...!!")
        mydb.close()

    h1=IntVar()
    
    j1=Label(over,text="customer_id", font=("arial", 12, "bold"))
    j1.grid(row=0,column=0)
    
    h1=Entry(over)
    h1.grid(row=0,column=1)

    b1=Button(over,text="delete",command=last)
    b1.grid(row=3,column=1)

    over.mainloop()
    
def task():
    
    customer_id=s1.get()
    price=s2.get()
    stock=s3.get()
    expiry_date=s4.get()
    selling_record=s5.get()

    qrdata=(f"customer_id:{customer_id}\n price:{price}\n stock:{stock}\n expiry_date:{expiry_date}\n selling_record:{selling_record}")
    qr_code=qrcode.make(qrdata)
    qr_code.save('image1.png')
    qr_code= qrcode.create(qrdata)
    qr_code.png("image1.png", scale = 8)
    qr_code.png('image1.png', scale = 6)
    
def csv():
    mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bakery"
            )
    mycursor=mydb.cursor()
    sql="select * FROM lists "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    all_customer_id=[]
    all_price=[]
    all_stock=[]
    all_expiry_date=[]
    all_selling_record=[]
    all_date=[]
    
    for customer_id,price,stock,expiry_date,selling_record,date in myresult:
        all_customer_id.append(customer_id)
        all_price.append(price)
        all_stock.append(stock)
        all_expiry_date.append(expiry_date)
        all_selling_record.append(selling_record)
        all_date.append(all_date)
    

    dic={'customer_id':all_customer_id,'price':all_price,'stock':all_stock,'expiry_date':all_expiry_date,'selling_record':all_selling_record,
         'all_date':all_date}
    df=pd.DataFrame(dic)
    df_csv=df.to_csv('D:/prajay(python)/bakery.csv',index=False)
    mydb.commit()
    messagebox.showinfo("Record","CSV FILE Generate Successfully...!!")
    mydb.close()
    
def email():
    sender_email = "sender@xyz.com"
    receiver_email = "receiver@xyz.com"
    message = """\
    Subject: It Worked!

    Simple Text email from your Python Script."""

    port = 465  
    app_password = input("Enter Password: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sender@xyz.com", app_password)
        server.sendmail(sender_email, receiver_email, message)

def gene():

    global my_image
    l1=Label(root)
    l1.grid(row=12,column=2)
    
    customer_id=s1.get()
    price=s2.get()
    stock=s3.get()
    expiry_date=s4.get()
    selling_record=s5.get()

    qrdata=pyqrcode.create(f"customer_id:{customer_id}\n  price:{price}\n stock:{stock}\n  expiry_date:{expiry_date}\n selling_record:{selling_record}")
    my1_qr=qrdata.xbm(scale=2)
    my_image=tk.BitmapImage(data=my1_qr)
    l1.config(image=my_image)
    


s1=IntVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

q1 = Label(root, text="CUSTOMER_ID:➾", font=("arial", 12, "bold"))
q1.grid(row=1, column=1)

s1 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s1.grid(row=1, column=2)

q2 = Label(root, text="PRICE:➾", font=("arial", 12, "bold"))
q2.grid(row=2, column=1)

s2 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s2.grid(row=2, column=2)

q3 = Label(root, text="STOCKS:➾", font=("arial", 12, "bold"))
q3.grid(row=3, column=1)

s3 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s3.grid(row=3, column=2)

q4 = Label(root, text="EXPIRY_DATE:➾", font=("arial", 12, "bold"))
q4.grid(row=4, column=1)

s4 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s4.grid(row=4, column=2)

q5 = Label(root, text="SELLING_RECORD:➾", font=("arial", 12, "bold"))
q5.grid(row=5, column=1)

s5 = Entry(root, font=("arial", 12, "bold"), bd=5, width=24)
s5.grid(row=5, column=2)

b1=Button(root,text="INSERT",command=insert,bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b1.grid(row=8,column=1)

b2=Button(root,text="UPDATE",command=update,bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b2.grid(row=9,column=1)

b3=Button(root,text="DELETE",command=delete,bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b3.grid(row=10,column=1)

b4=Button(root,text="CSV FILE",command=csv,bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b4.grid(row=8,column=2)

b4=Button(root,text="EMAIL",command=email,bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b4.grid(row=9,column=2)

b4=Button(root,text="PDF",bg="powder blue",bd=3,width=20,relief= RAISED,font=("Calibri", 10, "bold"))
b4.grid(row=10,column=2)

b5=Button(root,text= "QR Generator",width=20,relief= RAISED,bg="powder blue",fg="black",bd=3,font=("Calibri", 10, "bold"),command=gene)
b5.grid(row=11,column=2)

root.mainloop()