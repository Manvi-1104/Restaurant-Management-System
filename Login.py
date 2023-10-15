import tkinter as tk
import csv
user_list=[]

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()

var1=tk.IntVar()

window.title("Welcome to Evergreen Restaurant")
window['background']='White'
    
with open("C:\\Users\\Intel\\Desktop\\LoginID.csv", "r") as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        user_list.append([row[0],row[1],row[2],row[3]])

print(user_list)
username_list=[]
password_list=[]
admin_list=[]
for i in range(len(user_list)):
    username_list.append(user_list[i][1])
    password_list.append(user_list[i][0])
    admin_list.append(user_list[i][2])


def check():
    count=0
    user=str(field1.get())
    pin=str(field2.get())
    
    for i in range(len(user_list)):
        if user==user_list[i][1]:
            count=1
            print(user)
            
            if(pin==user_list[i][0]):
                print(pin)
                if user_list[i][2]=="Admin" and user_list[i][3]=="Manager":
                    label1=tk.Label(window, text="Edit page and Menu access is granted.", font=("Arial", 15),background='white')
                    label1.grid(column=4, row=5)
                elif user_list[i][2]=="Manager":
                    label1=tk.Label(window, text="Menu access is granted.", font=("Arial", 15),background='white')
                    label1.grid(column=4, row=5)
                
            else:
                label3=tk.Label(window, text="Incorrect password. Access denied.", font=("Arial", 15))
                label3.grid(column=4, row=5)
        else:
            continue
    if count==0:
        label2=tk.Label(window, text="Incorrect username. Access denied.", font=("Arial", 15))
        label2.grid(column=4, row=5)
        print(count)
    


lbl1 = tk.Label(window, text="Login",font=("Arial",30),background="light green",justify=tk.RIGHT)
lbl1.grid(column=4,row=0)
lbl1 = tk.Label(window, text="Username",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=1)
lbl1 = tk.Label(window, text="Password",font=("Arial",20),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=3)


field1=tk.Entry()
field1.grid(column=4, row=2)
field2=tk.Entry(show='*')
field2.grid(column=4, row=4)


B1=tk.Button(window,text="Enter",command=check ,background="White").grid(column=4,row=8)

window.mainloop()
