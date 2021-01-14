from tkinter import *

class FahraheittoC:
    def __init__(self,master):
        self.master = master
        master.title("FahrenhiettoCelsius")
        
        def Celsius_to_Fahrenheit():
            fah=(self.Entry.get())
            fah=float(fah)
            cel=(fah-32)*5/9
            datanum1.set(cel)
            if(cel<0):
                datachar1.set("Absolute zero temperature")
            elif(cel>=0 and cel<21.11):
                datachar1.set("Freezing/melting point of water")
            elif(cel>=21.11 and cel<37):
                datachar1.set("room temperature")
            elif(cel>=37 and cel<100):
                datachar1.set("Average body Temperature")
            elif(cel>=100):
                datachar1.set("Boiling point of water")
            else:
                datachar1.set("Wrong input")

        def Reset():
            fah.set("")
            datanum1.set("")
            datachar1.set("")

        def Swap():
            setting1.set("")
            settingmain1.set("")
            datanum1.set("")
            datachar1.set("")
            fah=CelsiustoF(app)

        datanum1=StringVar()
        datachar1=StringVar()
        fah=StringVar()
        setting1=StringVar()
        setting1.set("Celsius:")
        settingmain1=StringVar()
        settingmain1.set("Fahrenheit:")
        
        self.label=Label(master,textvariable=settingmain1,font=("Arial Bold", 16))
        self.label.place(x=10, y=8)

        self.Entry=Entry(master,textvariable = fah,font=("Arial Bold", 15),borderwidth=2, relief="solid")
        self.Entry.place(x=145, y=10)

        self.Button1=Button(master,text="Convert",font=("Arial Bold",15),command=Celsius_to_Fahrenheit)
        self.Button1.place(x=13,y=55)

        self.Button2=Button(master,text="Reset",font=("Arial Bold",15),command=Reset)
        self.Button2.place(x=115,y=55)

        self.Button3=Button(master,text="Swap",font=("Arial Bold",15),command=Swap)
        self.Button3.place(x=200,y=55)

        self.label1=Label(master,textvariable=setting1,font=("Arial Bold", 18))
        self.label1.place(x=10, y=115)

        self.label3=Label(master,textvariable=datanum1,font=("Arial Bold", 18),height=1, borderwidth=2, relief="solid")
        self.label3.place(x=145, y=115)

        self.label4=Label(master,textvariable=datachar1,font=("Arial Bold", 18),height=1, borderwidth=2, relief="solid")
        self.label4.place(x=10, y=175)

##################################################################################################################################

class CelsiustoF:
    def __init__(self,master):
        self.master = master
        master.title("CelsuistoFahrenheit")
        


        def Celsius_to_Fahrenheit():
            cel=(self.Entry.get())
            cel=float(cel)
            fah=(cel*9/5)+32
            datanum.set(fah)
            if(fah<32):
                datachar.set("Absolute zero temperature")
            elif(fah>=32 and fah<69.8):
                datachar.set("Freezing/melting point of water")
            elif(fah>=69.8 and fah<98.6):
                datachar.set("room temperature")
            elif(fah>=98.6 and fah<212.0):
                datachar.set("Average body Temperature")
            elif(fah>=212.0):
                datachar.set("Boiling point of water")
            else:
                datachar.set("Wrong input")

        def Reset():
            Cel.set("")
            datanum.set("")
            datachar.set("")

        def Swap():
            setting.set("")
            settingmain.set("")
            datanum.set("")
            datachar.set("")
            fah=FahraheittoC(app)

        datanum=StringVar()
        datachar=StringVar()
        Cel=StringVar()
        setting=StringVar()
        setting.set("Fahrenheit:")
        settingmain=StringVar()
        settingmain.set("Celsius:")
        
        self.label=Label(master,textvariable=settingmain,font=("Arial Bold", 16))
        self.label.place(x=10, y=8)

        self.Entry=Entry(master,textvariable = Cel,font=("Arial Bold", 15),borderwidth=2, relief="solid")
        self.Entry.place(x=145, y=10)

        self.Button1=Button(master,text="Convert",font=("Arial Bold",15),command=Celsius_to_Fahrenheit)
        self.Button1.place(x=13,y=55)

        self.Button2=Button(master,text="Reset",font=("Arial Bold",15),command=Reset)
        self.Button2.place(x=115,y=55)

        self.Button3=Button(master,text="Swap",font=("Arial Bold",15),command=Swap)
        self.Button3.place(x=200,y=55)

        self.label1=Label(master,textvariable=setting,font=("Arial Bold", 18))
        self.label1.place(x=10, y=115)

        self.label3=Label(master,textvariable=datanum,font=("Arial Bold", 18),height=1, borderwidth=2, relief="solid")
        self.label3.place(x=145, y=115)

        self.label4=Label(master,textvariable=datachar,font=("Arial Bold", 18),height=1, borderwidth=2, relief="solid")
        self.label4.place(x=10, y=175)

        

app=Tk()
gui = CelsiustoF(app)
app.geometry("400x250")
app.mainloop()
