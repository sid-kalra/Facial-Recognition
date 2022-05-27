from ast import Return
import importlib
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import cvtColor 
import mysql.connector
from numpy import delete
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # self.wm_iconbitmap("icon.ico")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="#185ADB")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background="white",foreground="#185ADB")
        lbl.place(x=110,y=(0),width=110,height=50)
        time()
        
        img_top =Image.open(r"photos\face1.webp")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=730)
        
        #back button
        b1_1=Button(self.root,command=self.back_data,text="Back",cursor="hand2", font=("sans-serif",12,"bold"),bg="#0AA1DD",fg="White")
        b1_1.place(x=5,y=10,width=100,height=30)
        
        
        #Train data button
        b1=Button(self.root,command=self.train_classifier,text="Train data",cursor="hand2",font=("sans-serif",30,"bold"),bg="red",fg="black",border=10)
        b1.place(x=710,y=665,width=300,height=60)
        
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #Train classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        self.back_data()
        messagebox.showinfo("Result","Training datasets completed")
        
    #back button    
    def back_data(self):
        self.root.destroy()
        
        

if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()