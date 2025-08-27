import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def cubeprint():
    #window creation
    window= Tk()
    window.title("2X2 RUBIK'S CUBE SOLVER") 
    window.geometry('700x700')
    window.configure(bg='lightblue')
    #database connection establishmnet 
    mydb = pymysql.connect(  host="localhost",user="root", password="root",database="cubedb")
    mycur=mydb.cursor()

    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="cubedb"
    )

    Bl=(0,0,0)
    mycursor = mydb.cursor()
    #fetching the solved step from database
    mycursor.execute("select *from cubecolorf order by stepno desc")
    result = mycursor.fetchone()     
    cl=result[2:]

    # Creating Canvas widget
    canvas = tkinter.Canvas(window, width=700, height=700, bg="black")
    canvas.pack()
    count=0
    size=(20,20)
    #assigning colour code
    for i in range(len(cl)):
        print(i)
        if cl[i]=="B":
            color="#0000FF"
        elif cl[i]=="G":
            color="#00FF00"
        elif cl[i]=="O":
            color="#FFA500"
        elif cl[i]=="R":
            color="#FF0000"
        elif cl[i]=="W":
            color="#FFFFFF"
        elif cl[i]=="Y":
            color="#FFFF00"
        #printing in cube shape
        # Assigning appropriate position and colour code for each cuboid   
        if i==0:
            x1=300
            y1=150
            x2=320
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==1:
            x1=325
            y1=150
            x2=345
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==2:
            x1=325
            y1=175
            x2=345
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==3:
            x1=300
            y1=175
            x2=320
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==4:
            x1=245
            y1=150
            x2=265
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==5:
            x1=270
            y1=150
            x2=290
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==6:
            x1=270
            y1=175
            x2=290
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==7:
            x1=245
            y1=175
            x2=265
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==8:
            x1=355
            y1=150
            x2=375
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==9:
            x1=380
            y1=150
            x2=400
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==10:
            x1=380
            y1=175
            x2=400
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==11:
            x1=355
            y1=175
            x2=375
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==12:
            x1=300
            y1=95
            x2=320
            y2=115
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==13:
            x1=325
            y1=95
            x2=345
            y2=115
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==14:
            x1=325
            y1=120
            x2=345
            y2=140
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==15:
            x1=300
            y1=120
            x2=320
            y2=140
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==16:
            x1=300
            y1=205
            x2=320
            y2=225
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==17:
            x1=325
            y1=205
            x2=345
            y2=225
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==18:
            x1=325
            y1=230
            x2=345
            y2=250
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==19:
            x1=300
            y1=230
            x2=320
            y2=250
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==20:
            x1=410
            y1=150
            x2=430
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==21:
            x1=435
            y1=150
            x2=455
            y2=170
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==22:
            x1=435
            y1=175
            x2=455
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
        elif i==23:
            x1=410
            y1=175
            x2=430
            y2=195
            rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill=color)
    
    window.mainloop()
