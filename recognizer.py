from ast import Return
import importlib
from inspect import CORO_CLOSED
from select import select
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import cvtColor, split 
import pymysql
from numpy import append, delete
import cv2
import os
import numpy as np
from student import Student
from time import strftime
from datetime import datetime
from datetime import date
import pymysql

class Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # self.wm_iconbitmap("icon.ico")
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("sans-serif",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #time button
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background="white",foreground="#185ADB")
        lbl.place(x=110,y=(0),width=110,height=50)
        time()
        
        img_top =Image.open(r"photos\face5.jpg")
        img_top=img_top.resize((1530,800),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=800)
        
        #back button
        b1_1=Button(self.root,command=self.back_data,text="Back",cursor="hand2", font=("sans-serif",12,"bold"),bg="#0AA1DD",fg="White")
        b1_1.place(x=5,y=10,width=100,height=30)
        
        
        b1=Button(self.root,text="Detect Face",command=self.face_recog,cursor="hand2",font=("sans-serif",30,"bold"),bg="#2155CD",fg="#E8F9FD",border=10)
        b1.place(x=290,y=370,width=400,height=80)
            
    #attendance
    def mark_attendance(self,i,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            now=datetime.now()
            d1=now.strftime("%d_%m_%Y")
            date1=date.today()
            date2=date(2022,5,24)
            var_total=(date1-date2).days
            var_total+=1
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i in name_list)):
                now=datetime.now()
                d1=now.strftime("%d_%m_%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtstring},{d1},Present")
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                x1="P"
                d2=str(d1)
                my_cursor.execute("Select 24_05_2022,25_05_2022,26_05_2022,27_05_2022,28_05_2022,29_05_2022, 30_05_2022,31_05_2022,01_06_2022,02_06_2022,03_06_2022,04_06_2022,05_06_2022,06_06_2022,07_06_2022,08_06_2022,09_06_2022,10_06_2022,11_06_2022,12_06_2022,13_06_2022,14_06_2022,15_06_2022,16_06_2022,17_06_2022,18_06_2022,19_06_2022,20_06_2022,21_06_2022,22_06_2022,23_06_2022,24_06_2022,25_06_2022,26_06_2022,27_06_2022,28_06_2022,29_06_2022,30_06_2022,01_07_2022,02_07_2022,03_07_2022,04_07_2022,05_07_2022 from attendancetable where Student_id=%s",(i,))
                x2=0
                myresult=my_cursor.fetchall()
                for x in myresult:
                    for j in x:
                        if  j=="P":
                            x2+=1
                x2=x2*100/var_total
                my_cursor.execute(f"Update attendancetable set Name=%s,Dep=%s,{d2}=%s,PERCENT=%s where Student_id=%s",(
                                        n,
                                        d,
                                        x1,
                                        x2,
                                        i
                ))  
                conn.commit()
                conn.close()
                  
            if (i not in name_list) :
                now=datetime.now()
                d1=now.strftime("%d_%m_%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtstring},{d1},Present")
                #Making connection to AWS
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                x1="P"
                d2=str(d1)
                x2=100/var_total
                #Making connection to AWS   
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute(f"insert into attendancetable (Student_id,Name,Dep,{d2},PERCENT) values(%s,%s,%s,%s,%s)",(
                                        i,
                                        n,
                                        d,
                                        x1,
                                        x2
                ))
                conn.commit()
                conn.close()
        
    #Face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            cordinates=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                #Making connection to AWS
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()

                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)             
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                if confidence>75:
                    cv2.putText(img,f"Id:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)                    
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    self.mark_attendance(i,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                cordinates=[x,y,w,h]
            return cordinates
        def recog(img,clf,faceCascade):
            cordinates=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while True:
            ret,img=video_cap.read()
            img=recog(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
            k=cv2.waitKey(1)
            if ((k==13 or k==27 or k==ord("q"))) :
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
        
    #back button    
    def back_data(self):
        self.root.destroy()

if __name__== "__main__":
    root=Tk()
    obj=Recognition(root)
    root.mainloop()
    