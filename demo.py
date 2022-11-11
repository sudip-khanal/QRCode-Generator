
import qrcode
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,filedialog



def create_qr(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data) #generate QRcode  
        res_img = img.resize((280,250)) # reszie QR Code Size
        #Convert To photoimage
        tkimage= ImageTk.PhotoImage(res_img)
        qr_canvas.delete('all')
        qr_canvas.create_image(0,0,anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning",'Enter Data in Entry First')

def save_qr(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data) #generate QRcode  
        res_img = img.resize((280,250)) # reszie QR Code Size
        
        path = filedialog.asksaveasfilename(defaultextension=".png",)
        if path:
            res_img.save(path)
            messagebox.showinfo("Sucess","QR Code is Saved ")
    else:
        messagebox.showwarning("Warning",'Enter Data in Entry First')
    



root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x380")
root.config(bg='white')
root.resizable(0,0)


frame1 = tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=30,y=5,width=280,height=250)

frame2 = tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=30,y=260,width=280,height=100)

qr_canvas = tk.Canvas(frame1)
qr_canvas.bind("<Double-1>",save_qr)
qr_canvas.create_image(0,0,anchor=tk.NW)
# qr_canvas.image = coverImg
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2,width=26,font=("Sitka Small",11),justify=tk.CENTER)
text_entry.bind("<Return>",create_qr)
text_entry.place(x=5,y=5)

btn_1 = ttk.Button(frame2,text="Create",width=10,command=create_qr)
btn_1.place(x=25,y=50)

btn_2 = ttk.Button(frame2,text="Save",width=10,command=save_qr)
btn_2.place(x=100,y=50)

btn_3 = ttk.Button(frame2,text="Exit",width=10,command=root.quit)
btn_3.place(x=175,y=50)


root.mainloop()