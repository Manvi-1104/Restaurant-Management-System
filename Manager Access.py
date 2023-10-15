import tkinter as tk

def select():
    sel=var1.get()
    lbl1.configure(text=sel)

window=tk.Tk()
var1=tk.IntVar()


window.title("Managers Access")
window['background']='White'


lbl1 = tk.Label(window, text="Choice",font=("Arial",20),background="light Green",justify=tk.RIGHT)
lbl1.grid(column=4,row=0)

B1=tk.Button(window,text="View Menu Table",command=select,width="20",background="white").grid(column=4,row=6)
B2=tk.Button(window,text="Dine-In Order",command=select,width="20",background="white").grid(column=4,row=8)
B3=tk.Button(window,text="Take-Away Order",command=select,width="20",background="white").grid(column=4,row=10)


window.mainloop()
