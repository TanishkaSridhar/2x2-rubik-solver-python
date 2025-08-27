#import tkinter
#from tkinter import *
#from tkinter import ttk
#from tkinter import messagebox
import pymysql
import pytwisty
from movesmodule import *

def cubesolv():
   #connection establishmnet
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
   cll=[]
   mycursor.execute("select *from cubecolorf")
   result = mycursor.fetchone()     
   cll=result[2:]
   for j in range(len(cll)):
      print(cll[j])
   s=""
   for i in cll:
      s+=i
   #using pytwisty module
   x=list(pytwisty.solve222(s))  
       
   
   k=1
   for i in x:
       if i=="F":
           cll=F(cll)
       elif i=="B":
           cll=B(cll)
       elif i=="R":
           cll=R(cll)
       elif i=="L":
           cll=L(cll)
       elif i=="U":
           cll=U(cll)
       elif i=="D":
           cll=D(cll)
       elif i=="F'":
           cll=Fp(cll)
       elif i=="B'":
           cll=Bp(cll)
       elif i=="R'":
           cll=Rp(cll)
       elif i=="L'":
           cll=Lp(cll)
       elif i=="U'":
           cll=Up(cll)
       elif i=="D'":
           cll=Dp(cll)
       elif i=="F2":
           cll=F2(cll)
       elif i=="B2":
           cll=B2(cll)
       elif i=="L2":
           cll=L2(cll)
       elif i=="R2":
           cll=R2(cll)
       elif i=="U2":
           cll=U2(cll)
       elif i=="D2":
           cll=D2(cll)
       elif i=="F2'":
           cll=F2p(cll)
       elif i=="B2'":
           cll=B2p(cll)
       elif i=="L2'":
           cll=L2p(cll)
       elif i=="R2'":
           cll=R2p(cll)
       elif i=="D2'":
           cll=D2p(cll)
       elif i=="U2'":
           cll=U2p(cll)
       elif i=="y":
           cll=y(cll)
       elif i=="y2":
           cll=y2(cll)
       
       mycursor.execute('insert into cubecolorf values({},"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(k,i,cll[0],cll[1],cll[2],cll[3],cll[4],cll[5],cll[6],cll[7],cll[8],cll[9],cll[10],cll[11],cll[12],cll[13],cll[14],cll[15],cll[16],cll[17],cll[18],cll[19],cll[20],cll[21],cll[22],cll[23]))
       k+=1
       mydb.commit()
       
           
       
   #'BWRRWWYGOYYWGBGOBBGRORYO'
   print("enter to get your instruction and 'stop' to end")
   i=0
   while True:
       y=input("")
       if y=="":
           print(x[i])
           
       if i<len(x)-1:
           i+=1
       else:
           break
   print("the cube has been solved!!!")




