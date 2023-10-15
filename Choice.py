import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()
var1=tk.IntVar()


window.title("Food Choice")
window['background']='White'


lbl1 = tk.Label(window, text="Please Select Food Type",font=("Arial",20),background="light Green",justify=tk.RIGHT)
lbl1.grid(column=4,row=0)

B1=tk.Button(window,text="Eat In Here",command=select,background="White").grid(column=4,row=8)
B2=tk.Button(window,text="Take-Away",command=select,background="White").grid(column=4,row=10)


window.mainloop()
