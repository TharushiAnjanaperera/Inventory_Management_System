from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

class employeeclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1228x600+300+135")
        
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary= StringVar()

        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 15), bd=2, relief=RIDGE, bg='white')
        SearchFrame.place(x=300, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "EmpID"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("times new roman", 12), bg='#d2b3f2')
        txt_search.place(x=200, y=10, width=180)
        
        btn_search = Button(SearchFrame, text='Search', font=("arial", 12, "bold"),command=self.search, bg='#57fa32', cursor="hand2")
        btn_search.place(x=400, y=6, width=180, height=30)

        title = Label(self.root, text="Employee Details", font=("arial", 13, "bold"), bg="#cf94d1", fg='black')
        title.place(x=50, y=100, width=1130)


        lbl_empid = Label(self.root, text="Emp ID", font=("arial", 12), bg="white")
        lbl_empid.place(x=50, y=150)

        lbl_gender = Label(self.root, text="Gender", font=("arial", 12), bg="white")
        lbl_gender.place(x=400, y=150)

        lbl_contact = Label(self.root, text="Contact", font=("arial", 12), bg="white")
        lbl_contact.place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("arial", 12), bg='#ddc5ed')
        txt_empid.place(x=150, y=150, width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select", "Male", "Female"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("arial", 12), bg='#ddc5ed')
        txt_contact.place(x=850, y=150, width=180)
        
        lbl_name = Label(self.root, text="Name", font=("arial", 12), bg="white")
        lbl_name.place(x=50, y=190)

        lbl_dob = Label(self.root, text="D.O.B", font=("arial", 12), bg="white")
        lbl_dob.place(x=400, y=190)

        lbl_doj = Label(self.root, text="D.O.J", font=("arial", 12), bg="white")
        lbl_doj.place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("arial", 12), bg='#ddc5ed')
        txt_name.place(x=150, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("arial", 12), bg='#ddc5ed')
        txt_dob.place(x=500, y=190, width=180)
        
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("arial", 12), bg='#ddc5ed')
        txt_doj.place(x=850, y=190, width=180)
        
        lbl_email = Label(self.root, text="Email", font=("arial", 12), bg="white")
        lbl_email.place(x=50, y=230)

        lbl_pass = Label(self.root, text="Password", font=("arial", 12), bg="white")
        lbl_pass.place(x=400, y=230)

        lbl_u_type = Label(self.root, text="User Type", font=("arial", 12), bg="white")
        lbl_u_type.place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("arial", 12), bg='#ddc5ed')
        txt_email.place(x=150, y=230, width=180)
        
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("arial", 12), bg='#ddc5ed')
        txt_pass.place(x=500, y=230, width=180)

        cmb_U_type = ttk.Combobox(self.root, textvariable=self.var_utype,values=("Select", "Admin", "Employee"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_U_type.place(x=850, y=230, width=180)
        cmb_U_type.current(0)
        
        lbl_address= Label(self.root, text="Address", font=("arial", 12), bg="white")
        lbl_address.place(x=50, y=270)

        lbl_salary = Label(self.root, text="Salary", font=("arial", 12), bg="white")
        lbl_salary.place(x=500, y=270)
        
        self.txt_address=Text(self.root,font=("arial", 12),bg='#ddc5ed')
        self.txt_address.place(x=150,y=270,height=60,width=300)
        
        txt_salary=Entry(self.root, textvariable=self.var_salary, font=("arial", 12), bg='#ddc5ed')
        txt_salary.place(x=600, y=270, width=180)

        btn_add = Button(self.root, text='Save',command=self.add, font=("arial", 12, "bold"), bg='#4f68e3', cursor="hand2")
        btn_add.place(x=500, y=305, width=110, height=28)

        btn_update = Button(self.root, text='Update',command=self.update, font=("arial", 12, "bold"), bg='#1ee649', cursor="hand2")
        btn_update.place(x=620, y=305, width=110, height=28)

        btn_delete = Button(self.root, text='Delete',command=self.delete, font=("arial", 12, "bold"), bg='#f5331d', cursor="hand2")
        btn_delete.place(x=740, y=305, width=110, height=28)

        btn_clear = Button(self.root, text='Clear',command=self.reset, font=("arial", 12, "bold"), bg='#827a79', cursor="hand2")
        btn_clear.place(x=860, y=305, width=110, height=28)


        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=245)
        
        Scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        Scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.EmployeeTable.xview)
        Scrolly.config(command=self.EmployeeTable.yview)
        
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="UserType")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        
        self.fatch_data()
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
    def add(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        
        emp_id = self.var_emp_id.get()
   
        values = (
        emp_id,
        self.var_name.get(),
        self.var_email.get(),
        self.var_gender.get(),
        self.var_contact.get(),
        self.var_dob.get(), 
        self.var_doj.get(),
        self.var_pass.get(),
        self.var_utype.get(),
        self.txt_address.get("1.0", "end-1c"),
        self.var_salary.get()
    )
        
        my_cursor.execute("SELECT * FROM employee WHERE empid = %s", (emp_id,))
        existing_record = my_cursor.fetchone()

        if existing_record:
            messagebox.showwarning("Warning", "Employee ID already exists. Please use a unique ID.")
        else:
            sql_query = """INSERT INTO employee (empid,name,email,gender,contact,dob,doj,pass,utype,address,salary) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   
        my_cursor.execute(sql_query, values)
        
        messagebox.showinfo("Success", "Employee has been inserted successfully")
    
        conn.commit()
        my_cursor.close()
        self.fatch_data()
        self.show()
        conn.close()
        
       
       
        
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        emp_id = self.var_emp_id.get()

        my_cursor.execute("SELECT * FROM employee WHERE empid = %s", (emp_id,))
        existing_record = my_cursor.fetchone()

        if not existing_record:
            messagebox.showwarning("Warning", "Employee ID does not exist. Cannot update.")
            conn.close()
            return

        values = (
        self.var_name.get(),
        self.var_email.get(),
        self.var_gender.get(),
        self.var_contact.get(),
        self.var_dob.get(),
        self.var_doj.get(),
        self.var_pass.get(),
        self.var_utype.get(),
        self.txt_address.get("1.0", "end-1c"),
        self.var_salary.get(),
        emp_id
    )

        sql_query = """UPDATE employee
                   SET name = %s, email = %s, gender = %s, contact = %s, dob = %s, doj = %s, pass = %s, utype = %s, address = %s, salary = %s
                   WHERE empid = %s"""

    
        my_cursor.execute(sql_query, values)
        conn.commit()
        messagebox.showinfo("Success", "Employee record updated successfully")
    
        my_cursor.close()
        conn.close()
        self.fatch_data()
  
        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for  i in  rows:
                self.EmployeeTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_data(self,event=""):
        cursor_row=self.EmployeeTable.focus()
        content=self.EmployeeTable.item(cursor_row)
        row=content['values']
        
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]), 
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_salary.set(row[10])
        
        self.txt_address.delete('1.0', 'end')  
        self.txt_address.insert('1.0', row[9]) 
        
    def delete(self):
        if self.var_emp_id.get()=="":
            messagebox.showerror("Error","First select the member") 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
            my_cursor = conn.cursor() 
            query="delete from employee where empid=%s"  
            value =(self.var_emp_id.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been deleted")
            
    def reset(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set(""),
        self.txt_address.delete("1.0", "end"),
        self.var_salary.set("")
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        search_by = self.var_searchby.get()
        search_txt = self.var_searchtxt.get()

        if search_by == "Select" or not search_txt:
            messagebox.showerror("Error", "Please select a search option and enter a search value.")
            return

        if search_by == "Email":
            query = "SELECT * FROM employee WHERE email LIKE %s"
            value = ('%' + search_txt + '%',)
        elif search_by == "Name":
            query = "SELECT * FROM employee WHERE name LIKE %s"
            value = ('%' + search_txt + '%',)
            
        elif search_by == "EmpID":
            query = "SELECT * FROM employee WHERE empid LIKE %s"
            value = ('%' + search_txt + '%',)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert("", END, values=row)
        else:
            messagebox.showinfo("No Results", "No matching records found.")

        conn.close()
    
if __name__ == "__main__":    
    root = Tk()
    obj = employeeclass(root)
    root.mainloop()
