import tkinter as tk
import tkinter.scrolledtext as tks
import datetime
from PIL import Image, ImageTk
saves = ""

def window():
    def strings(self):
        global saves
        saves = saves + str(datetime.datetime.now())[:-7]+ " ➣ " + textc.get("1.0",tk.END).strip() + "\n"
        textb['state'] = tk.NORMAL
        textb.delete("1.0",tk.END)
        textb.insert("insert", saves)
        textc.delete("1.0",tk.END)
        textc.delete("1.0")
        textb['state'] = tk.DISABLED
    root=tk.Ｔk()
    root.title("Chatting over it")
    root.resizable(0,0)
    root.geometry("500x500")
    img = Image.open('unknown.png')
    tk_img = ImageTk.PhotoImage(img.resize((100,100), Image.ANTIALIAS))
    sus = tk.Label(image=tk_img, width=100, height=100)
    sus.place(x=370,y=0)
    label=tk.Label(root,text="A simplified singular chatting box"+ "\n" +"Made by Joseph and Bernie",font=('Helvetica', 14))
    label.place(x=70,y=20)
    textc=tk.Text(root,height=2,width=60,border=1,font=('Helvetica', 10))
    textc.place(x=70,y=450)
    textb=tks.ScrolledText(root,height=20,width=58,border=1,state="disabled",font=('Helvetica', 10))
    textb.place(x=70,y=100)
    textc.bind("<Return>",strings)
    root.mainloop()
   
           
window()
