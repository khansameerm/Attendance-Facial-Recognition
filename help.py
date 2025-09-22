from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class Help:
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

        # Help Page Heading
        heading_label = Label(
            main_frame, 
            text="Help Page", 
            font=("Arial", 16, "bold"), 
            bg="black", 
            fg="white"
        )
        heading_label.pack(fill=X, pady=0)

        # Scrollbar setup
        scroll_y = Scrollbar(main_frame, orient=VERTICAL)
        
        # Instructions
        instructions = Text(
            main_frame, 
            wrap=WORD, 
            font=("Arial", 12), 
            bg="white", 
            fg="black", 
            bd=0, 
            yscrollcommand=scroll_y.set
        )
        scroll_y.config(command=instructions.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        instructions.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Help Content
        instructions.insert(
            END, 
            "Follow the steps below to use the Attendance System with Face Recognition:\n\n"
            "1. Student Detail:\n"
            "   - Use this tab to enter new student details or update existing ones.\n"
            "   - Take photo samples of the student to build the dataset.\n\n"
            "2. Train:\n"
            "   - Train the AI algorithm using the photo samples collected in the previous step.\n"
            "   - This step prepares the system to recognize student faces accurately.\n\n"
            "3. Face Detector:\n"
            "   - Allow the student to stand in front of the camera.\n"
            "   - The system will detect their face and automatically mark their attendance.\n\n"
            "4. Photos:\n"
            "   - View the complete dataset of photos for all registered students.\n"
            "   - This helps verify if the photo samples were taken correctly.\n\n"
            "5. Attendance:\n"
            "   - Import or export attendance data in Excel format.\n"
            "   - This ensures smooth data handling and integration with other tools.\n\n"
            "6. Project Info:\n"
            "   - View a summary of the technologies and components used in this project.\n"
            "   - Gain insight into the system's underlying design and functionality.\n\n"
            "7. Exit:\n"
            "   - Use this option to safely shut down the program.\n\n"
            "For any further assistance, feel free to contact the development team."
        )
        instructions.config(state=DISABLED)  # Make the text box read-only

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
    obj = Help(root)
    root.mainloop()
