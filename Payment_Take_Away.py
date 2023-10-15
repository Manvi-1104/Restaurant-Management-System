import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()
var1=tk.IntVar()


window.title("Payment")
window['background']='White'


lbl1 = tk.Label(window, text="Billing Invoice",font=("Arial",35),background="light Green",justify=tk.RIGHT)
lbl1.grid(column=4,row=0)
lbl1 = tk.Label(window, text="Bill Number:",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=1)
lbl1 = tk.Label(window, text="Customer Name:",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=3)
lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=5)
lbl1 = tk.Label(window, text="Date",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=5,row=1)
lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=5,row=4)
lbl1 = tk.Label(window, text=" Toatl Bill Amount",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=6)
lbl1 = tk.Label(window, text="Packing Charges:20/-",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=5)
B1=tk.Button(window,text="Enter",command=select,background="White").grid(column=4,row=8)

field1=tk.Entry()
field1.grid(column=4, row=2)
field2=tk.Entry()
field2.grid(column=4, row=4)
field3=tk.Entry()
field3.grid(column=5, row=2)
import mysql.connector as sql

mydb=sql.connect(
    host="localhost",
    user="root",
    charset="utf8",
    passwd="110104",
    auth_plugin='mysql_native_password',
    database="evergreen_restaurant")
  
def Payment():
    name=field1.get()
        

            
    command1="SELECT billNo FROM billing WHERE customer_name=%s "
    name1=(Name,)
    execution1=mycursor.execute(command1, name1)
    billing=mycursor.fetchall()
    print(billing)
        
        
mydb.commit()
            

window.mainloop()
