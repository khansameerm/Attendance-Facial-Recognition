from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System with Face Recognition") 

        # Title 
        title_lbl = Label(self.root, text="Train Data Set", font=("Segoe UI Semibold", 36, "bold"), bg="Black", fg="white")
        title_lbl.place(x=0, y=-1, width=1530, height=45)
         
    
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Gray Scale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train Classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Dataset training completed!")

        



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()