
import tkinter as tk
import csv
import mysql.connector as sql
from datetime import date
from tkinter import messagebox

def image(smp):
    img = tk.PhotoImage(file="C:/Users/Intel/Documents/Screencast-O-Matic/Screenshots/Screenshot - Why Consider Going Green During a Restaurant Renovation  Renovation and Interior Design.png")
    img = img.subsample(smp, smp)
    return img

root=tk.Tk()

menu = tk.Menu()
menu.add_command(label="Quit", command=root.destroy)
root.config(menu=menu)
 


root.title("Welcome to Evergreen Restaurant")
root['background']='White'
ImgButton = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    
    font="arial 30",
    
    pady=10
    # width=300
    )
 
lbl1 = tk.Label(root, text="Evergreen Restaurant",font=("Arial",35),background="light Green",compound=tk.CENTER)
lbl1.pack()
img = image(2) # 1=normal, 2=small, 3=smallest
ImgButton.config(image=img)
ImgButton.pack()

def Login():
    root.destroy()
    user_list=[]


    login_window=tk.Tk()

    

    login_window.title("Login")
    login_window['background']='White'

    lbl1 = tk.Label(login_window, text="Login",font=("Arial",30),background="light green",justify=tk.RIGHT)
    lbl1.grid(column=4,row=0)
    lbl1 = tk.Label(login_window, text="Username",font=("Arial",25),background="white",justify=tk.RIGHT)
    lbl1.grid(column=4,row=1)
    lbl1 = tk.Label(login_window, text="Password",font=("Arial",25),background="white",justify=tk.RIGHT)
    lbl1.grid(column=4,row=3)


    field11=tk.Entry(login_window)
    field11.grid(column=4, row=2)
    field20=tk.Entry(show='*')
    field20.grid(column=4, row=4)
        
    with open("C:\\Users\\Intel\\Desktop\\LoginID.csv", "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        for row in csv_reader:
            user_list.append([row[0],row[1],row[2],row[3]])


    username_list=[]
    password_list=[]
    admin_list=[]
    for i in range(len(user_list)):
        username_list.append(user_list[i][1])
        password_list.append(user_list[i][0])
        admin_list.append(user_list[i][2])


    def check():
        global admin
        count=0
        user=str(field11.get())
        pin=str(field20.get())
        
        for i in range(len(user_list)):
            if user==user_list[i][1]:
                count=1
                
                
                if(pin==user_list[i][0]):
                    
                    if user_list[i][2]=="Admin" and user_list[i][3]=="Manager":
                        label1=tk.Label(login_window, text="Admin access is granted.", font=("Arial", 15),background='white')
                        label1.grid(column=4, row=5)
                        admin=1
                        
                    elif user_list[i][2]=="Manager":
                        label1=tk.Label(login_window, text="Staff access is granted.", font=("Arial", 15),background='white')
                        label1.grid(column=4, row=5)
                        admin=2
                    
                else:
                    label3=tk.Label(login_window, text="Incorrect password. Access denied.", font=("Arial", 15))
                    label3.grid(column=4, row=5)
            else:
                continue
        if count==0:
            label2=tk.Label(login_window, text="Incorrect username. Access denied.", font=("Arial", 15))
            label2.grid(column=4, row=5)
            print(count)
    
        if admin==1:
            
            login_window.destroy()
            admin_window=tk.Tk()
            


            admin_window.title("Admin Access")
            admin_window['background']='White'


            lbl1 = tk.Label(admin_window, text="Choice",font=("Arial",25),background="light Green",justify=tk.RIGHT)
            lbl1.grid(column=4,row=0)

            
            def Edit_Menu():
                Edit_window=tk.Tk()

                

                Edit_window.title("Restaurateur")
                Edit_window['background']='White'
                lbl1 = tk.Label(Edit_window,text="Edit Menu",font=("Arial",20),background="light green",compound=tk.CENTER)
                lbl1.grid(column=4,row=0)
                lbl1 = tk.Label(Edit_window,text="Update Items",font=("Arial",18),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=3)
                lbl1 = tk.Label(Edit_window,text="Update Rate",font=("Arial",18),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=4)
                menu_list=["Veg Kababs","Paneer Tikka","Chilli Chicken","Aloo-Dal Tikki","Cheese Balls","Chicken Wings","Basil Chicken Cups","Potato Fries","Tomato Soup","Sweet Corn Soup","Lahori Paneer","Mushroom Buckwheat Risotto","Chicken Kadai","Lahori Kofta","Veg Kurma","Chana Masala","Vegetable Biryani","Spicy Vegan Potato Curry","Roti","Naan","Apple Pie","Bluberry Pastry","Honey Cheesecake","Mango Tarts","Chocolate Moussie","Affogato","Tiramisu","Pudding","Chocolate icecream","Mango Milkshake"]
                variable1=tk.StringVar(Edit_window)
                variable1.set(menu_list[0])
                field1=tk.OptionMenu(Edit_window,variable1,*menu_list)
                field1.grid(column=5,row=3)
                field2=tk.Entry(Edit_window)
                field2.grid(column=5, row=4)

                
                mydb=sql.connect(
                    host="localhost",
                    user="root",
                    charset="utf8",
                    passwd="110104",
                    auth_plugin='mysql_native_password',
                    database="evergreen_restaurant")

                mycursor=mydb.cursor()
                def check1():
                        
                        menu_list=variable1.get()
                        updateRate=field2.get()
                        
                        
                        command1=mycursor.execute("SELECT * FROM menu")
                        command2=mycursor.fetchall()
                        count=0
                  
                        for i in range(len(command2)):
                       
                            if str(command2[i][0])==menu_list:
                                
                                if menu_list=="" or updateRate=="":
                                    label2=tk.Label(Edit_window, text="Please enter all fields.")
                                    label2.grid(column=4, row=7)
                                
                                elif menu_list!="" and updateRate!="" and updateRate.isdigit():
                                    string1="UPDATE menu SET  Price=%s WHERE Item_name=%s"
                                    val=(updateRate,menu_list)
                                    mycursor.execute(string1, val)
                                    label3=tk.Label(Edit_window, text="Item has been successfully edited.")
                                    label3.grid(column=4, row=7)
                                    mydb.commit()
                                    count=1
                                    print(count)
                                    break
                               
                                
                                elif  count==0 and updateRate.isdigit() is False:
                                    label5=tk.Label(Edit_window, text="Please enter a numeric value for the Rate.")
                                    label5.grid(column=4, row=7)
                                    
                                elif count==0:
                                    label4=tk.Label(Edit_window,text="Sorry!Item does not exist")
                                    label4.grid(column=4,row=7)
                            
                                
                enter_button=tk.Button(Edit_window, text="Enter", command=check1)
                enter_button.grid(column=4, row=6)

                
                Edit_window.mainloop()

                            
            def View_Menu():
            
                View_window=tk.Tk()
                View_window.title("View Menu Table")
                View_window['background']="White"
                try:
                    
                    mydb = sql.connect(
                        host="localhost",
                        user="root",
                        passwd="110104",
                        charset="utf8",database="Evergreen_Restaurant")
                    mycursor=mydb.cursor()
                    
                    Menu=mycursor.execute("SELECT * FROM menu")
                    command1=mycursor.fetchall()
                    
                    lbl1=tk.Label(View_window, text="Item Name",font=("Arial",25),background="light green")
                    lbl1.grid(column=0, row=0)
                    lbl2=tk.Label(View_window, text="Price",font=("Arial",25),background="light green")
                    lbl2.grid(column=1, row=0)
                     
                       
                    for i in range(len(command1)):
                        
                        label1=tk.Label(View_window, text=command1[i][0],background="white",borderwidth=1, relief="solid")
                        label1.grid(column=0, row=i+1)
                        
                        label2=tk.Label(View_window, text=command1[i][1],background="white", borderwidth=1, relief="solid")
                        label2.grid(column=1, row=i+1)
                        
                        
                    exit_button=tk.Button(View_window, text="Exit",font=("Arial",13), command=View_window.destroy)
                    exit_button.grid(column=0, row=len(command1)+2)
                    
                except sql.InternalError as e:
                    print("InternalError")
                    print(e)
                    
                View_window.mainloop()
                
            def Take_Order():

                def callback():
                    if messagebox.askyesno('Verify', 'Is this your Final Order?'):
                        messagebox.showinfo('Yes', 'Order has been taken')
                        getVariable()
                        
                        
                    else:
                        messagebox.showinfo('No', 'Order has been cancelled')
                    
                window=tk.Tk()

                import mysql.connector as sql
                try:
                    
                    mydb=sql.connect(
                        host="localhost",
                        user="root",
                        charset="utf8",
                        passwd="110104",
                        auth_plugin='mysql_native_password',
                        database="evergreen_restaurant")
                    mycursor=mydb.cursor()

                    def getVariable():
                        sum1=0
                        if(var1.get()==1):
                            print("Veg Kababs")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Veg Kababs":
                                    qty1=int(variable1.get())
                                    print(qty1)
                                    string3=f"UPDATE menu SET quantity={qty1} WHERE Item_name='Veg Kababs'"#f strings-provide a way to embed expressions inside string literals,these are replaced by their values
                                    val=(qty1)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Veg Kababs'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty1*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var2.get()==1):
                            print("Paneer Tikka")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Paneer Tikka":
                                    qty2=int(variable2.get())
                                    print(qty2)
                                    string3=f"UPDATE menu SET quantity={qty2} WHERE Item_name='Paneer Tikka'"
                                    val=(qty2)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Paneer Tikka'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty2*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var3.get()==1):
                            print("Chilli Chicken")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chilli Chicken":
                                    qty3=int(variable3.get())
                                    print(qty3)
                                    string3=f"UPDATE menu SET quantity={qty3} WHERE Item_name='Chilli Chicken'"
                                    val=(qty3)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chilli Chicken'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty3*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var4.get()==1):
                            print("Aloo-Dal Tikki")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Aloo-Dal Tikki":
                                    qty4=int(variable4.get())
                                    print(qty4)
                                    string3=f"UPDATE menu SET quantity={qty1} WHERE Item_name='Aloo-Dal Tikki'"
                                    val=(qty4)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Aloo-Dal Tikki'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty4*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var5.get()==1):
                            print("Cheese Balls")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Cheese Balls":
                                    qty5=int(variable5.get())
                                    print(qty5)
                                    string3=f"UPDATE menu SET quantity={qty5} WHERE Item_name='Cheese Balls'"
                                    val=(qty5)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Cheese Balls'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty5*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var6.get()==1):
                            print("Chicken Wings")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chicken Wings":
                                    qty6=int(variable6.get())
                                    print(qty6)
                                    string3=f"UPDATE menu SET quantity={qty6} WHERE Item_name='Chicken Wings'"
                                    val=(qty6)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chicken Wings'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty6*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var7.get()==1):
                            print("Basil Chicken Cups")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Basil Chicken Cups":
                                    qty7=int(variable7.get())
                                    print(qty7)
                                    string3=f"UPDATE menu SET quantity={qty7} WHERE Item_name='Basil Chicken Cups'"
                                    val=(qty7)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Basil Chicken Cups'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty7*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var8.get()==1):
                            print("Potato Fries")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Potato Fries":
                                    qty8=int(variable8.get())
                                    print(qty8)
                                    string3=f"UPDATE menu SET quantity={qty8} WHERE Item_name='Potato Fries'"
                                    val=(qty8)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Potato Fries'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty8*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var9.get()==1):
                            print("Tomato Soup")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Tomato Soup":
                                    qty9=int(variable9.get())
                                    print(qty9)
                                    string3=f"UPDATE menu SET quantity={qty9} WHERE Item_name='Tomato Soup'"
                                    val=(qty9)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Tomato Soup'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty9*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var10.get()==1):
                            print("Sweet Corn Soup")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Sweet Corn Soup":
                                    qty10=int(variable10.get())
                                    print(qty10)
                                    string3=f"UPDATE menu SET quantity={qty10} WHERE Item_name='Sweet Corn Soup'"
                                    val=(qty10)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Sweet Corn Soup'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty10*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var11.get()==1):
                            print("Lahori Paneer")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Lahori Paneer":
                                    qty11=int(variable11.get())
                                    print(qty11)
                                    string3=f"UPDATE menu SET quantity={qty11} WHERE Item_name='Lahori Paneer'"
                                    val=(qty11)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Lahori Paneer'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty11*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var12.get()==1):
                            print("Mushroom Buckwheat Risotto")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mushroom Buckwheat Risotto":
                                    qty12=int(variable12.get())
                                    print(qty12)
                                    string3=f"UPDATE menu SET quantity={qty12} WHERE Item_name='Mushroom Buckwheat Risotto'"
                                    val=(qty12)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mushroom Buckwheat Risotto'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty12*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var13.get()==1):
                            print("Chicken Kadai")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chicken Kadai":
                                    qty13=int(variable13.get())
                                    print(qty13)
                                    string3=f"UPDATE menu SET quantity={qty13} WHERE Item_name='Chicken Kadai'"
                                    val=(qty13)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chicken Kadai'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty13*int(''.join(map(str,j))))
                                    
                                   
                                    
                                    mydb.commit()
                                    break
                        if(var14.get()==1):
                            print("Lahori Kofta")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Lahori Kofta":
                                    qty14=int(variable14.get())
                                    print(qty14)
                                    string3=f"UPDATE menu SET quantity={qty14} WHERE Item_name='Lahori Kofta'"
                                    val=(qty14)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Lahori Kofta'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty14*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var15.get()==1):
                            print("Veg Kurma")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Veg Kurma":
                                    qty15=int(variable15.get())
                                    print(qty15)
                                    string3=f"UPDATE menu SET quantity={qty15} WHERE Item_name='Veg Kurma'"
                                    val=(qty15)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Veg Kurma'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty15*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var16.get()==1):
                            print("Chana Masala")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chana Masala":
                                    qty16=int(variable16.get())
                                    print(qty16)
                                    string3=f"UPDATE menu SET quantity={qty16} WHERE Item_name='Chana Masala'"
                                    val=(qty16)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chana Masala'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty16*int(''.join(map(str,j))))
                                    
                                   
                                    
                                    mydb.commit()
                                    break
                        if(var17.get()==1):
                            print("Vegetable Biryani")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Vegetable Biryani":
                                    qty17=int(variable17.get())
                                    print(qty17)
                                    string3=f"UPDATE menu SET quantity={qty17} WHERE Item_name='Vegetable Biryani'"
                                    val=(qty17)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Vegetable Biryani'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty17*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var18.get()==1):
                            print("Spicy Vegan Potato Curry")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Spicy Vegan Potato Curry":
                                    qty18=int(variable18.get())
                                    print(qty18)
                                    string3=f"UPDATE menu SET quantity={qty18} WHERE Item_name='Spicy Vegan Potato Curry'"
                                    val=(qty18)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Spicy Vegan Potato Curry'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty18*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var19.get()==1):
                            print("Roti")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Roti":
                                    qty19=int(variable19.get())
                                    print(qty19)
                                    string3=f"UPDATE menu SET quantity={qty19} WHERE Item_name='Roti'"
                                    val=(qty19)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Roti'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty19*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var20.get()==1):
                            print("Naan")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Naan":
                                    qty20=int(variable20.get())
                                    print(qty20)
                                    string3=f"UPDATE menu SET quantity={qty20} WHERE Item_name='Naan'"
                                    val=(qty20)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Naan'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty20*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var21.get()==1):
                            print("Apple Pie")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Apple Pie":
                                    qty21=int(variable21.get())
                                    print(qty21)
                                    string3=f"UPDATE menu SET quantity={qty21} WHERE Item_name='Apple Pie'"
                                    val=(qty21)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Apple Pie'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty21*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var22.get()==1):
                            print("Bluberry Pastry")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Bluberry Pastry":
                                    qty22=int(variable22.get())
                                    print(qty22)
                                    string3=f"UPDATE menu SET quantity={qty22} WHERE Item_name='Bluberry Pastry'"
                                    val=(qty22)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Bluberry Pastry'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty22*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var23.get()==1):
                            print("Honey Cheesecake")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Honey Cheesecake":
                                    qty23=int(variable23.get())
                                    print(qty23)
                                    string3=f"UPDATE menu SET quantity={qty23} WHERE Item_name='Honey Cheesecake'"
                                    val=(qty23)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Honey Cheesecake'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty23*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var24.get()==1):
                            print("Mango Tarts")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mango Tarts":
                                    qty24=int(variable24.get())
                                    print(qty24)
                                    string3=f"UPDATE menu SET quantity={qty24} WHERE Item_name='Mango Tarts'"
                                    val=(qty24)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mango Tarts'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty24*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var25.get()==1):
                            print("Chocolate Moussie")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chocolate Moussie":
                                    qty25=int(variable25.get())
                                    print(qty25)
                                    string3=f"UPDATE menu SET quantity={qty25} WHERE Item_name='Chocolate Moussie'"
                                    val=(qty25)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chocolate Moussie'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty25*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var26.get()==1):
                            print("Affogato")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Affogato":
                                    qty26=int(variable26.get())
                                    print(qty26)
                                    string3=f"UPDATE menu SET quantity={qty26} WHERE Item_name='Affogato'"
                                    val=(qty26)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Affogato'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty26*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var27.get()==1):
                            print("Tiramisu")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Tiramisu":
                                    qty27=int(variable27.get())
                                    print(qty27)
                                    string3=f"UPDATE menu SET quantity={qty27} WHERE Item_name='Tiramisu'"
                                    val=(qty27)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Tiramisu'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty27*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var28.get()==1):
                            print("Pudding")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Pudding":
                                    qty28=int(variable28.get())
                                    print(qty28)
                                    string3=f"UPDATE menu SET quantity={qty28} WHERE Item_name='Pudding'"
                                    val=(qty28)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Pudding'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty28*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var29.get()==1):
                            print("Chocolate icecream")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chocolate icecream":
                                    qty29=int(variable29.get())
                                    print(qty29)
                                    string3=f"UPDATE menu SET quantity={qty29} WHERE Item_name='Chocolate icecream'"
                                    val=(qty29)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chocolate icecream'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty29*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var30.get()==1):
                            print("Mango Milkshake")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mango Milkshake":
                                    qty30=int(variable30.get())
                                    print(qty30)
                                    string3=f"UPDATE menu SET quantity={qty30} WHERE Item_name='Mango Milkshake'"
                                    val=(qty30)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mango Milkshake'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty30*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        
                        
                    
                        CustomerName=NameField.get()
                        date1=date.today()
                         
                        string1=f"insert into Billing(Customer_name,Date,Bill_Amt) values('{CustomerName}','{date1}', {sum1})"
                        
                        print("The Total is:",sum1)
                        mycursor.execute(string1)
                       
                        mydb.commit()
                        
                  
                except sql.InternalError as e:
                    print("InternalError")
                    print(e)

                window.title("Menu")
                window['background']='White'

                lbl1 = tk.Label(window, text="Starters",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=4,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=5,row=2)
                lbl1 = tk.Label(window, text="Main Course",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=6,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=7,row=2)
                lbl1 = tk.Label(window, text="Deserts",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=8,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=8,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=9,row=2)
                lbl1 = tk.Label(window, text="Customer Name",font=("Arial",15),background="white",justify=tk.RIGHT).grid(column=4,row=0)
                NameField=tk.Entry(window)
                NameField.grid(column=5,row=0)

                var1=tk.IntVar(window)
                B1=tk.Checkbutton(window,text="Veg Kababs--150/-",variable=var1,background="White").grid(column=4,row=3)
                var2=tk.IntVar(window)
                B2=tk.Checkbutton(window,text="Paneer Tikka--120/-",variable=var2,background="White").grid(column=4,row=4)
                var3=tk.IntVar(window)
                B3=tk.Checkbutton(window,text="Chilli Chicken--200/-",variable=var3,background="White").grid(column=4,row=5)
                var4=tk.IntVar(window)
                B4=tk.Checkbutton(window,text="Aloo-Dal Tikki--100/-",variable=var4,background="White").grid(column=4,row=6)
                var5=tk.IntVar(window)
                B5=tk.Checkbutton(window,text="Cheese Balls--200/-",variable=var5,background="White").grid(column=4,row=7)
                var6=tk.IntVar(window)
                B6=tk.Checkbutton(window,text="Chicken Wings--180/-",variable=var6,background="White").grid(column=4,row=8)
                var7=tk.IntVar(window)
                B7=tk.Checkbutton(window,text="Basil Chicken Cups--200/-",variable=var7,background="White").grid(column=4,row=9)
                var8=tk.IntVar(window)
                B8=tk.Checkbutton(window,text="Potato Fries--130/-",variable=var8,background="White").grid(column=4,row=10)
                var9=tk.IntVar(window)
                B9=tk.Checkbutton(window,text="Tomato Soup--150/-",variable=var9,background="White").grid(column=4,row=11)
                var10=tk.IntVar(window)
                B10=tk.Checkbutton(window,text="Sweet Corn Soup--120/-",variable=var10,background="White").grid(column=4,row=12)

                var11=tk.IntVar(window)
                B11=tk.Checkbutton(window,text="Lahori Paneer--210/-",variable=var11,background="White").grid(column=6,row=3)
                var12=tk.IntVar(window)
                B12=tk.Checkbutton(window,text="Mushroom Buckwheat Risotto--250/-",variable=var12,background="White").grid(column=6,row=4)
                var13=tk.IntVar(window)
                B13=tk.Checkbutton(window,text="Chicken Kadai--200/-",variable=var13,background="White").grid(column=6,row=5)
                var14=tk.IntVar(window)
                B14=tk.Checkbutton(window,text="Lahori Kofta--230/-",variable=var14,background="White").grid(column=6,row=6)
                var15=tk.IntVar(window)
                B15=tk.Checkbutton(window,text="Veg Kurma--200/-",variable=var15,background="White").grid(column=6,row=7)
                var16=tk.IntVar(window)
                B16=tk.Checkbutton(window,text="Chana Masala--180/-",variable=var16,background="White").grid(column=6,row=8)
                var17=tk.IntVar(window)
                B17=tk.Checkbutton(window,text="Vegetable Biryani--200/-",variable=var17,background="White").grid(column=6,row=9)
                var18=tk.IntVar(window)
                B18=tk.Checkbutton(window,text="Spicy Vegan Potato Curry--130/-",variable=var18,background="White").grid(column=6,row=10)
                var19=tk.IntVar(window)
                B19=tk.Checkbutton(window,text="Roti--30/-",variable=var19,background="White").grid(column=6,row=11)
                var20=tk.IntVar(window)
                B20=tk.Checkbutton(window,text="Naan--50/-",variable=var20,background="White").grid(column=6,row=12)

                var21=tk.IntVar(window)
                B21=tk.Checkbutton(window,text="Apple Pie--110/-",variable=var21,background="White").grid(column=8,row=3)
                var22=tk.IntVar(window)
                B22=tk.Checkbutton(window,text="Bluberry Pastry--120/-",variable=var22,background="White").grid(column=8,row=4)
                var23=tk.IntVar(window)
                B23=tk.Checkbutton(window,text="Honey Cheesecake--100/-",variable=var23,background="White").grid(column=8,row=5)
                var24=tk.IntVar(window)
                B24=tk.Checkbutton(window,text="Mango Tarts--100/-",variable=var24,background="White").grid(column=8,row=6)
                var25=tk.IntVar(window)
                B25=tk.Checkbutton(window,text="Chocolate Moussie--90/-",variable=var25,background="White").grid(column=8,row=7)
                var26=tk.IntVar(window)
                B26=tk.Checkbutton(window,text="Affogato--120/-",variable=var26,background="White").grid(column=8,row=8)
                var27=tk.IntVar(window)
                B27=tk.Checkbutton(window,text="Tiramisu--200/-",variable=var27,background="White").grid(column=8,row=9)
                var28=tk.IntVar(window)
                B28=tk.Checkbutton(window,text="Pudding--130/-",variable=var28,background="White").grid(column=8,row=10)
                var29=tk.IntVar(window)
                B29=tk.Checkbutton(window,text="Chocolate icecream--80/-",variable=var29,background="White").grid(column=8,row=11)
                var30=tk.IntVar(window)
                B30=tk.Checkbutton(window,text="Mango Milkshake--100/-",variable=var30,background="White").grid(column=8,row=12)

                Enter_button=tk.Button(window, text="Enter", command=callback)
                Enter_button.grid(column=6, row=13)

                qty_list=["0","1","2","3","4","5"]
                variable1=tk.StringVar(window)
                variable1.set(qty_list[0])
                field2=tk.OptionMenu(window,variable1,*qty_list)
                field2.grid(column=5,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable2=tk.StringVar(window)
                variable2.set(qty_list[0])
                field2=tk.OptionMenu(window,variable2,*qty_list)
                field2.grid(column=5,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable3=tk.StringVar(window)
                variable3.set(qty_list[0])
                field2=tk.OptionMenu(window,variable3,*qty_list)
                field2.grid(column=5,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable4=tk.StringVar(window)
                variable4.set(qty_list[0])
                field2=tk.OptionMenu(window,variable4,*qty_list)
                field2.grid(column=5,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable5=tk.StringVar(window)
                variable5.set(qty_list[0])
                field2=tk.OptionMenu(window,variable5,*qty_list)
                field2.grid(column=5,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable6=tk.StringVar(window)
                variable6.set(qty_list[0])
                field2=tk.OptionMenu(window,variable6,*qty_list)
                field2.grid(column=5,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable7=tk.StringVar(window)
                variable7.set(qty_list[0])
                field2=tk.OptionMenu(window,variable7,*qty_list)
                field2.grid(column=5,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable8=tk.StringVar(window)
                variable8.set(qty_list[0])
                field2=tk.OptionMenu(window,variable8,*qty_list)
                field2.grid(column=5,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable9=tk.StringVar(window)
                variable9.set(qty_list[0])
                field2=tk.OptionMenu(window,variable9,*qty_list)
                field2.grid(column=5,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable10=tk.StringVar(window)
                variable10.set(qty_list[0])
                field2=tk.OptionMenu(window,variable10,*qty_list)
                field2.grid(column=5,row=12)

                qty_list=["0","1","2","3","4","5"]
                variable11=tk.StringVar(window)
                variable11.set(qty_list[0])
                field2=tk.OptionMenu(window,variable11,*qty_list)
                field2.grid(column=7,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable12=tk.StringVar(window)
                variable12.set(qty_list[0])
                field2=tk.OptionMenu(window,variable12,*qty_list)
                field2.grid(column=7,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable13=tk.StringVar(window)
                variable13.set(qty_list[0])
                field2=tk.OptionMenu(window,variable13,*qty_list)
                field2.grid(column=7,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable14=tk.StringVar(window)
                variable14.set(qty_list[0])
                field2=tk.OptionMenu(window,variable14,*qty_list)
                field2.grid(column=7,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable15=tk.StringVar(window)
                variable15.set(qty_list[0])
                field2=tk.OptionMenu(window,variable15,*qty_list)
                field2.grid(column=7,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable16=tk.StringVar(window)
                variable16.set(qty_list[0])
                field2=tk.OptionMenu(window,variable16,*qty_list)
                field2.grid(column=7,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable17=tk.StringVar(window)
                variable17.set(qty_list[0])
                field2=tk.OptionMenu(window,variable17,*qty_list)
                field2.grid(column=7,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable18=tk.StringVar(window)
                variable18.set(qty_list[0])
                field2=tk.OptionMenu(window,variable18,*qty_list)
                field2.grid(column=7,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable19=tk.StringVar(window)
                variable19.set(qty_list[0])
                field2=tk.OptionMenu(window,variable19,*qty_list)
                field2.grid(column=7,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable20=tk.StringVar(window)
                variable20.set(qty_list[0])
                field2=tk.OptionMenu(window,variable20,*qty_list)
                field2.grid(column=7,row=12)


                qty_list=["0","1","2","3","4","5"]
                variable21=tk.StringVar(window)
                variable21.set(qty_list[0])
                field2=tk.OptionMenu(window,variable21,*qty_list)
                field2.grid(column=9,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable22=tk.StringVar(window)
                variable22.set(qty_list[0])
                field2=tk.OptionMenu(window,variable22,*qty_list)
                field2.grid(column=9,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable23=tk.StringVar(window)
                variable23.set(qty_list[0])
                field2=tk.OptionMenu(window,variable23,*qty_list)
                field2.grid(column=9,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable24=tk.StringVar(window)
                variable24.set(qty_list[0])
                field2=tk.OptionMenu(window,variable24,*qty_list)
                field2.grid(column=9,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable25=tk.StringVar(window)
                variable25.set(qty_list[0])
                field2=tk.OptionMenu(window,variable25,*qty_list)
                field2.grid(column=9,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable26=tk.StringVar(window)
                variable26.set(qty_list[0])
                field2=tk.OptionMenu(window,variable26,*qty_list)
                field2.grid(column=9,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable27=tk.StringVar(window)
                variable27.set(qty_list[0])
                field2=tk.OptionMenu(window,variable27,*qty_list)
                field2.grid(column=9,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable28=tk.StringVar(window)
                variable28.set(qty_list[0])
                field2=tk.OptionMenu(window,variable28,*qty_list)
                field2.grid(column=9,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable29=tk.StringVar(window)
                variable29.set(qty_list[0])
                field2=tk.OptionMenu(window,variable29,*qty_list)
                field2.grid(column=9,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable30=tk.StringVar(window)
                variable30.set(qty_list[0])
                field2=tk.OptionMenu(window,variable30,*qty_list)
                field2.grid(column=9,row=12)

                window.mainloop()
                
                bill_window=tk.Tk()
                bill_window.title("Payment")
                bill_window['background']='White'


                lbl1 = tk.Label(bill_window, text="Billing Invoice",font=("Arial",25),background="light Green",compound=tk.CENTER)
                lbl1.grid(column=4,row=0)
                lbl1 = tk.Label(bill_window, text="Bill Number:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=2)
                lbl1 = tk.Label(bill_window, text="Customer Name:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=1)

                lbl1 = tk.Label(bill_window, text="Date",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=5,row=2)
                lbl1 = tk.Label(bill_window, text="Choice",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=1)
                lbl1 = tk.Label(bill_window, text="Total Bill Amount:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=2)

                field1=tk.Entry(bill_window)
                field1.grid(column=5,row=1)

                choice_list=["Dine In","Take Away"]
                variable2=tk.StringVar(bill_window)
                variable2.set(choice_list[0])
                field2=tk.OptionMenu(bill_window,variable2,*choice_list)
                field2.grid(column=7,row=1)

                

                mydb=sql.connect(
                    host="localhost",
                    user="root",
                    charset="utf8",
                    passwd="110104",
                    auth_plugin='mysql_native_password',
                    database="evergreen_restaurant")
                mycursor=mydb.cursor()  
                def Payment():
                    CustomerName=field1.get()
                    command1=mycursor.execute("SELECT * FROM Billing")
                    command2=mycursor.fetchall()
                    for i in range(len(command2)):
                            if str(command2[i][1])==CustomerName:
                              
                               label1=tk.Label(bill_window, text=command2[i][0],background="white",font=("Arial",15),borderwidth=1, relief="solid")
                               label1.grid(column=4, row=i+3)
                    
                               label1=tk.Label(bill_window, text=command2[i][2],background="white",font=("Arial",15),borderwidth=1, relief="solid")
                               label1.grid(column=5, row=i+3)
                               if(variable2.get()=="Take Away"):
                                   query1=mycursor.execute("UPDATE billing SET Bill_Amt=Bill_Amt+30")
                               label2=tk.Label(bill_window, text=command2[i][3],background="white",font=("Arial",15), borderwidth=1, relief="solid")
                               label2.grid(column=6, row=i+3)
                    
                   
                        
                B1=tk.Button(bill_window,text="Enter",command=Payment,background="White").grid(column=5,row=60)
                bill_window.mainloop()
      
            
            B1=tk.Button(admin_window,text="Edit Menu",command=Edit_Menu,width="30",background="white").grid(column=4,row=4)
            B2=tk.Button(admin_window,text="View Menu Table",command=View_Menu,width="30",background="white").grid(column=4,row=6)
            B3=tk.Button(admin_window,text="Take Order",command=Take_Order,width="30",background="white").grid(column=4,row=8)

            admin_window.mainloop()

        elif admin==2:
            login_window.destroy()
            staff_window=tk.Tk()
            


            staff_window.title("Staff Access")
            staff_window['background']='White'


            lbl1 = tk.Label(staff_window, text="Choice",font=("Arial",25),background="light Green",compound=tk.CENTER)
            lbl1.grid(column=4,row=0)
            
            def View_Menu_Staff():
                window=tk.Tk()
                window.title("View Menu Table")
                window['background']="White"
                try:
                    
                    mydb = sql.connect(
                        host="localhost",
                        user="root",
                        passwd="110104",
                        charset="utf8",database="Evergreen_Restaurant")
                    mycursor=mydb.cursor()
                    
                    Menu=mycursor.execute("SELECT * FROM menu")
                    command1=mycursor.fetchall()
                    
                    lbl1=tk.Label(window, text="Item Name",font=("Arial",25),background="light green")
                    lbl1.grid(column=0, row=0)
                    lbl2=tk.Label(window, text="Price",font=("Arial",25),background="light green")
                    lbl2.grid(column=1, row=0)
                     
                       
                    for i in range(len(command1)):
                        
                        label1=tk.Label(window, text=command1[i][0],background="white",borderwidth=1, relief="solid")
                        label1.grid(column=0, row=i+1)
                        
                        label2=tk.Label(window, text=command1[i][1],background="white", borderwidth=1, relief="solid")
                        label2.grid(column=1, row=i+1)
                        
                        
                    exit_button=tk.Button(window, text="Exit",font=("Arial",13), command=window.destroy)
                    exit_button.grid(column=0, row=len(command1)+2)
                    
                except sql.InternalError as e:
                    print("InternalError")
                    print(e)
                    
                window.mainloop()

            def Take_Order_Staff():
                
                from datetime import date
                from tkinter import messagebox

                def callback():
                    if messagebox.askyesno('Verify', 'Is this your Final Order?'):
                        messagebox.showinfo('Yes', 'Order has been taken')
                        getVariable()
                        
                        
                    else:
                        messagebox.showinfo('No', 'Order has been cancelled')
                    
                window=tk.Tk()

                import mysql.connector as sql
                try:
                    
                    mydb=sql.connect(
                        host="localhost",
                        user="root",
                        charset="utf8",
                        passwd="110104",
                        auth_plugin='mysql_native_password',
                        database="evergreen_restaurant")
                    mycursor=mydb.cursor()

                    def getVariable():
                        sum1=0
                        if(var1.get()==1):
                            print("Veg Kababs")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Veg Kababs":
                                    qty1=int(variable1.get())
                                    print(qty1)
                                    string3=f"UPDATE menu SET quantity={qty1} WHERE Item_name='Veg Kababs'"#f strings-provide a way to embed expressions inside string literals,these are replaced by their values
                                    val=(qty1)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Veg Kababs'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty1*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var2.get()==1):
                            print("Paneer Tikka")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Paneer Tikka":
                                    qty2=int(variable2.get())
                                    print(qty2)
                                    string3=f"UPDATE menu SET quantity={qty2} WHERE Item_name='Paneer Tikka'"
                                    val=(qty2)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Paneer Tikka'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty2*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var3.get()==1):
                            print("Chilli Chicken")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chilli Chicken":
                                    qty3=int(variable3.get())
                                    print(qty3)
                                    string3=f"UPDATE menu SET quantity={qty3} WHERE Item_name='Chilli Chicken'"
                                    val=(qty3)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chilli Chicken'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty3*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var4.get()==1):
                            print("Aloo-Dal Tikki")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Aloo-Dal Tikki":
                                    qty4=int(variable4.get())
                                    print(qty4)
                                    string3=f"UPDATE menu SET quantity={qty1} WHERE Item_name='Aloo-Dal Tikki'"
                                    val=(qty4)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Aloo-Dal Tikki'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty4*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var5.get()==1):
                            print("Cheese Balls")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Cheese Balls":
                                    qty5=int(variable5.get())
                                    print(qty5)
                                    string3=f"UPDATE menu SET quantity={qty5} WHERE Item_name='Cheese Balls'"
                                    val=(qty5)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Cheese Balls'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty5*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var6.get()==1):
                            print("Chicken Wings")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chicken Wings":
                                    qty6=int(variable6.get())
                                    print(qty6)
                                    string3=f"UPDATE menu SET quantity={qty6} WHERE Item_name='Chicken Wings'"
                                    val=(qty6)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chicken Wings'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty6*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var7.get()==1):
                            print("Basil Chicken Cups")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Basil Chicken Cups":
                                    qty7=int(variable7.get())
                                    print(qty7)
                                    string3=f"UPDATE menu SET quantity={qty7} WHERE Item_name='Basil Chicken Cups'"
                                    val=(qty7)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Basil Chicken Cups'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty7*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var8.get()==1):
                            print("Potato Fries")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Potato Fries":
                                    qty8=int(variable8.get())
                                    print(qty8)
                                    string3=f"UPDATE menu SET quantity={qty8} WHERE Item_name='Potato Fries'"
                                    val=(qty8)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Potato Fries'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty8*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var9.get()==1):
                            print("Tomato Soup")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Tomato Soup":
                                    qty9=int(variable9.get())
                                    print(qty9)
                                    string3=f"UPDATE menu SET quantity={qty9} WHERE Item_name='Tomato Soup'"
                                    val=(qty9)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Tomato Soup'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty9*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var10.get()==1):
                            print("Sweet Corn Soup")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Sweet Corn Soup":
                                    qty10=int(variable10.get())
                                    print(qty10)
                                    string3=f"UPDATE menu SET quantity={qty10} WHERE Item_name='Sweet Corn Soup'"
                                    val=(qty10)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Sweet Corn Soup'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty10*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var11.get()==1):
                            print("Lahori Paneer")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Lahori Paneer":
                                    qty11=int(variable11.get())
                                    print(qty11)
                                    string3=f"UPDATE menu SET quantity={qty11} WHERE Item_name='Lahori Paneer'"
                                    val=(qty11)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Lahori Paneer'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty11*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var12.get()==1):
                            print("Mushroom Buckwheat Risotto")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mushroom Buckwheat Risotto":
                                    qty12=int(variable12.get())
                                    print(qty12)
                                    string3=f"UPDATE menu SET quantity={qty12} WHERE Item_name='Mushroom Buckwheat Risotto'"
                                    val=(qty12)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mushroom Buckwheat Risotto'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty12*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var13.get()==1):
                            print("Chicken Kadai")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chicken Kadai":
                                    qty13=int(variable13.get())
                                    print(qty13)
                                    string3=f"UPDATE menu SET quantity={qty13} WHERE Item_name='Chicken Kadai'"
                                    val=(qty13)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chicken Kadai'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty13*int(''.join(map(str,j))))
                                    
                                   
                                    
                                    mydb.commit()
                                    break
                        if(var14.get()==1):
                            print("Lahori Kofta")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Lahori Kofta":
                                    qty14=int(variable14.get())
                                    print(qty14)
                                    string3=f"UPDATE menu SET quantity={qty14} WHERE Item_name='Lahori Kofta'"
                                    val=(qty14)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Lahori Kofta'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty14*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var15.get()==1):
                            print("Veg Kurma")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Veg Kurma":
                                    qty15=int(variable15.get())
                                    print(qty15)
                                    string3=f"UPDATE menu SET quantity={qty15} WHERE Item_name='Veg Kurma'"
                                    val=(qty15)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Veg Kurma'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty15*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var16.get()==1):
                            print("Chana Masala")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chana Masala":
                                    qty16=int(variable16.get())
                                    print(qty16)
                                    string3=f"UPDATE menu SET quantity={qty16} WHERE Item_name='Chana Masala'"
                                    val=(qty16)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chana Masala'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty16*int(''.join(map(str,j))))
                                    
                                   
                                    
                                    mydb.commit()
                                    break
                        if(var17.get()==1):
                            print("Vegetable Biryani")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Vegetable Biryani":
                                    qty17=int(variable17.get())
                                    print(qty17)
                                    string3=f"UPDATE menu SET quantity={qty17} WHERE Item_name='Vegetable Biryani'"
                                    val=(qty17)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Vegetable Biryani'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty17*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var18.get()==1):
                            print("Spicy Vegan Potato Curry")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Spicy Vegan Potato Curry":
                                    qty18=int(variable18.get())
                                    print(qty18)
                                    string3=f"UPDATE menu SET quantity={qty18} WHERE Item_name='Spicy Vegan Potato Curry'"
                                    val=(qty18)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Spicy Vegan Potato Curry'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty18*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var19.get()==1):
                            print("Roti")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Roti":
                                    qty19=int(variable19.get())
                                    print(qty19)
                                    string3=f"UPDATE menu SET quantity={qty19} WHERE Item_name='Roti'"
                                    val=(qty19)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Roti'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty19*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var20.get()==1):
                            print("Naan")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Naan":
                                    qty20=int(variable20.get())
                                    print(qty20)
                                    string3=f"UPDATE menu SET quantity={qty20} WHERE Item_name='Naan'"
                                    val=(qty20)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Naan'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty20*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var21.get()==1):
                            print("Apple Pie")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Apple Pie":
                                    qty21=int(variable21.get())
                                    print(qty21)
                                    string3=f"UPDATE menu SET quantity={qty21} WHERE Item_name='Apple Pie'"
                                    val=(qty21)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Apple Pie'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty21*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var22.get()==1):
                            print("Bluberry Pastry")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Bluberry Pastry":
                                    qty22=int(variable22.get())
                                    print(qty22)
                                    string3=f"UPDATE menu SET quantity={qty22} WHERE Item_name='Bluberry Pastry'"
                                    val=(qty22)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Bluberry Pastry'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty22*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var23.get()==1):
                            print("Honey Cheesecake")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Honey Cheesecake":
                                    qty23=int(variable23.get())
                                    print(qty23)
                                    string3=f"UPDATE menu SET quantity={qty23} WHERE Item_name='Honey Cheesecake'"
                                    val=(qty23)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Honey Cheesecake'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty23*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var24.get()==1):
                            print("Mango Tarts")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mango Tarts":
                                    qty24=int(variable24.get())
                                    print(qty24)
                                    string3=f"UPDATE menu SET quantity={qty24} WHERE Item_name='Mango Tarts'"
                                    val=(qty24)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mango Tarts'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty24*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var25.get()==1):
                            print("Chocolate Moussie")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chocolate Moussie":
                                    qty25=int(variable25.get())
                                    print(qty25)
                                    string3=f"UPDATE menu SET quantity={qty25} WHERE Item_name='Chocolate Moussie'"
                                    val=(qty25)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chocolate Moussie'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty25*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var26.get()==1):
                            print("Affogato")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Affogato":
                                    qty26=int(variable26.get())
                                    print(qty26)
                                    string3=f"UPDATE menu SET quantity={qty26} WHERE Item_name='Affogato'"
                                    val=(qty26)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Affogato'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty26*int(''.join(map(str,j))))
                                    
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var27.get()==1):
                            print("Tiramisu")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Tiramisu":
                                    qty27=int(variable27.get())
                                    print(qty27)
                                    string3=f"UPDATE menu SET quantity={qty27} WHERE Item_name='Tiramisu'"
                                    val=(qty27)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Tiramisu'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty27*int(''.join(map(str,j))))
                                    
                                    mydb.commit()
                                    break
                        if(var28.get()==1):
                            print("Pudding")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Pudding":
                                    qty28=int(variable28.get())
                                    print(qty28)
                                    string3=f"UPDATE menu SET quantity={qty28} WHERE Item_name='Pudding'"
                                    val=(qty28)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Pudding'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty28*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var29.get()==1):
                            print("Chocolate icecream")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Chocolate icecream":
                                    qty29=int(variable29.get())
                                    print(qty29)
                                    string3=f"UPDATE menu SET quantity={qty29} WHERE Item_name='Chocolate icecream'"
                                    val=(qty29)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Chocolate icecream'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty29*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        if(var30.get()==1):
                            print("Mango Milkshake")
                            command1=mycursor.execute("SELECT * FROM menu")
                            command2=mycursor.fetchall()
                            for i in range(len(command2)):
                                if str(command2[i][0])=="Mango Milkshake":
                                    qty30=int(variable30.get())
                                    print(qty30)
                                    string3=f"UPDATE menu SET quantity={qty30} WHERE Item_name='Mango Milkshake'"
                                    val=(qty30)
                                    mycursor.execute(string3,val)
                                    string1="SELECT Price FROM menu WHERE Item_name='Mango Milkshake'"
                                    mycursor.execute(string1)
                                    string2=mycursor.fetchall()
                                    for j in string2:
                                        print(j)
                                        sum1=sum1+(qty30*int(''.join(map(str,j))))
                                    
                                    
                                    mydb.commit()
                                    break
                        
                        
                    
                        CustomerName=NameField.get()
                        date1=date.today()
                         
                        string1=f"insert into Billing(Customer_name,Date,Bill_Amt) values('{CustomerName}','{date1}', {sum1})"
                        
                        print(CustomerName,sum1)
                        mycursor.execute(string1)
                       
                        mydb.commit()
                        
                  
                except sql.InternalError as e:
                    print("InternalError")
                    print(e)

                window.title("Menu")
                window['background']='White'

                lbl1 = tk.Label(window, text="Starters",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=4,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=5,row=2)
                lbl1 = tk.Label(window, text="Main Course",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=6,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=7,row=2)
                lbl1 = tk.Label(window, text="Deserts",font=("Arial",20),background="light Green",justify=tk.RIGHT)
                lbl1.grid(column=8,row=1)
                lbl1 = tk.Label(window, text="Items",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=8,row=2)
                lbl1 = tk.Label(window, text="Quantity",font=("Arial",20),background="white",justify=tk.RIGHT)
                lbl1.grid(column=9,row=2)
                lbl1 = tk.Label(window, text="Customer Name",font=("Arial",15),background="white",justify=tk.RIGHT).grid(column=4,row=0)
                NameField=tk.Entry(window)
                NameField.grid(column=5,row=0)

                var1=tk.IntVar(window)
                B1=tk.Checkbutton(window,text="Veg Kababs--150/-",variable=var1,background="White").grid(column=4,row=3)
                var2=tk.IntVar(window)
                B2=tk.Checkbutton(window,text="Paneer Tikka--120/-",variable=var2,background="White").grid(column=4,row=4)
                var3=tk.IntVar(window)
                B3=tk.Checkbutton(window,text="Chilli Chicken--200/-",variable=var3,background="White").grid(column=4,row=5)
                var4=tk.IntVar(window)
                B4=tk.Checkbutton(window,text="Aloo-Dal Tikki--100/-",variable=var4,background="White").grid(column=4,row=6)
                var5=tk.IntVar(window)
                B5=tk.Checkbutton(window,text="Cheese Balls--200/-",variable=var5,background="White").grid(column=4,row=7)
                var6=tk.IntVar(window)
                B6=tk.Checkbutton(window,text="Chicken Wings--180/-",variable=var6,background="White").grid(column=4,row=8)
                var7=tk.IntVar(window)
                B7=tk.Checkbutton(window,text="Basil Chicken Cups--200/-",variable=var7,background="White").grid(column=4,row=9)
                var8=tk.IntVar(window)
                B8=tk.Checkbutton(window,text="Potato Fries--130/-",variable=var8,background="White").grid(column=4,row=10)
                var9=tk.IntVar(window)
                B9=tk.Checkbutton(window,text="Tomato Soup--150/-",variable=var9,background="White").grid(column=4,row=11)
                var10=tk.IntVar(window)
                B10=tk.Checkbutton(window,text="Sweet Corn Soup--120/-",variable=var10,background="White").grid(column=4,row=12)

                var11=tk.IntVar(window)
                B11=tk.Checkbutton(window,text="Lahori Paneer--210/-",variable=var11,background="White").grid(column=6,row=3)
                var12=tk.IntVar(window)
                B12=tk.Checkbutton(window,text="Mushroom Buckwheat Risotto--250/-",variable=var12,background="White").grid(column=6,row=4)
                var13=tk.IntVar(window)
                B13=tk.Checkbutton(window,text="Chicken Kadai--200/-",variable=var13,background="White").grid(column=6,row=5)
                var14=tk.IntVar(window)
                B14=tk.Checkbutton(window,text="Lahori Kofta--230/-",variable=var14,background="White").grid(column=6,row=6)
                var15=tk.IntVar(window)
                B15=tk.Checkbutton(window,text="Veg Kurma--200/-",variable=var15,background="White").grid(column=6,row=7)
                var16=tk.IntVar(window)
                B16=tk.Checkbutton(window,text="Chana Masala--180/-",variable=var16,background="White").grid(column=6,row=8)
                var17=tk.IntVar(window)
                B17=tk.Checkbutton(window,text="Vegetable Biryani--200/-",variable=var17,background="White").grid(column=6,row=9)
                var18=tk.IntVar(window)
                B18=tk.Checkbutton(window,text="Spicy Vegan Potato Curry--130/-",variable=var18,background="White").grid(column=6,row=10)
                var19=tk.IntVar(window)
                B19=tk.Checkbutton(window,text="Roti--30/-",variable=var19,background="White").grid(column=6,row=11)
                var20=tk.IntVar(window)
                B20=tk.Checkbutton(window,text="Naan--50/-",variable=var20,background="White").grid(column=6,row=12)

                var21=tk.IntVar(window)
                B21=tk.Checkbutton(window,text="Apple Pie--110/-",variable=var21,background="White").grid(column=8,row=3)
                var22=tk.IntVar(window)
                B22=tk.Checkbutton(window,text="Bluberry Pastry--120/-",variable=var22,background="White").grid(column=8,row=4)
                var23=tk.IntVar(window)
                B23=tk.Checkbutton(window,text="Honey Cheesecake--100/-",variable=var23,background="White").grid(column=8,row=5)
                var24=tk.IntVar(window)
                B24=tk.Checkbutton(window,text="Mango Tarts--100/-",variable=var24,background="White").grid(column=8,row=6)
                var25=tk.IntVar(window)
                B25=tk.Checkbutton(window,text="Chocolate Moussie--90/-",variable=var25,background="White").grid(column=8,row=7)
                var26=tk.IntVar(window)
                B26=tk.Checkbutton(window,text="Affogato--120/-",variable=var26,background="White").grid(column=8,row=8)
                var27=tk.IntVar(window)
                B27=tk.Checkbutton(window,text="Tiramisu--200/-",variable=var27,background="White").grid(column=8,row=9)
                var28=tk.IntVar(window)
                B28=tk.Checkbutton(window,text="Pudding--130/-",variable=var28,background="White").grid(column=8,row=10)
                var29=tk.IntVar(window)
                B29=tk.Checkbutton(window,text="Chocolate icecream--80/-",variable=var29,background="White").grid(column=8,row=11)
                var30=tk.IntVar(window)
                B30=tk.Checkbutton(window,text="Mango Milkshake--100/-",variable=var30,background="White").grid(column=8,row=12)

                Enter_button=tk.Button(window, text="Enter", command=callback)
                Enter_button.grid(column=6, row=13)

                qty_list=["0","1","2","3","4","5"]
                variable1=tk.StringVar(window)
                variable1.set(qty_list[0])
                field2=tk.OptionMenu(window,variable1,*qty_list)
                field2.grid(column=5,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable2=tk.StringVar(window)
                variable2.set(qty_list[0])
                field2=tk.OptionMenu(window,variable2,*qty_list)
                field2.grid(column=5,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable3=tk.StringVar(window)
                variable3.set(qty_list[0])
                field2=tk.OptionMenu(window,variable3,*qty_list)
                field2.grid(column=5,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable4=tk.StringVar(window)
                variable4.set(qty_list[0])
                field2=tk.OptionMenu(window,variable4,*qty_list)
                field2.grid(column=5,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable5=tk.StringVar(window)
                variable5.set(qty_list[0])
                field2=tk.OptionMenu(window,variable5,*qty_list)
                field2.grid(column=5,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable6=tk.StringVar(window)
                variable6.set(qty_list[0])
                field2=tk.OptionMenu(window,variable6,*qty_list)
                field2.grid(column=5,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable7=tk.StringVar(window)
                variable7.set(qty_list[0])
                field2=tk.OptionMenu(window,variable7,*qty_list)
                field2.grid(column=5,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable8=tk.StringVar(window)
                variable8.set(qty_list[0])
                field2=tk.OptionMenu(window,variable8,*qty_list)
                field2.grid(column=5,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable9=tk.StringVar(window)
                variable9.set(qty_list[0])
                field2=tk.OptionMenu(window,variable9,*qty_list)
                field2.grid(column=5,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable10=tk.StringVar(window)
                variable10.set(qty_list[0])
                field2=tk.OptionMenu(window,variable10,*qty_list)
                field2.grid(column=5,row=12)

                qty_list=["0","1","2","3","4","5"]
                variable11=tk.StringVar(window)
                variable11.set(qty_list[0])
                field2=tk.OptionMenu(window,variable11,*qty_list)
                field2.grid(column=7,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable12=tk.StringVar(window)
                variable12.set(qty_list[0])
                field2=tk.OptionMenu(window,variable12,*qty_list)
                field2.grid(column=7,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable13=tk.StringVar(window)
                variable13.set(qty_list[0])
                field2=tk.OptionMenu(window,variable13,*qty_list)
                field2.grid(column=7,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable14=tk.StringVar(window)
                variable14.set(qty_list[0])
                field2=tk.OptionMenu(window,variable14,*qty_list)
                field2.grid(column=7,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable15=tk.StringVar(window)
                variable15.set(qty_list[0])
                field2=tk.OptionMenu(window,variable15,*qty_list)
                field2.grid(column=7,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable16=tk.StringVar(window)
                variable16.set(qty_list[0])
                field2=tk.OptionMenu(window,variable16,*qty_list)
                field2.grid(column=7,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable17=tk.StringVar(window)
                variable17.set(qty_list[0])
                field2=tk.OptionMenu(window,variable17,*qty_list)
                field2.grid(column=7,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable18=tk.StringVar(window)
                variable18.set(qty_list[0])
                field2=tk.OptionMenu(window,variable18,*qty_list)
                field2.grid(column=7,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable19=tk.StringVar(window)
                variable19.set(qty_list[0])
                field2=tk.OptionMenu(window,variable19,*qty_list)
                field2.grid(column=7,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable20=tk.StringVar(window)
                variable20.set(qty_list[0])
                field2=tk.OptionMenu(window,variable20,*qty_list)
                field2.grid(column=7,row=12)


                qty_list=["0","1","2","3","4","5"]
                variable21=tk.StringVar(window)
                variable21.set(qty_list[0])
                field2=tk.OptionMenu(window,variable21,*qty_list)
                field2.grid(column=9,row=3)

                qty_list=["0","1","2","3","4","5"]
                variable22=tk.StringVar(window)
                variable22.set(qty_list[0])
                field2=tk.OptionMenu(window,variable22,*qty_list)
                field2.grid(column=9,row=4)

                qty_list=["0","1","2","3","4","5"]
                variable23=tk.StringVar(window)
                variable23.set(qty_list[0])
                field2=tk.OptionMenu(window,variable23,*qty_list)
                field2.grid(column=9,row=5)

                qty_list=["0","1","2","3","4","5"]
                variable24=tk.StringVar(window)
                variable24.set(qty_list[0])
                field2=tk.OptionMenu(window,variable24,*qty_list)
                field2.grid(column=9,row=6)

                qty_list=["0","1","2","3","4","5"]
                variable25=tk.StringVar(window)
                variable25.set(qty_list[0])
                field2=tk.OptionMenu(window,variable25,*qty_list)
                field2.grid(column=9,row=7)

                qty_list=["0","1","2","3","4","5"]
                variable26=tk.StringVar(window)
                variable26.set(qty_list[0])
                field2=tk.OptionMenu(window,variable26,*qty_list)
                field2.grid(column=9,row=8)

                qty_list=["0","1","2","3","4","5"]
                variable27=tk.StringVar(window)
                variable27.set(qty_list[0])
                field2=tk.OptionMenu(window,variable27,*qty_list)
                field2.grid(column=9,row=9)

                qty_list=["0","1","2","3","4","5"]
                variable28=tk.StringVar(window)
                variable28.set(qty_list[0])
                field2=tk.OptionMenu(window,variable28,*qty_list)
                field2.grid(column=9,row=10)

                qty_list=["0","1","2","3","4","5"]
                variable29=tk.StringVar(window)
                variable29.set(qty_list[0])
                field2=tk.OptionMenu(window,variable29,*qty_list)
                field2.grid(column=9,row=11)

                qty_list=["0","1","2","3","4","5"]
                variable30=tk.StringVar(window)
                variable30.set(qty_list[0])
                field2=tk.OptionMenu(window,variable30,*qty_list)
                field2.grid(column=9,row=12)

                window.mainloop()

            
               
                
                bill_window=tk.Tk()
                bill_window.title("Payment")
                bill_window['background']='White'


                lbl1 = tk.Label(bill_window, text="Billing Invoice",font=("Arial",25),background="light Green",compound=tk.CENTER)
                lbl1.grid(column=4,row=0)
                lbl1 = tk.Label(bill_window, text="Bill Number:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=2)
                lbl1 = tk.Label(bill_window, text="Customer Name:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=4,row=1)

                lbl1 = tk.Label(bill_window, text="Date",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=5,row=2)
                lbl1 = tk.Label(bill_window, text="Choice",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=1)
                lbl1 = tk.Label(bill_window, text="Total Bill Amount:",font=("Arial",15),background="white",justify=tk.RIGHT)
                lbl1.grid(column=6,row=2)

                field1=tk.Entry(bill_window)
                field1.grid(column=5,row=1)

                choice_list=["Dine In","Take Away"]
                variable2=tk.StringVar(bill_window)
                variable2.set(choice_list[0])
                field2=tk.OptionMenu(bill_window,variable2,*choice_list)
                field2.grid(column=7,row=1)

                

                mydb=sql.connect(
                    host="localhost",
                    user="root",
                    charset="utf8",
                    passwd="110104",
                    auth_plugin='mysql_native_password',
                    database="evergreen_restaurant")
                mycursor=mydb.cursor()  
                def Payment():
                    CustomerName=field1.get()
                    command1=mycursor.execute("SELECT * FROM Billing")
                    command2=mycursor.fetchall()
                    for i in range(len(command2)):
                            if str(command2[i][1])==CustomerName:
                              
                               label1=tk.Label(bill_window, text=command2[i][0],background="white",font=("Arial",15),borderwidth=1, relief="solid")
                               label1.grid(column=4, row=i+3)
                    
                               label1=tk.Label(bill_window, text=command2[i][2],background="white",font=("Arial",15),borderwidth=1, relief="solid")
                               label1.grid(column=5, row=i+3)
                               if(variable2.get()=="Take Away"):
                                   query1=mycursor.execute("UPDATE billing SET Bill_Amt=Bill_Amt+30")
                                   lbl1=tk.Label(bill_window,text="Additional charges of 30/- added",background="white",font=("Arial",15)).grid(column=5,row=61)
                               label2=tk.Label(bill_window, text=command2[i][3],background="white",font=("Arial",15), borderwidth=1, relief="solid")
                               label2.grid(column=6, row=i+3)
                    
                   
                        
                B1=tk.Button(bill_window,text="Enter",command=Payment,background="White").grid(column=5,row=60)
                
                bill_window.mainloop()
            B1=tk.Button(staff_window,text="View Menu Table",command=View_Menu_Staff,width="30",background="white").grid(column=4,row=6)
            B2=tk.Button(staff_window,text="Take Order",command=Take_Order_Staff,width="30",background="white").grid(column=4,row=8)

            


    B1=tk.Button(login_window,text="Enter",command=check,background="White").grid(column=4,row=8)
                
                
B1=tk.Button(root,text="Login",font=("Arial",20),command=Login,compound=tk.CENTER).pack()

root.mainloop()
