import pyqrcode
from tkinter import *
from PIL import Image,ImageTk

def generate():
    text=entry1.get()
    qr=pyqrcode.create(text)
    file="qr code"
    path=r"<path to be saved>"
    name = path+file+'.png'
    qr.png(name,scale=10)
    image=Image.open(name)
    image = image.resize((400,400),Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    root.image.config(image=image)
    root.image.photo = image

root=Tk()
root.title("QR code GENERATOR")
root.geometry("960x650+0+0")
root.config(background="powder blue")

text = Label(root,text="Enter or paste the link:",font=('times 26 bold'),bg="powder blue")
text.grid(row=0,column=0,padx=3,pady=3)

entry1 = Entry(root,width=40,font=("verdana",18))
entry1.grid(row=0,column=1,padx=4,pady=3)

Button1 =Button (root,text="GENERATE",font=('times 26 bold'),bg="BLUE",command=generate)
Button1.grid(row=1,column=1,padx=3,pady=3)

Showqr=Label(root,text="QR Code Shows below:",font=('times 26 bold'),bg="powder blue")
Showqr.grid(row=2,column=1,padx=3,pady=3)

root.image=Label(root,background="powder blue")
root.image.grid(row=3,column=1,padx=3,pady=3)

root.mainloop()
