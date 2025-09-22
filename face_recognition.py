from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition")
        
        title_lbl = Label(self.root, text="Face Recognition", font=("Segoe UI Semibold", 36, "bold"), bg="Black", fg="white")
        title_lbl.place(x=0, y=-1, width=1530, height=45)


    # attendance 

    def mark_attendance(self,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")

                

    # face recognition

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="arsalali@12_", database="face_recognizer")
                my_cursor = conn.cursor()

                # Fetch Name
                my_cursor.execute("select Name from student where Student_id=%s", (id,))
                result = my_cursor.fetchone()
                n = result[0] if result else "Unknown"

                # Fetch Roll
                my_cursor.execute("select Roll from student where Student_id=%s", (id,))
                result = my_cursor.fetchone()
                r = result[0] if result else "Unknown"

                # Fetch Department
                my_cursor.execute("select Department from student where Student_id=%s", (id,))
                result = my_cursor.fetchone()
                d = result[0] if result else "Unknown"

                if confidence > 77:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, f"Roll Number: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:  # Check if the frame is captured successfully
                print("Failed to capture frame from webcam. Retrying...")
                continue  # Skip this iteration and try again

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()  # Release webcam resources
        cv2.destroyAllWindows()  # Close all OpenCV windows











if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()