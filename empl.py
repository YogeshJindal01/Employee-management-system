from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_design=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=IntVar()
        self.var_doj=IntVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=IntVar()
        self.var_country=StringVar()
        self.var_salary=IntVar()
        
        lb_title = Label(self.root,text="Employee Management System",font=("times new roman",37,"bold"),fg='darkblue',bg='white')
        lb_title.place(x=0,y=0,width=1530,height=50)
        #logo haeding
        img_logo=Image.open('images/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=370,y=0,width=50,height=50)
        # 2nd frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=50,width=1530,height=170)
        #1st image
        img1=Image.open('images/new2.webp')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.im_1=Label(img_frame,image=self.photo1)
        self.im_1.place(x=0,y=0,width=540,height=160)
        #2nd image
        img2=Image.open('images/new3.webp')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.im_2=Label(img_frame,image=self.photo2)
        self.im_2.place(x=540,y=0,width=540,height=160)
        #3rd image
        img3=Image.open('images/new4.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.im_3=Label(img_frame,image=self.photo3)
        self.im_3.place(x=1080,y=0,width=540,height=160)

        #main frame

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=10,y=220,width=1500,height=560)

        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Information",font=("times new roman",24,"bold"),fg='darkRed',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=250)

        #department
        dep=Label(upper_frame,text="Department:",font=("arial",12,"bold"),fg='black',bg='white')
        dep.grid(row=0,column=0,padx=2,sticky=W)
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial,12,bold'),width=15,state='readonly')
        combo_dep['value']=('Select Department','Manager','HR','Software development','Frontend development','backend development')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=3,sticky=W)

        #name
        name=Label(upper_frame,text="Name:",font=("arial",12,"bold"),fg='black',bg='white')
        name.grid(row=0,column=2,padx=8,pady=7,sticky=W)
        e_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        e_name.grid(row=0,column=3,padx=2,pady=7)

        #Designation
        designation=Label(upper_frame,text="Designation:",font=("arial",12,"bold"),fg='black',bg='white')
        designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        e_designation=ttk.Entry(upper_frame,textvariable=self.var_design,width=22,font=("arial",11,"bold"))
        e_designation.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #email
        email=Label(upper_frame,text="E-mail:",font=("arial",12,"bold"),fg='black',bg='white')
        email.grid(row=1,column=2,padx=8,pady=7,sticky=W)
        e_mail=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        e_mail.grid(row=1,column=3,padx=2,pady=7)

        #Address
        address=Label(upper_frame,text="Address:",font=("arial",12,"bold"),fg='black',bg='white')
        address.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        e_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        e_address.grid(row=2,column=1,padx=2,pady=7)

        #Married
        married=Label(upper_frame,text="Married:",font=("arial",12,"bold"),fg='black',bg='white')
        married.grid(row=2,column=2,padx=8,pady=7,sticky=W)
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial,12,bold'),width=15,state='readonly')
        combo_dep['value']=('Select','Married','Unmarried')
        combo_dep.current(0)
        combo_dep.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #dob
        dob=Label(upper_frame,text="DOB:",font=("arial",12,"bold"),fg='black',bg='white')
        dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        e_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        e_dob.grid(row=3,column=1,padx=2,pady=7)
        
        #doj
        doj=Label(upper_frame,text="DOJ:",font=("arial",12,"bold"),fg='black',bg='white')
        doj.grid(row=3,column=2,padx=8,pady=7,sticky=W)
        e_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        e_doj.grid(row=3,column=3,padx=2,pady=7)

        #id proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state='readonly',font=("arial",12,"bold"),width=15)
        com_txt_proof['value']=("Select ID Proof:","Pan Card","Adhar Card","Driving License","Passport")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        e_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        e_proof.grid(row=4,column=1,padx=2,pady=7)

        #gender
        gender=Label(upper_frame,text="Gender:",font=("arial",12,"bold"),fg='black',bg='white')
        gender.grid(row=4,column=2,padx=8,pady=7,sticky=W)
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state='readonly',font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Select","Male","Female","other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #phone
        phone=Label(upper_frame,text="Phone:",font=("arial",12,"bold"),fg='black',bg='white')
        phone.grid(row=0,column=4,padx=8,pady=7,sticky=W)
        e_doj=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        e_doj.grid(row=0,column=5,padx=2,pady=7)

        #country
        country=Label(upper_frame,text="Country:",font=("arial",12,"bold"),fg='black',bg='white')
        country.grid(row=1,column=4,padx=8,pady=7,sticky=W)
        e_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        e_country.grid(row=1,column=5,padx=2,pady=7)
        
        #ctc
        ctc=Label(upper_frame,text="Salary(CTC):",font=("arial",12,"bold"),fg='black',bg='white')
        ctc.grid(row=2,column=4,padx=8,pady=7,sticky=W)
        e_doj=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        e_doj.grid(row=2,column=5,padx=2,pady=7)

        #image mid 
        img_mid=Image.open('images/officenew.jpg')
        img_mid=img_mid.resize((370,220),Image.ANTIALIAS)
        self.photomid=ImageTk.PhotoImage(img_mid)
        self.im_mid=Label(upper_frame,image=self.photomid)
        self.im_mid.place(x=970,y=-15,width=220,height=220)

        #Button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=1250,y=-10,width=200,height=210)
        button_1=Button(button_frame,text="Save",command=self.data_add,font=("arial",15,"bold"),width=13,fg="white",bg="green")
        button_1.grid(row=0,column=0,padx=14,pady=4)
        button_2=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,fg="white",bg="green")
        button_2.grid(row=1,column=0,padx=14,pady=4)
        button_3=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,fg="white",bg="green")
        button_3.grid(row=2,column=0,padx=14,pady=4)
        button_4=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=13,fg="white",bg="green")
        button_4.grid(row=3,column=0,padx=14,pady=4)


        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Information Table",font=("times new roman",20,"bold"),fg='DarkRed',bg='white')
        down_frame.place(x=10,y=260,width=1480,height=290)


        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search Employee Information",font=("times new roman",18,"bold"),fg='darkRed',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=70)
        search_by=Label(search_frame,bd=2,relief=RIDGE,text="Search By",font=("times new roman",15,"bold"),fg='white',bg='OrangeRed')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select option","Phone","Id Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        e_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        e_search.grid(row=0,column=2,padx=5)
        button_search=Button(search_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,fg="white",bg="green")
        button_search.grid(row=0,column=3,padx=5)
        button_showall=Button(search_frame,text="Show all",command=self.fetch_data,font=("arial",11,"bold"),width=14,fg="white",bg="green")
        button_showall.grid(row=0,column=4,padx=5)
        #home=Label(search_frame,bd=2,relief=RIDGE,text="Wear a mask",font=("times new roman",30,"bold"),fg='red',bg='white')
        #home.place(x=780,y=0,width=600,height=30)
        #img_logo_mask=Image.open('images/money.jpg')
        #img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        #self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask)
        #self.lo go=Label(search_frame,image=self.photoimg_logo_mask)
        #self.logo.place(x=900,y=0,width=50,height=30)


        #Employee table
        #Table Frames
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=70,width=1470,height=180)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","des","email","add","marr","dob","doj","comb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading('dep',text="Department")
        self.employee_table.heading('name',text="Name")
        self.employee_table.heading('des',text="Designation")
        self.employee_table.heading('email',text="Email")
        self.employee_table.heading('add',text="Address")
        self.employee_table.heading('marr',text="Married")
        self.employee_table.heading('dob',text="DOB")
        self.employee_table.heading('doj',text="DOJ")
        self.employee_table.heading('comb',text="ID Type")
        self.employee_table.heading('idproof',text="Id Proof")
        self.employee_table.heading('gender',text="Gender")
        self.employee_table.heading('phone',text="Phone")
        self.employee_table.heading('country',text="Country")
        self.employee_table.heading('salary',text="Salary")
        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('des',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('add',width=100)
        self.employee_table.column('marr',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('comb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

        #**********Functions****************
    def data_add(self):
                if self.var_dep.get()=='' or self.var_email.get()=='':
                        messagebox.showerror('Error','All Fields are required')
                else:
                        try:
                                conn=mysql.connector.connect(host='localhost',username='root',password='Yogesh@009',database='mydata')
                                my_cursor=conn.cursor()
                                my_cursor.execute(" INSERT INTO `employee3` VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                         self.var_dep.get(),
                                                                                                         self.var_name.get(),
                                                                                                         self.var_design.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_married.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_doj.get(),
                                                                                                         self.var_idproofcomb.get(),
                                                                                                         self.var_idproof.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_country.get(),
                                                                                                         self.var_salary.get()

                                                                                                                                                                                                                                                 ))


                                conn.commit()
                                self.fetch_data()
                                #conn.close()
                                messagebox.showinfo('Success','Employee has been added!',parent=self.root) 
                        except Exception as es:
                                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
     #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Yogesh@009',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('Select*from employee3')
        data=my_cursor.fetchall()
        if len(data)!=0:
                self.employee_table.delete(*self.employee_table.get_children())
                for i in data:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    #get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_design.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
                 messagebox.showerror('Error','All Fields are required')
        else:
                try:
                        update=messagebox.askyesno('update','Are you sure update this employee data')
                        if update>0:
                                 conn=mysql.connector.connect(host='localhost',username='root',password='Yogesh@009',database='mydata')
                                 my_cursor=conn.cursor()
                                 my_cursor.execute('update employee3 set Department=%s,name=%s,Designation=%s,email=%s,address=%s,dob=%s,doj=%s,married_status=%s,id_proof_type=%s,gender=%s,phone=%s,country=%s,salary=%s where id_proof=%s',(
                                         
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                        self.var_design.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_married.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                                                                        
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                        self.var_idproof.get()

                                                                                                                                                                                                                                ))
                        else:
                                if not update:
                                        return
                        conn.commit()   
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('success','Employee Successfully updated!',parent=self.root)     
                except Exception as es:
                        messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  


    def delete_data(self):
        if self.var_idproof.get()=="":
                 messagebox.showerror('Error',"All fields are required!")
        else:
                try:
                        Delete=messagebox.askyesno('Delete','Are you sure you want to Delete')
                        if Delete>0:
                                conn=mysql.connector.connect(host='localhost',username='root',password='Yogesh@009',database='mydata')
                                my_cursor=conn.cursor()
                                sql='delete from employee3 where id_proof=%s'
                                value=(self.var_idproof.get(),)
                                my_cursor.execute(sql,value)
                        else:
                                if not Delete:
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
                except Exception as es:
                        messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)




    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_design.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")


    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
                messagebox.showerror('Error','Please select option')
        else:
                try:
                        conn=mysql.connector.connect(host='localhost',username='root',password='Yogesh@009',database='mydata')
                        my_cursor=conn.cursor()
                        #my sql query
                        my_cursor.execute('select * from employee3 where ' +str(self.var_com_search.get()+" LIKE '%"+str(self.var_search.get()+"%'")))
                        rows=my_cursor.fetchall()
                        if len(rows)!=0:
                                self.employee_table.delete(*self.employee_table.get_children())
                                for i in rows:
                                        self.employee_table.insert("",END,values=i)
                        conn.commit
                        conn.close()
                except Exception as es:
                        messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



  

        #
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
