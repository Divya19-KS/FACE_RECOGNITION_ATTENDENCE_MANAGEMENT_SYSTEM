from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\developer.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

       
        
        #developer info
        dev_label=Label(main_frame,text="Hello Welcome! We the Developers",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        dev_label=Label(main_frame,text="1)Chethan P M     2)Divya Shree K S",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)
        dev_label=Label(main_frame,text="3)Hadiya Amber   4)Harish Kumar",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=75)

        dev_label=Label(main_frame,text="We are from CSE",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=110)

        img2=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\WhatsApp Image 2024-07-18 at 10.38.11 AM.jpeg")
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)























if __name__ =="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()