import initialstatecube as isc
import finalstatecube as fsc
import cubesolve as cs
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
#creating window
window= Tk()
window.title("2X2 RUBIK'S CUBE SOLVER") 
window.geometry('700x700')
window.configure(bg='lightblue')
#database connection establishment
mydb = mysql.connector.connect(  host="localhost",user="root", password="root",database="cubedb")
mycur=mydb.cursor()
choices=["B","G","O","R","W","Y"]
clicked1=tkinter.StringVar()
clicked1.set("select")
clicked2=tkinter.StringVar()
clicked2.set("select")
clicked3=tkinter.StringVar()
clicked3.set("select")
clicked4=tkinter.StringVar()
clicked4.set("select")
clicked5=tkinter.StringVar()
clicked5.set("select")
clicked6=tkinter.StringVar()
clicked6.set("select")
clicked7=tkinter.StringVar()
clicked7.set("select")
clicked8=tkinter.StringVar()
clicked8.set("select")
clicked9=tkinter.StringVar()
clicked9.set("select")
clicked10=tkinter.StringVar()
clicked10.set("select")
clicked11=tkinter.StringVar()
clicked11.set("select")
clicked12=tkinter.StringVar()
clicked12.set("select")
clicked13=tkinter.StringVar()
clicked13.set("select")
clicked14=tkinter.StringVar()
clicked14.set("select")
clicked15=tkinter.StringVar()
clicked15.set("select")
clicked16=tkinter.StringVar()
clicked16.set("select")
clicked17=tkinter.StringVar()
clicked17.set("select")
clicked18=tkinter.StringVar()
clicked18.set("select")
clicked19=tkinter.StringVar()
clicked19.set("select")
clicked20=tkinter.StringVar()
clicked20.set("select")
clicked21=tkinter.StringVar()
clicked21.set("select")
clicked22=tkinter.StringVar()
clicked22.set("select")
clicked23=tkinter.StringVar()
clicked23.set("select")
clicked24=tkinter.StringVar()
clicked24.set("select")

#creating drop boxes in approproate position of the window to get the colour values 
lab1=Label(window,text="ENTER THE FRONT FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=30)
drop1=tkinter.OptionMenu(window,clicked1,*choices)
drop1.place(x=20,y=70)
drop2=tkinter.OptionMenu(window,clicked2,*choices)
drop2.place(x=120,y=70)
drop3=tkinter.OptionMenu(window,clicked3,*choices)
drop3.place(x=220,y=70)
drop4=tkinter.OptionMenu(window,clicked4,*choices)
drop4.place(x=320,y=70)

lab2=Label(window,text="ENTER THE LEFT FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=110)
drop5=tkinter.OptionMenu(window,clicked5,*choices)
drop5.place(x=20,y=150)
drop6=tkinter.OptionMenu(window,clicked6,*choices)
drop6.place(x=120,y=150)
drop7=tkinter.OptionMenu(window,clicked7,*choices)
drop7.place(x=220,y=150)
drop8=tkinter.OptionMenu(window,clicked8,*choices)
drop8.place(x=320,y=150)

lab3=Label(window,text="ENTER THE RIGHT FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=190)
drop9=tkinter.OptionMenu(window,clicked9,*choices)
drop9.place(x=20,y=230)
drop10=tkinter.OptionMenu(window,clicked10,*choices)
drop10.place(x=120,y=230)
drop11=tkinter.OptionMenu(window,clicked11,*choices)
drop11.place(x=220,y=230)
drop12=tkinter.OptionMenu(window,clicked12,*choices)
drop12.place(x=320,y=230)

lab4=Label(window,text="ENTER THE TOP FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=270)
drop13=tkinter.OptionMenu(window,clicked13,*choices)
drop13.place(x=20,y=310)
drop14=tkinter.OptionMenu(window,clicked14,*choices)
drop14.place(x=120,y=310)
drop15=tkinter.OptionMenu(window,clicked15,*choices)
drop15.place(x=220,y=310)
drop16=tkinter.OptionMenu(window,clicked16,*choices)
drop16.place(x=320,y=310)

lab5=Label(window,text="ENTER THE BOTTOM FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=350)
drop17=tkinter.OptionMenu(window,clicked17,*choices)
drop17.place(x=20,y=390)
drop18=tkinter.OptionMenu(window,clicked18,*choices)
drop18.place(x=120,y=390)
drop19=tkinter.OptionMenu(window,clicked19,*choices)
drop19.place(x=220,y=390)
drop20=tkinter.OptionMenu(window,clicked20,*choices)
drop20.place(x=320,y=390)

lab6=Label(window,text="ENTER THE BACK FACE VALES OF 2X2 RUBIK'S CUBE").place(x=10,y=430)
drop21=tkinter.OptionMenu(window,clicked21,*choices)
drop21.place(x=20,y=470)
drop22=tkinter.OptionMenu(window,clicked22,*choices)
drop22.place(x=120,y=470)
drop23=tkinter.OptionMenu(window,clicked23,*choices)
drop23.place(x=220,y=470)
drop24=tkinter.OptionMenu(window,clicked24,*choices)
drop24.place(x=320,y=470)

#using drop boxes colour values of each cuboid is received form the user
def savedata():
    L1=clicked1.get()
    L2=clicked2.get()
    L3=clicked3.get()
    L4=clicked4.get()
    L5=clicked5.get()
    L6=clicked6.get()
    L7=clicked7.get()
    L8=clicked8.get()
    L9=clicked9.get()
    L10=clicked10.get()
    L11=clicked11.get()
    L12=clicked12.get()
    L13=clicked13.get()
    L14=clicked14.get()
    L15=clicked15.get()
    L16=clicked16.get()
    L17=clicked17.get()
    L18=clicked18.get()
    L19=clicked19.get()
    L20=clicked20.get()
    L21=clicked21.get()
    L22=clicked22.get()
    L23=clicked23.get()
    L24=clicked24.get()
    if((L1=="select")or(L2=="select")or(L3=="select")or(L4=="select")or(L5=="select")or(L6=="select")or(L7=="select")or(L8=="select")or(L9=="select")or(L10=="select")or(L11=="select")or(L12=="select")or(L13=="select")or(L14=="select")or(L15=="select")or(L16=="select")or(L17=="select")or(L18=="select")or(L19=="select")or(L20=="select")or(L21=="select")or(L22=="select")or(L23=="select")or(L24=="select")):
        print("selct an option")
        messagebox.showinfo("Alert","select all color options")
    else:
        #mycur.execute("create table if not exists colorcubef(stepno int, step varchar(5),l1 char,l2 char,l3 char,l4 char,l5 char,l6 char,l7 char,l8 char,l9 char, l10 char, l11 char, l12 char, l13 char, l14 char, l15 char, l16 char, l17 char, l18 char, l19 char, l20 char, l21 char, l22 char, l23 char, l24 char")
        mycur.execute("delete from cubecolorf")
        z=0
        #sroring the received colour values in database
        mycur.execute("insert into cubecolorf(stepno,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24)values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(z,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24))
        mydb.commit()
        messagebox.showinfo("success","Colour data inserted successfully")
        global cll
        cll=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24]

#creating buttons in the window to do the appropriate operations
cll=[]
btn=Button(window,text="Save",command=savedata)
btn.place(x=340,y=530)

btn2=Button(window,text="Display Initail State",command=isc.cubeprint)
btn2.place(x=340,y=560)

btn3=Button(window,text="Solve",command=cs.cubesolv)
btn3.place(x=340,y=590)

btn4=Button(window,text="Display Final State",command=fsc.cubeprint)
btn4.place(x=340,y=620)

#closing the created window
window.mainloop()







