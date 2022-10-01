from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql
import numpy



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()







class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Real\Downloads\oop.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



        #==========================Frame Details===========================#

        frame= Frame(self.root,bg="white")
        frame.place(x=485,y=150,width=340,height=450)

        lbl_login=Label(frame,text="Login",font=("times new roman",30,"bold"),fg="Black",bg="White")
        lbl_login.place(x=115,y=10)

        lbl_user=Label(frame,text="Username : ",font=("times new roman",15,"bold"),fg="Black",bg="White")
        lbl_user.place(x=20, y=80)
        self.txt_user = Entry(frame,font=("times new roman",15,"bold"),bd=5, relief=GROOVE)
        self.txt_user.place(x=25,y=120,width=270)


        lbl_pass=Label(frame,text="Password : ",font=("times new roman",15,"bold"),fg="Black",bg="White")
        lbl_pass.place(x=20, y=170)
        self.txt_pass = Entry(frame,show="*",font=("times new roman",15,"bold"),bd=5, relief=GROOVE)
        self.txt_pass.place(x=25,y=210,width=270)


        #==================Button================#


        login_btn = Button(frame, text="Login", command=self.login,font=("times new roman",15,"bold"),bd=3, relief=RIDGE,fg="black",bg="white")
        login_btn.place(x=30,y=300,width=120,height=35)

        reg_btn = Button(frame, text="Sign Up",command=self.register_window, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black",bg="white")
        reg_btn.place(x=170, y=300, width=120,height=35)

        forgot_btn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="black", bg="white")
        forgot_btn.place(x=80, y=370, width=160)



    def register_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Register(self.new_win)


    def login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
             messagebox.showerror("Error","All Field Required")
        elif self.txt_user.get()=="Real" and self.txt_pass.get()=="Mimmoy":
             messagebox.showinfo("Success","Login Successfully")
             self.new_win = Toplevel(self.root)
             self.app = dashboard(self.new_win)
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()
            cur.execute("select * from registers where email=%s and pass=%s",(self.txt_user.get(),
                                                                              self.txt_pass.get()
                                                                            ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                self.new_win=Toplevel(self.root)
                self.app=dashboard(self.new_win)
            con.commit()
            con.close()

#=========================================================================================================================================================

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")


        #===============Variables==============#

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()






        #===============BG Image===============#
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Real\Downloads\1155052.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #===============Left Image=============#
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Real\Downloads\leftoop.png")
        left_bg = Label(self.root,image=self.bg1)
        left_bg.place(x=50,y=100,width=470,height=550)





        #=================Main Frame==============#
        frame=Frame(self.root,bg="White",bd=4, relief=RIDGE)
        frame.place(x=520,y=100,width=800,height=550)

        lbl_reg = Label(frame,text="Register Here",font=("times of roman",20,"bold"),bg="white",fg="black")
        lbl_reg.place(x=20,y=20)

        lbl_name1 = Label(frame, text="First Name : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_name1.place(x=20, y=100)
        self.txt_name1 =Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_name1.place(x=25, y=135, width=270)

        lbl_name2 = Label(frame, text="Last Name : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_name2.place(x=370, y=100)
        self.txt_name2 = Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_name2.place(x=370, y=135, width=270)

        lbl_contact = Label(frame, text="Contact : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_contact.place(x=20, y=170)
        self.txt_contact = Entry(frame,textvariable=self.var_contact ,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_contact.place(x=25, y=200, width=270)

        lbl_email = Label(frame, text="Email : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_email.place(x=370, y=170)
        self.txt_email = Entry(frame, textvariable=self.var_email,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_email.place(x=370, y=200, width=270)


        lbl_security_Q = Label(frame, text="Select Security Question : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_security_Q.place(x=20, y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite song")
        self.combo_security_Q.place(x=25,y=270,width=270)
        self.combo_security_Q.current(0)

        lbl_security_A = Label(frame, text="Security Answer : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_security_A.place(x=370, y=240)
        self.txt_security_A =Entry(frame,textvariable=self.var_securityA ,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_security_A.place(x=370, y=270, width=270)

        lbl_pass = Label(frame, text="Password : ", font=("times new roman", 15, "bold"), fg="Black",bg="White")
        lbl_pass.place(x=20, y=310)
        self.txt_pass = Entry(frame, textvariable=self.var_pass,show="*",font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_pass.place(x=25, y=340, width=270)

        lbl_pass_c = Label(frame, text="Confirm Password : ", font=("times new roman", 15, "bold"), fg="Black", bg="White")
        lbl_pass_c.place(x=370, y=310)
        self.txt_pass_c = Entry(frame,textvariable=self.var_confpass, show="*",font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_pass_c.place(x=370, y=340, width=270)


        #=============== Check Button =================#

        check_btn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("times new roman", 12, "bold"), fg="Black", bg="White",onvalue=1,offvalue=0)
        check_btn.place(x=20 , y = 400)

        reg_btn = Button(frame, command=self.register_data,text="Register Now",font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black",bg="white").place(x=20,y=460,width=180,height=35)
        login_btn = Button(frame,command=self.return_login, text="Login Now",font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black",bg="white").place(x=220,y=460,width=180,height=35)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()
            query=("select * from registers where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row = cur.fetchone()
            if row !=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                cur.execute("insert into registers values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_fname.get(),
                                                                                   self.var_lname.get(),
                                                                                   self.var_contact.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_securityQ.get(),
                                                                                   self.var_securityA.get(),
                                                                                   self.var_pass.get(),

                                                                                 ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register Successfully")


    def return_login(self):
        self.root.destroy()



#============================================================================================================================================
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_No_var = StringVar()
        self.gender_No_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()




        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=20,y=100,width=450,height=585)

        m_title = Label(Manage_Frame,text="Manage Student",bg=green,fg=Blue,font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="ID :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_No_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_No_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
        combo_gender.current(0)

        lbl_Contact = Label(Manage_Frame, text="Contact :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="D. O. B. :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame, textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame,width=30,height=3, font=("times new roman", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")



        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=15, y=525, width=420)

        add_btn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state='readonly')
        combo_search['values'] = ("ID", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="ID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")


        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               self.gender_No_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_Address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_No_var.set(row[2])
        self.gender_No_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")
        self.gender_No_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)


    def update_data(self):

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where id=%s",(
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               self.gender_No_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_Address.get('1.0',END),
                                                                               self.Roll_No_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been Updated")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from students where ID=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
#====================================================================================================================================#
class Department:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_No_var = StringVar()
        self.gender_No_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()




        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=20,y=100,width=480,height=585)

        m_title = Label(Manage_Frame,text="Dept Name & Faculties",bg=green,fg=Blue,font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Dept Name :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Faculty Name :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_No_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")





        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=15, y=500, width=420)

        add_btn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=530, y=100, width=800, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=15, state='readonly')
        combo_search['values'] = ("deptname ","Facultyname")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("deptname","Facultyname","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("deptname",text="Department Name")
        self.Student_table.heading("Facultyname",text="Faculty Name")
        self.Student_table.heading("Email",text="Email")



        self.Student_table['show']='headings'
        self.Student_table.column("deptname",width=100)
        self.Student_table.column("Facultyname",width=100)
        self.Student_table.column("Email",width=100)


        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into department values (%s,%s,%s)",(self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from department")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_No_var.set(row[2])



    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")



    def update_data(self):

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("update department set Facultyname=%s,Email=%s where deptname=%s",(
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               self.Roll_No_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been Updated")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from department where deptname=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from department where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
#=====================================================================================================================================#
class Advisor:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_No_var = StringVar()
        self.gender_No_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()




        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=20,y=100,width=490,height=585)

        m_title = Label(Manage_Frame,text="Advisors Information",bg=green,fg=Blue,font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Advisor Name :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_roll = Label(Manage_Frame,text="Advisor ID :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=2, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=2, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Phone Number :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_No_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=20, sticky="w")





        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=15, y=500, width=420)

        add_btn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=530, y=100, width=800, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=15, state='readonly')
        combo_search['values'] = ("ID","Name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("ID","Name","Phone","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("ID",text="ID")
        self.Student_table.heading("Name",text="Advisor Name")
        self.Student_table.heading("Phone",text="Phone Number")
        self.Student_table.heading("Email",text="Email")




        self.Student_table['show']='headings'
        self.Student_table.column("ID",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Phone",width=100)
        self.Student_table.column("Email",width=100)


        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into advisor values (%s,%s,%s,%s)",(
                                                                    self.contact_var.get(),
                                                                    self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from advisor")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.contact_var.set(row[0])
        self.Roll_No_var.set(row[1])
        self.name_var.set(row[2])
        self.email_No_var.set(row[3])



    def clear(self):
        self.contact_var.set("")
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")



    def update_data(self):

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("update advisor set Name=%s,Phone=%s,Email=%s where ID=%s",(
                                                                               self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               self.contact_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been Updated")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from advisor where ID=%s",self.contact_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from advisor where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
#=====================================================================================================================================#

class Waiver:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_No_var = StringVar()
        self.gender_No_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()





        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=20,y=100,width=450,height=585)

        m_title = Label(Manage_Frame,text="Waiver Calculator",bg=green,fg=Blue,font=("times new roman",35,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="ID :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Semester :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_No_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")


        lbl_Contact = Label(Manage_Frame, text="Percentage :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")




        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=15, y=525, width=420)


        add_btn = Button(btn_Frame,text="Calculate",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=480, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state='readonly')
        combo_search['values'] = ("ID", "Name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=850, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("ID","Semester","Percentage","Total Tuition Fees","After Waiver Fees","Registration Fees","Without Registration Fees","Mid Fees","Final Fees"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("ID",text="ID")
        self.Student_table.heading("Semester",text="Semester")
        self.Student_table.heading("Percentage",text="Percentage")
        self.Student_table.heading("Total Tuition Fees",text="Total Tuition Fees")
        self.Student_table.heading("After Waiver Fees",text="After Waiver Fees")
        self.Student_table.heading("Registration Fees", text="Registration Fees")
        self.Student_table.heading("Without Registration Fees",text="Without Registration Fees")
        self.Student_table.heading("Mid Fees",text="Mid Fees")
        self.Student_table.heading("Final Fees",text="Final Fees")


        self.Student_table['show']='headings'
        self.Student_table.column("ID",width=70)
        self.Student_table.column("Semester",width=50)
        self.Student_table.column("Percentage",width=50)
        self.Student_table.column("Total Tuition Fees",width=90)
        self.Student_table.column("After Waiver Fees",width=90)
        self.Student_table.column("Registration Fees",width=90)
        self.Student_table.column("Without Registration Fees",width=120)
        self.Student_table.column("Mid Fees",width=50)
        self.Student_table.column("Final Fees", width=50)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)






    def add_students(self):
        self.total = DoubleVar()
        self.w = DoubleVar()
        self.nt = DoubleVar()
        self.tsc = DoubleVar()
        self.sp = DoubleVar()
        self.s = IntVar()
        self.waiver = IntVar()
        self.reg = IntVar()
        self.ww = DoubleVar()


        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:

            s = int(self.email_No_var.get())
            waiver = int(self.contact_var.get())
            if s == 1:
                gc = 12
                cc = 3
                lc = 1
            elif s == 2:
                gc = 9
                cc = 2
                lc = 3
            elif s == 3:
                gc = 3
                cc = 6
                lc = 5
            elif s == 4:
                gc = 5
                cc = 3
                lc = 5
            elif s == 5:
                gc = 3
                cc = 6
                lc = 5
            elif s == 6:
                gc = 0
                cc = 7
                lc = 5
            elif s == 7:
                gc = 0
                cc = 4
                lc = 7
            elif s == 8:
                gc = 2
                cc = 6
                lc = 5
            elif s == 9:
                gc = 0
                cc = 6
                lc = 5
            elif s == 10:
                gc = 0
                cc = 5
                lc = 4
            elif s == 11:
                gc = 3
                cc = 7
                lc = 2
            elif s == 12:
                gc = 3
                cc = 6
                lc = 0
            else:
                messagebox.showerror("Error", "Enter Semester Between 1-12")

            self.total = (gc * 3200) + (cc * 4900) + (lc * 5000)
            self.t = str(self.total)

            self.w = (self.total * waiver) / 100
            self.a = str(self.w)

            self.nt = self.total - self.w
            self.n = str(self.nt)

            self.tsc = self.nt + 13500
            self.ts = str(self.tsc)

            self.sp = self.nt / 2
            self.s = str(self.sp)

            self.reg = 13500
            self.r = str(self.reg)

            self.ww = self.sp * 2
            self.www = str(self.ww)

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into waiver values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),

                                                                               self.email_No_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.t,
                                                                               self.ts,
                                                                               self.r,
                                                                               self.www,
                                                                               self.s,
                                                                               self.s,
                                                                               self.name_var.get()




                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from waiver limit 9")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_No_var.set(row[2])
        self.contact_var.set(row[3])


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")
        self.contact_var.set("")



    def update_data(self):

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("update waiver set Semester=%s,Percentage=%s, Name =%s where ID=%s",(
                                                                               self.email_No_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.name_var.get(),

                                                                               self.Roll_No_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been Updated")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from waiver where ID=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from waiver where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
#=====================================================================================================================================#

class CGPA:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.total_credit = StringVar()
        self.credit_Hours = StringVar()
        self.Grade_Point = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()





        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=15,y=100,width=500,height=585)

        m_title = Label(Manage_Frame,text="CGPA Calculator",bg=green,fg=Blue,font=("times new roman",35,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="ID :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Credit Taken :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.total_credit,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")


        lbl_Contact = Label(Manage_Frame, text="Credit Hours :", bg=green, fg="white",font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.credit_Hours, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Grade Point :", bg=green, fg="white",font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.Grade_Point, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")






        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=80, y=500, width=310)


        add_btn = Button(btn_Frame,text="Calculate",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=1, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=2, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=530, y=100, width=810, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state='readonly')
        combo_search['values'] = ("ID", "Name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=20, y=70, width=760, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("ID","Name","CGPA"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("ID",text="ID")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("CGPA",text="CGPA")



        self.Student_table['show']='headings'
        self.Student_table.column("ID",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("CGPA",width=100)


        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)






    def add_students(self):
        self.total_credit_taken = IntVar()
        self.gi = DoubleVar()
        self.ci = DoubleVar()
        self.total = DoubleVar()
        self.gpa = DoubleVar()
        self.temp = DoubleVar()
        self.sum = DoubleVar()
        self.g = StringVar

        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:
            self.total_credit_taken = int(self.total_credit.get())
            self.ci = list(map(int,self.credit_Hours.get().split()))
            self.gi = list(map(float,self.Grade_Point.get().split()))

            self.temp = numpy.multiply(self.ci,self.gi)

            self.sum = 0

            for i in self.temp:
                self.sum +=i
            self.total = self.sum

            self.gpa = self.total/self.total_credit_taken
            self.gpa = "{:.2f}".format(self.gpa)
            self.g = str(self.gpa)



            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into cgpa values (%s,%s,%s)",(self.Roll_No_var.get(),
                                                                self.name_var.get(),
                                                                self.g,



                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from cgpa")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.total_credit.set("")
        self.credit_Hours.set("")
        self.Grade_Point.set("")



    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from cgpa where ID=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from cgpa where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()

#=====================================================================================================================================#

class Resturant:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#39a94b')
        title=Label(self.root,text="Green Garden",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)


        # ===============All Variables======================#

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_No_var = StringVar()
        self.gender_No_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()




        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=20,y=100,width=450,height=585)

        m_title = Label(Manage_Frame,text="Menu Details",bg=green,fg=Blue,font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Name :",bg=green,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Price :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Time :", bg=green, fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_No_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("Select","Breakfast","Lunch","Dinner")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
        combo_gender.current(0)



        #============================Button Frame===================#

        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg=Ash)
        btn_Frame.place(x=15, y=525, width=420)

        add_btn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)




        # ===============Details Frame======================#

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=green)
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg=green, fg=Blue,font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")
        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state='readonly')
        combo_search['values'] = ("Name", "Time")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        search_btn = Button(Details_Frame, text="Search", width=10,pady=5,command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Details_Frame, text="Show All", width=10, pady=5 ,command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)



        # ===============Table Frame======================#

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("Name","Price","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Price",text="Price")
        self.Student_table.heading("Time",text="Time")


        self.Student_table['show']='headings'
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Price",width=100)
        self.Student_table.column("Time",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required to fill")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into greengarden values (%s,%s,%s)",(self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.gender_No_var.get(),
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from greengarden")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_No_var.set(row[2])



    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")


    def update_data(self):

            con = pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("update greengarden set Name=%s,Price=%s,Time=%s",(
                                                                               self.Roll_No_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_No_var.get(),
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Recored has been Updated")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from greengarden where Name=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        if  self.search_txt.get()=="":
            messagebox.showerror("Error","Please enter the information")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()

            cur.execute("select * from greengarden where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()

#======================================================================================================================================#

class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")



        Blue=('#204496')
        Ash=('#868e92')
        green=('#89e1fa')
        title=Label(self.root,text="Student Management",bd=9,relief=GROOVE,font=("times new roman",40,"bold"),bg=Ash,fg=Blue)
        title.pack(side=TOP,fill = X)



        #===============ManageFrame======================#


        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=green)
        Manage_Frame.place(x=550, y=100, width=790, height=585)


        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Real\Downloads\leftoop.png")
        left_bg = Label(self.root, image=self.bg1)
        left_bg.place(x=50, y=100, width=470, height=550)

        m_title = Label(Manage_Frame,text="Admin Dashboard",bg=green,fg=Blue,font=("times new roman",40,"bold"))
        m_title.place(x=200,y=20)

        add_btn = Button(Manage_Frame, text="Student Information", command=self.Student_Information_window,width=30, height=2).place(x=160,y=200)
        update_btn = Button(Manage_Frame, text="Department Information", command=self.Department_Information_window,width=30,height=2).place(x=450,y=200)
        delete_btn = Button(Manage_Frame, text="Advisors Information", command=self.Advisor_Information_window,width=30, height=2).place(x=160,y=300)
        clear_btn = Button(Manage_Frame, text="CGPA Calculator", command=self.CGPA_Information_window,width=30,height=2).place(x=450,y=300)
        cl1_btn = Button(Manage_Frame, text="Waiver Calculator", command=self.Waiver_Information_window,width=30,height=2).place(x=160,y=390)
        cl2_btn = Button(Manage_Frame, text="Green Garden Details", command=self.Green_Information_window,width=30, height=2).place(x=450,y=390)

    def Student_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Student(self.new_win)

    def Department_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Department(self.new_win)

    def Advisor_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Advisor(self.new_win)

    def Waiver_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Waiver(self.new_win)
    def CGPA_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=CGPA(self.new_win)
    def Green_Information_window(self):
        self.new_win=Toplevel(self.root)
        self.app=Resturant(self.new_win)





if __name__ == '__main__':
    main()