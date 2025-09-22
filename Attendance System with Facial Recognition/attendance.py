from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition") 

        # variables

        self.var_roll_num = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()

        # Set a black background
        self.root.configure(bg='black')

        # Bg Image 
        img = Image.open(r"C:\Users\Hp\Desktop\Face Recognitation System\college_images\About-The-University1.jpg")
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
        title_lbl = Label(bg_img, text="Attendance Details", font=("Segoe UI Semibold", 36, "bold"), bg="Black", fg="white")
        title_lbl.place(x=0, y=-1, width=1530, height=45)
        
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=70, y=130, width=1400, height= 600)

        # left label Frame 
        left_frame = LabelFrame(main_frame, bd=0, bg="white", relief=RIDGE, text="\t\tStudent Information", font=("Segoe UI Semibold", 22, "bold"))
        left_frame.place(x=10, y=10, width=690, height=400)

        left_in_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_in_frame.place(x=20, y=100, width=665, height= 250)

        # Roll
        rollLabel = Label(left_in_frame, text="Roll:", bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=0, padx=10, pady=(25, 10))  

        atten_roll = ttk.Entry(left_in_frame, textvariable=self.var_roll_num, width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=1, padx=20, pady=(25, 5))  

        # Name
        nameLabel = Label(left_in_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=0, column=2, padx=10, pady=(25, 0))  

        atten_name = ttk.Entry(left_in_frame, textvariable=self.var_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=0, column=3, padx=20, pady=(25, 8)) 

        # Department
        depLabel = Label(left_in_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=0, padx=10) 

        atten_dep = ttk.Entry(left_in_frame, textvariable=self.var_department, width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=1, padx=20, pady=8)  # Increased padx for spacing

        # Time
        timeLabel = Label(left_in_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=2, padx=10) 

        atten_time = ttk.Entry(left_in_frame, textvariable=self.var_time, width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=3, padx=20, pady=8) 

        # Date
        dateLabel = Label(left_in_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=1, column=2, padx=10)  

        atten_date = ttk.Entry(left_in_frame, textvariable=self.var_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=1, column=3, padx=20, pady=8)  

        # Attendance
        attendanceLabel = Label(left_in_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=2, column=0, padx=10)  

        self.atten_status = ttk.Combobox(left_in_frame, textvariable=self.var_attendance_status, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=2, column=1, padx=20, pady=8)  
        self.atten_status.current(0)


        # Button Frame 
        btn_frame = Frame(left_in_frame, bd=0, relief=RIDGE, bg="white")
        btn_frame.place(x=20, y=180, width=620, height=40)  

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=10, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        import_btn.grid(row=0, column=0, padx=5, pady=5)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=10, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        export_btn.grid(row=0, column=1, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Update", width=10, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        update_btn.grid(row=0, column=2, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data ,width=10, font=("Segoe UI Semibold", 10, "bold"), bg="Green", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)


        # Right label Frame 
        right_frame = LabelFrame(main_frame, bd=0, bg="white", relief=RIDGE, text="\t\tAttendance Details", font=("Segoe UI Semibold", 22, "bold"))
        right_frame.place(x=710, y=10, width=680, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=20, y=10, width=640, height=500) 

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, column=("Roll Number", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("Roll Number", text="Roll Number")
        self.attendance_table.heading("Name", text="Name")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("Attendance", text="Attendance")

        self.attendance_table["show"] = "headings"

        self.attendance_table.column("Roll Number", width=100, anchor=CENTER)
        self.attendance_table.column("Name", width=100, anchor=CENTER)
        self.attendance_table.column("Department", width=100, anchor=CENTER)
        self.attendance_table.column("Time", width=100, anchor=CENTER)
        self.attendance_table.column("Date", width=100, anchor=CENTER)
        self.attendance_table.column("Attendance", width=100, anchor=CENTER)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # fetch data

    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Export Error", "No data available to export. Please make sure the table contains data before exporting.", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data has been exported successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        data = content["values"]

        self.var_roll_num.set(data[0]) 
        self.var_name.set(data[1])    
        self.var_department.set(data[2])  
        self.var_time.set(data[3])    
        self.var_date.set(data[4])    
        self.var_attendance_status.set(data[5]) 


    def reset_data(self):
        self.var_roll_num.set("") 
        self.var_name.set("")    
        self.var_department.set("")  
        self.var_time.set("")     
        self.var_date.set("")    
        self.var_attendance_status.set("Status")  

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()