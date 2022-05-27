from ast import Return
from atexit import register
import importlib
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import cvtColor 
import pymysql
from numpy import delete
import cv2
from time import strftime
from datetime import datetime
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_std_id=StringVar()
        self.var_std=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_search=StringVar()
        self.var_search_combo=StringVar()
     
        #image2
        img2 =Image.open(r"photos\student2.jpg")
        img2=img2.resize((1540,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=0,width=1540,height=130)
        
        #back button
        b1_1=Button(self.root,command=self.back_data,text="Back",cursor="hand2", font=("sans-serif",12,"bold"),bg="#0AA1DD",fg="White")
        b1_1.place(x=5,y=20,width=100,height=30)
        
        #bg image
        img4 =Image.open(r"photos\History-of-Facial-Recognition-Technology.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Management",font=("sans-serif",34,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background="white",foreground="#185ADB")
        lbl.place(x=110,y=(0),width=110,height=50)
        time()
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1490,height=600)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Add New Student",font=("sans-serif",18,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=550,height=588)
        
        #Department
        dep_label=Label(Left_frame,text="Department",font=("sans-serif",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=50,pady=10,sticky=W)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("sans-serif",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,pady=10,padx=50,sticky=W)
        
        
        #year
        year_label=Label(Left_frame,text="Year",font=("sans-serif",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=50,pady=10,sticky=W)
        year_combo=ttk.Combobox(Left_frame,textvariable=self.var_year,font=("sans-serif",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,pady=10,padx=50,sticky=W)
        
        #studentid
        studentId_label=Label(Left_frame,text="StudentID",font=("sans-serif",13,"bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=50,pady=10,sticky=W)
        
        studentId_entry=ttk.Entry(Left_frame,textvariable=self.var_std_id,width=20,font=("sans-serif",13,"bold"))
        studentId_entry.grid(row=2,column=1,padx=50,pady=10,sticky=W)
        
        #studentName
        studentName_label=Label(Left_frame,text="Student Name",font=("sans-serif",13,"bold"),bg="white")
        studentName_label.grid(row=3,column=0,padx=50,pady=10,sticky=W)
        
        studentName_entry=ttk.Entry(Left_frame,textvariable=self.var_std,width=20,font=("sans-serif",13,"bold"))
        studentName_entry.grid(row=3,column=1,padx=50,pady=10,sticky=W)
        
        
        #Gender
        Gender_label=Label(Left_frame,text="Gender",font=("sans-serif",13,"bold"),bg="white")
        Gender_label.grid(row=4,column=0,padx=50,pady=10,sticky=W)
        
        Gender_combo=ttk.Combobox(Left_frame,textvariable=self.var_gender,font=("sans-serif",12,"bold"),width=20,state="readonly")
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=4,column=1,pady=10,padx=50,sticky=W)
        
        #dob
        DOB_label=Label(Left_frame,text="DOB",font=("sans-serif",13,"bold"),bg="white")
        DOB_label.grid(row=5,column=0,padx=50,pady=10,sticky=W)
        
        DOB_entry=ttk.Entry(Left_frame,textvariable=self.var_dob,width=20,font=("sans-serif",13,"bold"))
        DOB_entry.grid(row=5,column=1,padx=50,pady=10,sticky=W)
        
        #email
        Email_label=Label(Left_frame,text="Email",font=("sans-serif",13,"bold"),bg="white")
        Email_label.grid(row=6,column=0,padx=50,pady=10,sticky=W)
        
        Email_entry=ttk.Entry(Left_frame,textvariable=self.var_email,width=20,font=("sans-serif",13,"bold"))
        Email_entry.grid(row=6,column=1,padx=50,pady=10,sticky=W)
        
        #phone no
        Phone_label=Label(Left_frame,text="Phone Number",font=("sans-serif",13,"bold"),bg="white")
        Phone_label.grid(row=7,column=0,padx=50,pady=10,sticky=W)
        
        Phone_entry=ttk.Entry(Left_frame,textvariable=self.var_phone,width=20,font=("sans-serif",13,"bold"))
        Phone_entry.grid(row=7,column=1,padx=50,pady=10,sticky=W)
        
        
        #radio buttons
        self.var_radio=StringVar()
        rb1=ttk.Radiobutton(Left_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        rb1.grid(row=8,column=0,padx=50,pady=10,sticky=W)
        rb2=ttk.Radiobutton(Left_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        rb2.grid(row=8,column=1,padx=50,pady=10,sticky=W)
        
        #save button
        save_btn=Button(Left_frame,command=self.add_data,text="Save",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=15)
        save_btn.grid(row=11,column=0,padx=50,pady=10,sticky=W)
        #update button
        update_btn=Button(Left_frame,command=self.update_data,text="Update",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=15)
        update_btn.grid(row=11,column=1,padx=50,pady=10,sticky=W)
        #delete button
        delete_btn=Button(Left_frame,command=self.delete_data,text="Delete",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=15)
        delete_btn.grid(row=12,column=0,padx=50,pady=10,sticky=W)
        #reset button
        reset_btn=Button(Left_frame,command=self.reset_data,text="Reset",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=15)
        reset_btn.grid(row=12,column=1,padx=50,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(Left_frame,command=self.take_photo,text="Take Photos",font=("sans-serif",13,"bold"),fg="white",bg="#2155CD",width=15)
        take_photo_btn.grid(row=10,column=0,padx=50,pady=10,sticky=W)
        
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("sans-serif",18,"bold"),fg="red")
        Right_frame.place(x=600,y=10,width=900,height=580)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("sans-serif",16,"bold"),fg="red")
        search_frame.place(x=5,y=10,width=860,height=100)
        
        search_label=Label(search_frame,text="Search By:",font=("sans-serif",15,"bold"),fg="#2155CD",bg="white")
        search_label.grid(row=0,column=0,padx=20,pady=15,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search_combo,font=("sans-serif",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Student_id","Name","Dep")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=20,pady=15,sticky=W)
        
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("sans-serif",13,"bold"))
        search_entry.grid(row=0,column=2,padx=20,pady=15,sticky=W)
        
        search_btn=Button(search_frame,command=self.search_data,text="Search",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=12)
        search_btn.grid(row=0,column=3,padx=20,pady=15)
        
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",font=("sans-serif",13,"bold"),fg="#E8F9FD",bg="#0AA1DD",width=12)
        showAll_btn.grid(row=0,column=4,padx=20,pady=15)
        
        #table frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=135,width=870,height=400)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("department","year","id","name","gender","dob","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("department",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        self.student_table.column("department",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #back button    
    def back_data(self):
        self.root.destroy()
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_std.get()=="" or self.var_std_id.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_dep.get(),                                                
                                                self.var_year.get(),                                
                                                self.var_std_id.get(),
                                                self.var_std.get(),                                               
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_radio.get()
                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
            
    #fetch data from database
    def fetch_data(self):
        conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_std_id.set(data[2]),
        self.var_std.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_email.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_radio.set(data[8])
        
        
    #update button
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_std.get()=="" or self.var_std_id.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)  
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Year=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",(
                                                self.var_dep.get(),                                              
                                                self.var_year.get(),                                      
                                                self.var_std.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_radio.get(),
                                                self.var_std_id.get()
                                            ))
                else:
                    if not Update:
                        return   
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()  
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
    #delete button
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student details","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)                    
        
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
    
    #search data
    def search_data(self):
        if self.var_search_combo.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_search_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
    
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
    
    
    #reset button
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_std_id.set(""),
        self.var_std.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio.set("")
        
    
    #Take photo sample
    def take_photo(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_std.get()=="" or self.var_std_id.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        if(self.var_radio.get()=="No"):
            messagebox.showerror("Error","No photo sample is selected",parent=self.root)    
        if(self.var_radio.get()=="Yes"):
            try:
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Year=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",(
                                                self.var_dep.get(),                                         
                                                self.var_year.get(),
                                                self.var_std.get(),                                              
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),                                               
                                                self.var_radio.get(),
                                                self.var_std_id.get()
                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                
                
                #Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(self.var_std_id.get())+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
          
              
if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()