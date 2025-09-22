from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk, ImageEnhance
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition")
        face_instance = Face_Recognition(self.root)
        train_instance = Train(self.root)
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
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Segoe UI Semibold", 36, "bold"), bg="Black", fg="White")
        title_lbl.place(x=0, y=-1, width=1530, height=45)

        # Student Button 
        bt1_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\graduate.png")
        bt1_img = bt1_img.resize((220, 220))
        self.photoimg1 = ImageTk.PhotoImage(bt1_img)

        b1 = Button(bg_img, image=self.photoimg1, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        # Detect Face Button 
        bt2_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\face-scan.png")
        bt2_img = bt2_img.resize((220, 220))
        self.photoimg2 = ImageTk.PhotoImage(bt2_img)

        b1 = Button(bg_img, image=self.photoimg2, cursor="hand2",command=face_instance.face_recog)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=face_instance.face_recog, font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        # Attendance Button
        bt3_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\attendance.png")
        bt3_img = bt3_img.resize((220, 220))
        self.photoimg3 = ImageTk.PhotoImage(bt3_img)

        b1 = Button(bg_img, image=self.photoimg3, command=self.attendance_data, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance",  command=self.attendance_data,cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        
        # Help Button
        #bt3_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\attendance.png")
        #bt3_img = bt3_img.resize((220, 220))
        #self.photoimg3 = ImageTk.PhotoImage(bt3_img)

        #b1 = Button(bg_img, image=self.photoimg3, cursor="hand2")
        #b1.place(x=800, y=100, width=220, height=220)

        #b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        #b1_1.place(x=800, y=300, width=220, height=40)
        
        # Help Desk Button
        bt4_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\help_desk.png")
        bt4_img = bt4_img.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(bt4_img)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help", cursor="hand2", command=self.help_data, font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        
        # Train Button
        bt5_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\train.png")
        bt5_img = bt5_img.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(bt5_img)

        b1 = Button(bg_img, command=train_instance.train_classifier ,image=self.photoimg5, cursor="hand2")
        b1.place(x=200, y=500, width=220, height=220)

        b1_1 = Button(bg_img, text="Train", command=train_instance.train_classifier , cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=200, y=710, width=220, height=40)
        
        # Photos Button
        bt6_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\photos.png")
        bt6_img = bt6_img.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(bt6_img)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command = self.open_img)
        b1.place(x=500, y=500, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos",command = self.open_img,cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=500, y=710, width=220, height=40)
        
        # Project Information Button
        bt7_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\project.png")
        bt7_img = bt7_img.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(bt7_img)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command= self.developer_data)
        b1.place(x=800, y=500, width=220, height=220)

        b1_1 = Button(bg_img, text="Project Info", cursor="hand2",command= self.developer_data, font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=800, y=710, width=220, height=40)
        
        # Exit Button
        bt8_img = Image.open(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\exit.png")
        bt8_img = bt8_img.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(bt8_img)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.iExit)
        b1.place(x=1100, y=500, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("Segoe UI Semibold", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=1100, y=710, width=220, height=40)

    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno ("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


#======================= Function Buttons ==============================
         
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()