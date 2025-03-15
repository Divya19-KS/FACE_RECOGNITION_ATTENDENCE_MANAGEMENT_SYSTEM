from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
import tkinter
import os
from time import strftime
from datetime import datetime
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face_recognition\images\login.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\lo.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #icon images
        img2=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\use.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\pass.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #login btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget password btn
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="Amber" and self.txtpass.get()=="hadii":
            messagebox.showinfo("Success","Welcome to Face Recognition System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Hadiya0405@amber",database="amber")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                    ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password window
    def reset_pass(self):
        if self.combo_secu.get()=="Select":
            messagebox.showerror("Error","Invalid username and password",parent=self.root2)
        elif self.txt_sec.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Hadiya0405@amber",database="amber")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and secu=%s and sec=%s")
            value=(self.txtuser.get(),self.combo_secu.get(),self.txt_sec.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showerror("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()



    #forgot password window
    def forgot_password_window(self):
        if self.txtuser.get=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Hadiya0405@amber",database="amber")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My error","please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                secu=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                secu.place(x=50,y=80)

                self.combo_secu=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_secu["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
                self.combo_secu.place(x=50,y=110,width=250)
                self.combo_secu.current(0)

                sec=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec.place(x=50,y=150)

                self.txt_sec=Entry(self.root2,font=("times new roman",15))
                self.txt_sec.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text=" New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secu=StringVar()
        self.var_sec=StringVar()
        self.var_password=StringVar()
        self.var_conf=StringVar()


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face_recognition\images\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face_recognition\images\nat.jpg")
        left_bg1=Label(self.root,image=self.bg1)
        left_bg1.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        secu=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        secu.place(x=50,y=240)

        self.combo_secu=ttk.Combobox(frame,textvariable=self.var_secu,font=("times new roman",15,"bold"),state="readonly")
        self.combo_secu["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_secu.place(x=50,y=270,width=250)
        self.combo_secu.current(0)

        sec=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec.place(x=370,y=240)

        self.txt_sec=Entry(frame,textvariable=self.var_sec,font=("times new roman",15))
        self.txt_sec.place(x=370,y=270,width=250)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=310)

        self.txt_password=Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        conf=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        conf.place(x=370,y=310)

        self.txt_conf=Entry(frame,textvariable=self.var_conf,font=("times new roman",15))
        self.txt_conf.place(x=370,y=340,width=250)

       

        
        


        #check btn
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        img=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\reg.webp")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\HP\Desktop\face_recognition\images\gg.jpeg")
        img1=img1.resize((200,45),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15))
        b1.place(x=330,y=420,width=200)


        #function declaration
    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secu.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_password.get()!=self.var_conf.get():
                messagebox.showerror("Error","password & confirm password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Hadiya0405@amber",database="amber")
                my_cursor=conn.cursor()
                Query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(Query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_fname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_secu.get(),
                                                                                           self.var_sec.get(),
                                                                                           self.var_password.get()
                                                 
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")
    def return_login(self):
        self.root.destroy()




        




if __name__=="__main__":
    main()