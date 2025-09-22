from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition")
        
        # Video player setup
        self.lblVideo = Label(self.root)
        self.lblVideo.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.cap = cv2.VideoCapture(r"C:\Users\hp\Desktop\Face Recognitation System\college_images\Sir Syed University.mp4")
        self.update_video()

        # Main frame setup
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=500, y=130, width=500, height=600)
        
        # Project Information Heading
        heading_label = Label(
            main_frame, 
            text="Project Information", 
            font=("Segoe UI Semibold", 16, "bold"), 
            bg="black", 
            fg="white"
        )
        heading_label.pack(fill=X, pady=0)

        # Project Description
        project_info = Text(main_frame, wrap=WORD, font=("Segoe UI Semibold", 12), bg="white", fg="black", bd=0)
        project_info.insert(
            END, 
            "This is a Face Recognition Attendance Management System built using OpenCV, "
            "Face Recognition library, and MySQL. The system automatically recognizes faces, "
            "records attendance, and stores data in a secure database.\n\n"
            "Key Features:\n"
            "- Real-time face detection and recognition.\n"
            "- Attendance tracking and storage.\n"
            "- MySQL database integration.\n"
            "- Simple and intuitive user interface."
        )
        project_info.config(state=DISABLED)  
        project_info.pack(padx=10, pady=10, fill=BOTH, expand=True)

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (1920, 1080))
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lblVideo.imgtk = imgtk
            self.lblVideo.configure(image=imgtk)
            # Reduce delay to speed up video playback
            self.lblVideo.after(5, self.update_video)
        else:
            # Reset the video to the beginning for infinite loop
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.update_video()

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
