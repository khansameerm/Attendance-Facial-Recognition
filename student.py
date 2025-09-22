from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from train import Train



class Student:


    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition") 
        train_instance = Train(self.root)

        #==================== Variables =========================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_instructor=StringVar()
        
        # Set a black background
        self.root.configure(bg='black')

        # Bg Image 
        img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\about-the-university.png")
        img = img.resize((1550, 800))

        # Reduce the opacity of the image
        alpha = 0.5  # Set the desired opacity (0.0 to 1.0)
        img = img.convert("RGBA")
        alpha_channel = img.split()[3]
        alpha_channel = alpha_channel.point(lambda p: p * alpha)
        img.putalpha(alpha_channel)

        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg, bg='black')
        bg_img.place(x=0, y=0, width=1550, height=800)

        # Title 
        title_lbl = Label(bg_img, text="Student Details", font=("Segoe UI Semibold", 36, "bold"), bg="Black", fg="white")
        title_lbl.place(x=0, y=-1, width=1530, height=45)
        
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=70, y=130, width=1400, height= 600)
        
        # left label Frame 
        left_frame = LabelFrame(main_frame, bd=0, bg="white", relief=RIDGE, text="\t\tStudent Details", font=("Segoe UI Semibold", 22, "bold"))
        left_frame.place(x=10, y=10, width=690, height=580)
        
        # Current Course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("Segoe UI Semibold", 12, "bold"))
        current_course_frame.place(x=2, y=10, width=680, height=130)
        
        # department Label   
        dep_label = Label(current_course_frame,text="Department", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0 ,padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame,  textvariable=self.var_dep ,font=("Segoe UI Semibold", 12, "bold"), width=20, state="readonly")
        dep_combo["values"] = ("Select Department","Software","Computer Science","Biomedical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Course Label   
        course_label = Label(current_course_frame,text="Course", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2 ,padx=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("Segoe UI Semibold", 12, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course","P_Fund","OOPS","DSA","OS","AI")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        # Year Label   
        year_label = Label(current_course_frame, text="Batch", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0 ,padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Segoe UI Semibold", 12, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Batch","2022F","2023F","2024F")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        # Semester Label   
        semester_label = Label(current_course_frame,text="Semester", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2 ,padx=10, sticky=W)
        
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester ,font=("Segoe UI Semibold", 12, "bold"), width=20, state="readonly")
        semester_combo["values"] = ("Select Semester","1st","2nd","3rd","4th","5th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        # Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("Segoe UI Semibold", 12, "bold"))
        class_student_frame.place(x=2, y=160, width=680, height=250)
        
        # Studnet Id Label   
        student_id_label = Label(class_student_frame, text="Student ID:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0 ,padx=10, pady= 5, sticky=W)
        
        student_id_entry = Entry(class_student_frame, textvariable=self.va_std_id, width=18, font=("Segoe UI Semibold", 12, "bold"), highlightthickness=1, highlightbackground="gray", highlightcolor="gray")
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W) 
        
        # Studnet Name Label   
        student_name_label = Label(class_student_frame,text="Student Name:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2 ,padx=10, pady=5, sticky=W)
        
        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=18, font=("Segoe UI Semibold", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W) 
        
        # Section Label   
        cgpa_label = Label(class_student_frame,text="Section:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        cgpa_label.grid(row=1, column=0 ,padx=10, pady=5, sticky=W)
        
        #cgpa_entry = ttk.Entry(class_student_frame, textvariable=self.var_section, width=18, font=("Segoe UI Semibold", 12, "bold"))
        #cgpa_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W) 

        cgpa_combo = ttk.Combobox(class_student_frame, textvariable=self.var_section, font=("Segoe UI Semibold", 12, "bold"), width=16, state="readonly")
        cgpa_combo["values"] = ("Select Section","A","B","C","D","E","F")
        cgpa_combo.current(0)
        cgpa_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # Roll No Label   
        roll_no_label = Label(class_student_frame,text="Roll No:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2 ,padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=18, font=("Segoe UI Semibold", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W) 
        
        # Gender Label   
        gender_label = Label(class_student_frame,text="Gender:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0 ,padx=10, pady= 5, sticky=W)
        

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("Segoe UI Semibold", 12, "bold"), width=16, state="readonly")
        gender_combo["values"] = ("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        
        # Date of birth Label   
        dob_label = Label(class_student_frame,text="Date of Birth:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2 ,padx=10, pady= 5, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=18, font=("Segoe UI Semibold", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W) 
        
        # Email Label   
        email_label = Label(class_student_frame,text="Email:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0 ,padx=10, pady= 5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=18, font=("Segoe UI Semibold", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W) 
        
        # Phone No Label   
        phone_label = Label(class_student_frame,text="Phone No:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2 ,padx=10, pady= 5, sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=18, font=("Segoe UI Semibold", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W) 
        
        # Address Label   
        Address_label = Label(class_student_frame,text="Address:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=0 ,padx=10, pady= 5, sticky=W)
        
        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address,width=18, font=("Segoe UI Semibold", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W) 
        
        # Instructor Label
        instructor_label = Label(class_student_frame,text="Instructor:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        instructor_label.grid(row=4, column=2 ,padx=10, pady= 5, sticky=W)
        
        instructor_entry = ttk.Entry(class_student_frame, textvariable=self.var_instructor, width=18, font=("Segoe UI Semibold", 12, "bold"))
        instructor_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W) 
        
        # Radio Buttons
        self.var_radio1=StringVar()  
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1 ,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)
        
        self.var_radio2=StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio2 ,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)
        
        # Button Frame (first row)
        btn_frame = Frame(left_frame, bd=0, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=410, width=680, height=60)  # Adjust height for more space around buttons

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        save_btn.grid(row=0, column=0, padx=15, pady=10)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        update_btn.grid(row=0, column=1, padx=15, pady=10)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        delete_btn.grid(row=0, column=2, padx=15, pady=10)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        reset_btn.grid(row=0, column=3, padx=15, pady=10)

        train_photo_btn = Button(btn_frame, text="Train", command=train_instance.train_classifier, width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        train_photo_btn.grid(row=0, column=4, padx=15, pady=10)  # Placing it in the 5th column (right next to Reset button)

        # Second Button Frame (second row)
        btn_frame2 = Frame(left_frame, bd=0, relief=RIDGE, bg="white")
        btn_frame2.place(x=0, y=450, width=680, height=60)  # Reduced y value for more vertical closeness

        take_photo_btn = Button(btn_frame2, text="Take Photo Sample", command=self.generate_dataset, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=15, pady=10)

        update_photo_btn = Button(btn_frame2, text="Update Photo Sample", font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=15, pady=10)
        
        
        # Right label Frame 
        right_frame = LabelFrame(main_frame, bd=0, bg="white", relief=RIDGE, text="\t\tStudent Details", font=("Segoe UI Semibold", 22, "bold"))
        right_frame.place(x=710, y=10, width=680, height=580)

        # Search System 
        search_student_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Segoe UI Semibold", 12, "bold"))
        search_student_frame.place(x=2, y=9, width=670, height=70)
        
        search_label = Label(search_student_frame,text="Search By:", font=("Segoe UI Semibold", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0 ,padx=10, sticky=W)
        
        search_combo = ttk.Combobox(search_student_frame, font=("Segoe UI Semibold", 12, "bold"), width=10, state="readonly")
        search_combo["values"] = ("Select","Roll No","Phone No","Biomedical")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        student_id_entry = ttk.Entry(search_student_frame, width=15, font=("Segoe UI Semibold", 12, "bold"))
        student_id_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W) 
        
        search_btn = Button(search_student_frame, text="Search", width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        search_btn.grid(row=0, column=3, padx=15, pady=10)

        show_all_btn = Button(search_student_frame, text="Show All", width=12, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        show_all_btn.grid(row=0, column=4, padx=15, pady=10)

        
       # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=2, y=100, width=670, height=420)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "batch", "sem", "id", "name", "cgpa", "roll", "gender", "dob", "email", "phone", "address", "instructor", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("cgpa", text="CGPA")
        self.student_table.heading("roll", text="Roll")  
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("instructor", text="Instructor")
        self.student_table.heading("photo", text="PhotoSampleStatus")    
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100, anchor=CENTER)
        self.student_table.column("course", width=100, anchor=CENTER)
        self.student_table.column("batch", width=100, anchor=CENTER)
        self.student_table.column("sem", width=100, anchor=CENTER)
        self.student_table.column("id", width=100, anchor=CENTER)
        self.student_table.column("name", width=100, anchor=CENTER)
        self.student_table.column("roll", width=100, anchor=CENTER)
        self.student_table.column("gender", width=100, anchor=CENTER)
        self.student_table.column("cgpa", width=100, anchor=CENTER)
        self.student_table.column("dob", width=100, anchor=CENTER)
        self.student_table.column("email", width=200, anchor=CENTER)
        self.student_table.column("phone", width=100, anchor=CENTER)
        self.student_table.column("address", width=100, anchor=CENTER)
        self.student_table.column("instructor", width=100, anchor=CENTER)
        self.student_table.column("photo", width=150, anchor=CENTER)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #============================ Function Declaration ==============================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password= "arsalali@12_", database = "face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_instructor.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #===================================== fetch data ===============================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password= "arsalali@12_", database = "face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close

#========================== get cursor =================

    def get_cursor(self,event= ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_instructor.set(data[13]),
        self.var_radio1.set(data[14])
    
    #update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required", parent=self.root)

        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password= "arsalali@12_", database = "face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Section = %s, Roll = %s, Gender=%s, Dob = %s, Email=%s, Phone=%s, Address=%s, Instructor=%s , PhotoSample=%s where Student_id=%s",(     
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_instructor.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()
                                                                                                                ))
                else:
                    if not update:
                        return  
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)

    # delete function

    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student","Do you want to delete student details",parent= self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password= "arsalali@12_", database = "face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)   
    
    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_instructor.set("")
        self.var_radio1.set("")



    #======================= Generate data set or Take photo samples =========================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password= "arsalali@12_", database = "face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Section = %s, Roll = %s, Gender=%s, Dob = %s, Email=%s, Phone=%s, Address=%s, Instructor=%s , PhotoSample=%s where Student_id=%s",(     
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_instructor.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get() == id+1
                                                                                                                ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

                #=============================== load predefined data on frontal face from opencv ========================
                
                face_classifier = cv2.CascadeClassifier(r"C:\Users\Hp\Desktop\Face Recognitation System\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum neighbor = 5

                    for (x,y,w,h) in faces: 
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0    # 0 - 100 samples
                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face, str(img_id), (50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Data set generation completed!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)   



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
        