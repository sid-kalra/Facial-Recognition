from ast import Return
import importlib
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import cvtColor, exp 
import pymysql
from numpy import delete
import cv2
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
import pymysql

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # self.wm_iconbitmap("icon.ico")
        
        #Variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_attendance=StringVar()
        self.var_percent=StringVar()
        self.var_search=StringVar()
        self.var_search_combo=StringVar()

        #image1
        img1 =Image.open(r"photos\attendance.jpg")
        img1=img1.resize((1530,350),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1530,height=350)
        
        #bg image
        img4 =Image.open(r"photos\History-of-Facial-Recognition-Technology.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=610)
        
        title_lbl=Label(bg_img,text="Attendance Management System",font=("sans-serif",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background="white",foreground="blue")
        lbl.place(x=110,y=(0),width=110,height=50)
        time()
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=53,width=1480,height=500)
        
        #back button
        b1_1=Button(self.root,command=self.back_data,text="Back",cursor="hand2", font=("sans-serif",12,"bold"),bg="#0AA1DD",fg="White")
        b1_1.place(x=5,y=10,width=100,height=30)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("sans-serif",18,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=600,height=480)
        
        export_btn=Button(Left_frame,text="Download Attendance",command=self.exportCsv,font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=20)
        export_btn.grid(row=6,column=0,pady=10,padx=50,sticky=W)
        
        #reset button
        reset_btn=Button(Left_frame,command=self.reset_data,text="Reset",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=17)
        reset_btn.grid(row=6,column=1,pady=10,padx=50,sticky=W)
        
        search_label=Label(Left_frame,text="Search By:",font=("sans-serif",15,"bold"),fg="#2155CD",bg="white")
        search_label.grid(row=7,column=0,padx=50,pady=10,sticky=W)
        
        search_combo=ttk.Combobox(Left_frame,textvariable=self.var_search_combo,font=("sans-serif",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Student_id","Name","Dep")
        search_combo.current(0)
        search_combo.grid(row=8,column=0,padx=50,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Left_frame,textvariable=self.var_search,width=15,font=("sans-serif",13,"bold"))
        search_entry.grid(row=8,column=1,padx=50,pady=10,sticky=W)
        
        search_btn=Button(Left_frame,command=self.search_data,text="Search",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=20)
        search_btn.grid(row=9,column=0,padx=50,pady=10,sticky=W)
        
        showAll_btn=Button(Left_frame,command=self.fetch_data,text="Show All",font=("sans-serif",13,"bold"),fg="white",bg="#0AA1DD",width=17)
        showAll_btn.grid(row=9,column=1,padx=50,pady=10,sticky=W)
        
        #Labels and entry
        
        #attendance id
        Student_id_label=Label(Left_frame,text="Student id",font=("sans-serif",13,"bold"),bg="white")
        Student_id_label.grid(row=0,column=0,pady=10,padx=50,sticky=W)
        
        Student_id_entry=ttk.Entry(Left_frame,textvariable=self.var_id,width=20,font=("sans-serif",13,"bold"))
        Student_id_entry.grid(row=0,column=1,pady=10,padx=50,sticky=W)
        
        #studentName
        studentName_label=Label(Left_frame,text="Student Name",font=("sans-serif",13,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,pady=10,padx=50,sticky=W)
        
        studentName_entry=ttk.Entry(Left_frame,textvariable=self.var_name,width=20,font=("sans-serif",13,"bold"))
        studentName_entry.grid(row=1,column=1,pady=10,padx=50,sticky=W)
        
        
        #Department
        dep_label=Label(Left_frame,text="Department",font=("sans-serif",13,"bold"),bg="white")
        dep_label.grid(row=2,column=0,pady=12,padx=50,sticky=W)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("sans-serif",13,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,pady=10,padx=50,sticky=W)
        
            
        #Attendance Status
        attend_label=Label(Left_frame,text="Today's Attendance",font=("sans-serif",13,"bold"),bg="white")
        attend_label.grid(row=3,column=0,pady=10,padx=50,sticky=W)
        self.attend=ttk.Combobox(Left_frame,textvariable=self.var_attendance,font=("sans-serif",13,"bold"),width=20,state="readonly")
        self.attend["values"]=("Status","Present","Absent")
        self.attend.grid(row=3,column=1,pady=10,padx=50,sticky=W)
        self.attend.current(0)
        
        #Attendance
        percent_label=Label(Left_frame,text="Attendance Percent",font=("sans-serif",13,"bold"),bg="white")
        percent_label.grid(row=4,column=0,pady=10,padx=50,sticky=W)
        
        percent_entry=ttk.Entry(Left_frame,textvariable=self.var_percent,width=20,font=("sans-serif",13,"bold"))
        percent_entry.grid(row=4,column=1,pady=10,padx=50,sticky=W)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("sans-serif",18,"bold"),fg="red")
        Right_frame.place(x=630,y=10,width=830,height=480)
        
        #Low attendance button
        export_btn=Button(Right_frame,text="Short Attendance",command=self.low,font=("sans-serif",14,"bold"),fg="white",bg="#0AA1DD",width=20)
        export_btn.grid(row=0,column=0,pady=10,padx=70,sticky=W)
        
        #Perfect attendance button
        export_btn=Button(Right_frame,text="Perfect Attendance",command=self.perfect,font=("sans-serif",14,"bold"),fg="white",bg="#0AA1DD",width=20)
        export_btn.grid(row=0,column=1,pady=10,padx=70,sticky=W)
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=55,width=810,height=380)
        
        
        #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","PERCENT","24_05_2022","25_05_2022","26_05_2022","27_05_2022",
                                                                    "28_05_2022","29_05_2022","30_05_2022","31_05_2022","01_06_2022","02_06_2022","03_06_2022","04_06_2022","05_06_2022","06_06_2022",
                                                                    "07_06_2022","08_06_2022","09_06_2022","10_06_2022","11_06_2022","12_06_2022","13_06_2022","14_06_2022","15_06_2022","16_06_2022",
                                                                    "17_06_2022","18_06_2022","19_06_2022","20_06_2022","21_06_2022","22_06_2022","23_06_2022","24_06_2022","25_06_2022","26_06_2022",
                                                                    "27_06_2022","28_06_2022","29_06_2022","30_06_2022","01_07_2022","02_07_2022","03_07_2022","04_07_2022","05_07_2022"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Student Id")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("PERCENT",text="Percent")
        self.AttendanceReportTable.heading("24_05_2022",text="24_05_2022")
        self.AttendanceReportTable.heading("25_05_2022",text="25_05_2022")
        self.AttendanceReportTable.heading("26_05_2022",text="26_05_2022")
        self.AttendanceReportTable.heading("27_05_2022",text="27_05_2022")
        self.AttendanceReportTable.heading("28_05_2022",text="28_05_2022")
        self.AttendanceReportTable.heading("29_05_2022",text="29_05_2022")
        self.AttendanceReportTable.heading("30_05_2022",text="30_05_2022")
        self.AttendanceReportTable.heading("31_05_2022",text="31_05_2022")
        self.AttendanceReportTable.heading("01_06_2022",text="01_06_2022")
        self.AttendanceReportTable.heading("02_06_2022",text="02_06_2022")
        self.AttendanceReportTable.heading("03_06_2022",text="03_06_2022")
        self.AttendanceReportTable.heading("04_06_2022",text="04_06_2022")
        self.AttendanceReportTable.heading("05_06_2022",text="05_06_2022")
        self.AttendanceReportTable.heading("06_06_2022",text="06_06_2022")
        self.AttendanceReportTable.heading("07_06_2022",text="07_06_2022")
        self.AttendanceReportTable.heading("08_06_2022",text="08_06_2022")
        self.AttendanceReportTable.heading("09_06_2022",text="09_06_2022")
        self.AttendanceReportTable.heading("10_06_2022",text="10_06_2022")
        self.AttendanceReportTable.heading("11_06_2022",text="11_06_2022")
        self.AttendanceReportTable.heading("12_06_2022",text="12_06_2022")
        self.AttendanceReportTable.heading("13_06_2022",text="13_06_2022")
        self.AttendanceReportTable.heading("14_06_2022",text="14_06_2022")
        self.AttendanceReportTable.heading("15_06_2022",text="15_06_2022")
        self.AttendanceReportTable.heading("16_06_2022",text="16_06_2022")
        self.AttendanceReportTable.heading("17_06_2022",text="17_06_2022")
        self.AttendanceReportTable.heading("18_06_2022",text="18_06_2022")
        self.AttendanceReportTable.heading("19_06_2022",text="19_06_2022")
        self.AttendanceReportTable.heading("20_06_2022",text="20_06_2022")
        self.AttendanceReportTable.heading("21_06_2022",text="21_06_2022")
        self.AttendanceReportTable.heading("22_06_2022",text="22_06_2022")
        self.AttendanceReportTable.heading("23_06_2022",text="23_06_2022")
        self.AttendanceReportTable.heading("24_06_2022",text="24_06_2022")
        self.AttendanceReportTable.heading("25_06_2022",text="25_06_2022")
        self.AttendanceReportTable.heading("26_06_2022",text="26_06_2022")
        self.AttendanceReportTable.heading("27_06_2022",text="27_06_2022")
        self.AttendanceReportTable.heading("28_06_2022",text="28_06_2022")
        self.AttendanceReportTable.heading("29_06_2022",text="29_06_2022")
        self.AttendanceReportTable.heading("30_06_2022",text="30_06_2022")
        self.AttendanceReportTable.heading("01_07_2022",text="01_07_2022")
        self.AttendanceReportTable.heading("02_07_2022",text="02_07_2022")
        self.AttendanceReportTable.heading("03_07_2022",text="03_07_2022")
        self.AttendanceReportTable.heading("04_07_2022",text="04_07_2022")
        self.AttendanceReportTable.heading("05_07_2022",text="05_07_2022")
        
        
        
        
        
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("PERCENT",width=100)
        self.AttendanceReportTable.column("24_05_2022",width=100)
        self.AttendanceReportTable.column("25_05_2022",width=100)
        self.AttendanceReportTable.column("26_05_2022",width=100)
        self.AttendanceReportTable.column("27_05_2022",width=100)
        self.AttendanceReportTable.column("28_05_2022",width=100)
        self.AttendanceReportTable.column("29_05_2022",width=100)
        self.AttendanceReportTable.column("30_05_2022",width=100)
        self.AttendanceReportTable.column("31_05_2022",width=100)
        self.AttendanceReportTable.column("01_06_2022",width=100)
        self.AttendanceReportTable.column("02_06_2022",width=100)
        self.AttendanceReportTable.column("03_06_2022",width=100)
        self.AttendanceReportTable.column("04_06_2022",width=100)
        self.AttendanceReportTable.column("05_06_2022",width=100)
        self.AttendanceReportTable.column("06_06_2022",width=100)
        self.AttendanceReportTable.column("07_06_2022",width=100)
        self.AttendanceReportTable.column("08_06_2022",width=100)
        self.AttendanceReportTable.column("09_06_2022",width=100)
        self.AttendanceReportTable.column("10_06_2022",width=100)
        self.AttendanceReportTable.column("11_06_2022",width=100)
        self.AttendanceReportTable.column("12_06_2022",width=100)
        self.AttendanceReportTable.column("13_06_2022",width=100)
        self.AttendanceReportTable.column("14_06_2022",width=100)
        self.AttendanceReportTable.column("15_06_2022",width=100)
        self.AttendanceReportTable.column("16_06_2022",width=100)
        self.AttendanceReportTable.column("17_06_2022",width=100)
        self.AttendanceReportTable.column("18_06_2022",width=100)
        self.AttendanceReportTable.column("19_06_2022",width=100)
        self.AttendanceReportTable.column("20_06_2022",width=100)
        self.AttendanceReportTable.column("21_06_2022",width=100)
        self.AttendanceReportTable.column("22_06_2022",width=100)
        self.AttendanceReportTable.column("23_06_2022",width=100)
        self.AttendanceReportTable.column("24_06_2022",width=100)
        self.AttendanceReportTable.column("25_06_2022",width=100)
        self.AttendanceReportTable.column("26_06_2022",width=100)
        self.AttendanceReportTable.column("27_06_2022",width=100)
        self.AttendanceReportTable.column("28_06_2022",width=100)
        self.AttendanceReportTable.column("29_06_2022",width=100)
        self.AttendanceReportTable.column("30_06_2022",width=100)
        self.AttendanceReportTable.column("01_07_2022",width=100)
        self.AttendanceReportTable.column("02_07_2022",width=100)
        self.AttendanceReportTable.column("03_07_2022",width=100)
        self.AttendanceReportTable.column("04_07_2022",width=100)
        self.AttendanceReportTable.column("05_07_2022",width=100)
         
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.cursor)
        self.fetch_data()
    
    #back button    
    def back_data(self):
        self.root.destroy()
    
    def low(self):
        conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendancetable where PERCENT<75.0")
        rows=my_cursor.fetchall()
        if len(rows)==0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            conn.commit()
        if len(rows)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()
    def perfect(self):
        conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendancetable where PERCENT=100.0")
        rows=my_cursor.fetchall()
        if len(rows)==0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            conn.commit()
        if len(rows)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #fetch data from database
    def fetch_data(self):
        conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendancetable")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()  
        
    #search data
    def search_data(self):
        if self.var_search_combo.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from attendancetable where "+str(self.var_search_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in rows:
                        self.AttendanceReportTable.insert("",END,values=i)
                    conn.commit()
                conn.close()
    
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
    
    #Export
    def exportCsv(self):
        try:
            fln=filedialog.asksaveasfilename(initialfile=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)    
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from attendancetable")
                myresult=my_cursor.fetchall()
                for i in myresult:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
                
        
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
    def cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        now=datetime.now()
        d1=now.strftime("%d_%m_%Y")
        d2=str(d1)
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_percent.set(rows[3])
        d3=self.var_id.get()
        conn=pymysql.connect(host="database1.chw7a9s6h44d.us-west-2.rds.amazonaws.com",user="admin",password="Mysql123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select {d2} from attendancetable where Student_id= {d3}",())
        my_result=my_cursor.fetchone()
        if (my_result[0]=="P"):
            self.var_attendance.set("Present")
        else:
            self.var_attendance.set("Absent")
        
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_attendance.set("")
        self.var_percent.set("0")
        
        
if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()