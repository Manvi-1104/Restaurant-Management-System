import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)
def image(smp):
    img = tk.PhotoImage(file="C:/Users/Intel/Documents/Screencast-O-Matic/Screenshots/Screenshot - Why Consider Going Green During a Restaurant Renovation  Renovation and Interior Design.png")
    img = img.subsample(smp, smp)
    return img

root=tk.Tk()

menu = tk.Menu()
menu.add_command(label="Quit", command=root.destroy)
root.config(menu=menu)
 
var1=tk.IntVar()

root.title("Restaurant Management")
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
 
lbl1 = tk.Label(root, text="Evergreen Restaurant",font=("Arial",45),background="light Green",compound=tk.CENTER)
lbl1.pack()
img = image(2) # 1=normal, 2=small, 3=smallest
ImgButton.config(image=img)
ImgButton.pack()
  
B1=tk.Button(root,text="Dine In",font=("Arial",20),command=select,compound=tk.CENTER).pack()
B2=tk.Button(root,text="Room Service",font=("Arial",20),command=select).pack()


root.mainloop()
