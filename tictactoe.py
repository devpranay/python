from tkinter import *
import tkinter.messagebox

def newgame():
    button1['text']=" "
    button1.configure(background = "gainsboro")
    button2['text']=" "
    button2.configure(background = "gainsboro")
    button3['text']=" "
    button3.configure(background = "gainsboro")
    button4['text']=" "
    button4.configure(background = "gainsboro")
    button5['text']=" "
    button5.configure(background = "gainsboro")
    button6['text']=" "
    button6.configure(background = "gainsboro")
    button7['text']=" "
    button7.configure(background = "gainsboro")
    button8['text']=" "
    button8.configure(background = "gainsboro")
    button9['text']=" "
    button9.configure(background = "gainsboro")

root=Tk()
root.geometry("960x650+0+0")
root.title("TIC TAC TOE")
root.configure(background = "orange")


top =Frame(root, bg="orange",pady=2,width=1350,height=100,relief=RIDGE)
top.grid(row=0,column=0)

lbl1 =Label(top,font=('arial',50,'bold'),text="TIC TAC TOE",bd=21,bg="orange",fg='white', justify=CENTER)
lbl1.grid(row=0,column=0)

main=Frame(root,bg='yellow',bd=10,width=1350,height=600,relief=RIDGE)
main.grid(row=1,column=0)

left=Frame(main,bd=10,width=400,height=500,pady=10,padx=2,bg="yellow",relief=RIDGE)
left.pack(side=LEFT)



right=Frame(main,bd=10,width=750,height=500,pady=10,padx=2,bg="yellow",relief=RIDGE)
right.pack(side=RIGHT)



X=IntVar()
O=IntVar()

X.set(0)
O.set(0)

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if(buttons["text"] ==" " and click == True):
        buttons["text"] = "X"
        buttons.configure(background="red")
        click = False
    elif(buttons["text"] ==" " and click == False):
        buttons["text"] = "O"
        buttons.configure(background="green")
        click = True 
    score()


def score():
    if(button1["text"]=="X" and button2["text"] == "X" and button3["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")
        
    elif(button4["text"]=="X" and button5["text"] == "X" and button6["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")

    elif(button7["text"]=="X" and button8["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")

    elif(button1["text"]=="X" and button5["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")

    elif(button3["text"]=="X" and button5["text"] == "X" and button7["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")
    
    
    elif(button1["text"]=="X" and button4["text"] == "X" and button7["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")

    elif(button2["text"]=="X" and button5["text"] == "X" and button8["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")

    elif(button3["text"]=="X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("You won a game","WINNER X")



    elif(button1["text"]=="O" and button2["text"] == "O" and button3["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")

    elif(button4["text"]=="O" and button5["text"] == "O" and button6["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")

    elif(button7["text"]=="O" and button8["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")

    elif(button1["text"]=="O" and button5["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("Winner O","You won a game")

    elif(button3["text"]=="O" and button5["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")

    elif(button1["text"]=="O" and button4["text"] == "O" and button7["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")

    elif(button2["text"]=="O" and button5["text"] == "O" and button8["text"] == "O"):
        tkinter.messagebox.showinfo("Winner O","You won a game")

    elif(button3["text"]=="O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("You won a game","WINNER O")




button1 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(right,text=" ",font=('times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

newbutton=Button(left,text="NEW-GAME",font=('times 26 bold'),height=1,width=15,bg='gainsboro',command=newgame)
newbutton.pack()


root.mainloop()





