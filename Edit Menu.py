
import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()

var1=tk.IntVar()

window.title("Restaurateur")
window['background']='White'
lbl1 = tk.Label(window, text="Edit Menu",font=("Arial",20),background="light green",compound=tk.CENTER)
lbl1.grid(column=4,row=0)
lbl1 = tk.Label(window, text="Update Items",font=("Arial",18),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=3)
lbl1 = tk.Label(window, text="Update Rate",font=("Arial",18),background="white",justify=tk.RIGHT)
lbl1.grid(column=4,row=4)

field1=tk.Entry()
field1.grid(column=5, row=4)

import mysql.connector as sql
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
        updateRate=field1.get()
        
        
        command1=mycursor.execute("SELECT * FROM menu")
        command2=mycursor.fetchall()
        count=0
  
        for i in range(len(command2)):
       
            if str(command2[i][0])==menu_list:
                
                if menu_list=="" or updateRate=="":
                    label2=tk.Label(window, text="Please enter all fields.")
                    label2.grid(column=4, row=7)
                
                elif menu_list!="" and updateRate!="" and updateRate.isdigit():
                    string1="UPDATE menu SET  Price=%s WHERE Item_name=%s"
                    val=(updateRate,menu_list)
                    mycursor.execute(string1, val)
                    label3=tk.Label(window, text="Item has been successfully edited.")
                    label3.grid(column=4, row=7)
                    mydb.commit()
                    count=1
                    print(count)
                    break
               
                
                elif  count==0 and updateRate.isdigit() is False:
                    label5=tk.Label(window, text="Please enter a numeric value for the Rate.")
                    label5.grid(column=4, row=7)
                    
                elif count==0:
                    label4=tk.Label(window,text="Sorry!Item does not exist")
                    label4.grid(column=4,row=7)
            
                
enter_button=tk.Button(window, text="Enter", command=check1)
enter_button.grid(column=4, row=6)

menu_list=["Veg Kababs","Paneer Tikka","Chilli Chicken","Aloo-Dal Tikki","Cheese Balls","Chicken Wings","Basil Chicken Cups","Potato Fries","Tomato Soup","Sweet Corn Soup","Lahori Paneer","Mushroom Buckwheat Risotto","Chicken Kadai","Lahori Kofta","Veg Kurma","Chana Masala","Vegetable Biryani","Spicy Vegan Potato Curry","Roti","Naan","Apple Pie","Bluberry Pastry","Honey Cheesecake","Mango Tarts","Chocolate Moussie","Affogato","Tiramisu","Pudding","Chocolate icecream","Mango Milkshake"]
variable1=tk.StringVar(window)
variable1.set(menu_list[0])
field4=tk.OptionMenu(window,variable1,*menu_list)
field4.grid(column=5,row=3)


window.mainloop()
