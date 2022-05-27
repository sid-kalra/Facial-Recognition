from tkinter import*
from tkinter import ttk
import importlib
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
from train import Train
from recognizer import Recognition
from attendance import Attendance
import os
import cv2
from time import strftime
from datetime import datetime
import pymysql
#importing all the libraries

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #bg image
        img4 =Image.open(r"photos\background3.jpg")
        img4=img4.resize((1530,930),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=930)
        
        #title of page
        title_lbl=Label(self.root,text="ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",40,"bold"),fg="red",bg="#171717")
        title_lbl.place(x=0,y=100,width=1530,height=50)
        
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background="#171717",foreground="#185ADB")
        lbl.place(x=110,y=(0),width=110,height=50)
        time()
        
        myname=Label(self.root,text="Developed by: Siddharth Kalra",font=("sans-serif",15,"bold"),bg="#171717",fg="white")
        myname.place(x=1220,y=750)
        
        #student button
        img5 =Image.open(r"photos\student.jpg")
        img5=img5.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=230,width=250,height=220)
        
        b1_1=Button(bg_img,text="Add Student Details",command=self.student_details,cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=430,width=250,height=40)
        
        
        #detect face button
        img6 =Image.open(r"photos\face2.png")
        img6=img6.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b2=Button(bg_img,image=self.photoimg6,command=self.open_recognizer,cursor="hand2")
        b2.place(x=650,y=230,width=250,height=220)
        
        b2_1=Button(bg_img,text="Detect Face" ,command=self.open_recognizer, cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b2_1.place(x=650,y=430,width=250,height=40)
        
        
        #attendance button
        img7 =Image.open(r"photos\attendance.jpg")
        img7=img7.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b3=Button(bg_img,image=self.photoimg7,command=self.attend_data,cursor="hand2")
        b3.place(x=1100,y=230,width=250,height=220)
        
        b3_1=Button(bg_img,text="Attendance" ,command=self.attend_data, cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b3_1.place(x=1100,y=430,width=250,height=40)
        

        #Train data button
        img9 =Image.open(r"photos\train.webp")
        img9=img9.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b5=Button(bg_img,command=self.train_data,image=self.photoimg9,cursor="hand2")
        b5.place(x=200,y=510,width=250,height=220)
        
        b5_1=Button(bg_img,command=self.train_data,text="Train Data",cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b5_1.place(x=200,y=710,width=250,height=40)
        
        
        #Photos button
        img10 =Image.open(r"photos\images.png")
        img10=img10.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b6=Button(bg_img,command=self.open_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=650,y=510,width=250,height=220)
        
        b6_1=Button(bg_img,text="Photos Database" ,command=self.open_img, cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b6_1.place(x=650,y=710,width=250,height=40)
        
        #Exit button
        img12 =Image.open(r"photos\exit.jpg")
        img12=img12.resize((250,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        b8=Button(bg_img,command=self.exit,image=self.photoimg12,cursor="hand2")
        b8.place(x=1100,y=510,width=250,height=220)
        
        b8_1=Button(bg_img,command=self.exit,text="Exit App" , cursor="hand2", font=("sans-serif",15,"bold"),bg="white",fg="black")
        b8_1.place(x=1100,y=710,width=250,height=40)
     
    #exit button    
    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Do you want to exit the project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return
    
    #Function Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def open_img(self):
        os.startfile("data")
    
    def open_recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition(self.new_window)
        
    def attend_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()