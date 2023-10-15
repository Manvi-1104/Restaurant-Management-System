import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()
var1=tk.IntVar()


window.title("Payment")
window['background']='White'


lbl1 = tk.Label(window, text="Billing Invoice",font=("Arial",20),background="light Green",justify=tk.RIGHT)
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
lbl1.grid(column=5,row=5)
lbl1 = tk.Label(window, text="Bill Amount",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=6)
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
    
    billNo=field1.get()
    Name=field2.get()
    date=field3.get()
    
    command1=mycursor.execute("SELECT * FROM billing")
    command2=mycursor.fetchall()
    """
    for i in range(len(command2)):
        
        if str(command2[i][0])==:
            label1=tk.Label(window, text="Room already exists. Please try again.")
            label1.grid(column=0, row=5)
            break
   
        else:
            if roomtype=="" or rate=="" or num=="":
                label2=tk.Label(window, text="Please enter all fields.")
                label2.grid(column=0, row=4)
            
            elif roomtype!="" and rate!="" and rate.isdigit():
                string1="INSERT INTO room_master VALUES (%s, %s, %s)"
                val=(num, roomtype, rate)
                mycursor.execute(string1, val)
                label3=tk.Label(window, text="Data has been successfully added.")
                label3.grid(column=0, row=4)
                mydb.commit()
                break
            
            elif num.isdigit() is False:
                label5=tk.Label(window, text="Please enter a numeral value for the room number.")
                label5.grid(column=0, row=4)
                
            else:
                label4=tk.Label(window, text="Please enter a valid rate value.")
                label4.grid(column=0, row=4)"""

    for i in range(len(command2)):
            label1=tk.Label(window, text=command2[i][0], borderwidth=1, relief="solid")
            label1.grid(column=0, row=i+1)
            
            label2=tk.Label(window, text=command2[i][1], borderwidth=1, width=15, relief="solid")
            label2.grid(column=1, row=i+1)
            
            label3=tk.Label(window, text=command2[i][2], borderwidth=1, relief="solid")
            label3.grid(column=2, row=i+1)
        
        
                
    exit_button=tk.Button(window, text="Exit", command=window.destroy)
    exit_button.grid(column=0, row=len(command2)+2)               
"""enter_button=tk.Button(window, text="Enter", command=payment)
enter_button.grid(column=0, row=3)"""
        
        
mydb.commit()
            

window.mainloop()
