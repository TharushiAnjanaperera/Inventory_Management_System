from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

class supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1228x600+300+135")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice= StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        

        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 15), bd=2, relief=RIDGE, bg='white')
        SearchFrame.place(x=300, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Name","Invoice"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt, font=("times new roman", 12), bg='#d2b3f2')
        txt_search.place(x=200, y=10, width=180)
        
        btn_search = Button(SearchFrame, text='Search', font=("arial", 12, "bold"),command=self.search, bg='#57fa32', cursor="hand2")
        btn_search.place(x=400, y=6, width=180, height=30)

        title = Label(self.root, text="Supplier Details", font=("arial", 13, "bold"), bg="#cf94d1", fg='black')
        title.place(x=50, y=100, width=1130)


        lbl_suplier_invoice = Label(self.root, text="Supplier Invoice", font=("arial", 12), bg="white")
        lbl_suplier_invoice.place(x=50, y=150)

        txt_suplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("arial", 12), bg='#ddc5ed')
        txt_suplier_invoice.place(x=190, y=150, width=180)

        
        lbl_name = Label(self.root, text="Name", font=("arial", 12), bg="white")
        lbl_name.place(x=400, y=150)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("arial", 12), bg='#ddc5ed')
        txt_name.place(x=500, y=150, width=180)

        lbl_contact = Label(self.root, text="Contact Number", font=("arial", 12), bg="white")
        lbl_contact.place(x=750, y=150)
        
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("arial", 12), bg='#ddc5ed')
        txt_contact.place(x=900, y=150, width=180)

        lbl_desc= Label(self.root, text="Description", font=("arial", 12), bg="white")
        lbl_desc.place(x=50, y=200)
        self.txt_desc=Text(self.root,font=("arial", 12),bg='#ddc5ed')
        self.txt_desc.place(x=150,y=200,height=60,width=300)

        btn_add = Button(self.root, text='Save',command=self.add, font=("arial", 12, "bold"), bg='#4f68e3', cursor="hand2")
        btn_add.place(x=500, y=305, width=110, height=28)

        btn_update = Button(self.root, text='Update',command=self.update, font=("arial", 12, "bold"), bg='#1ee649', cursor="hand2")
        btn_update.place(x=620, y=305, width=110, height=28)

        btn_delete = Button(self.root, text='Delete',command=self.delete, font=("arial", 12, "bold"), bg='#f5331d', cursor="hand2")
        btn_delete.place(x=740, y=305, width=110, height=28)

        btn_clear = Button(self.root, text='Clear',command=self.reset, font=("arial", 12, "bold"), bg='#827a79', cursor="hand2")
        btn_clear.place(x=860, y=305, width=110, height=28)


        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=10,y=350,relwidth=1,height=205)
        
        Scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        Scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.SupplierTable.xview)
        Scrolly.config(command=self.SupplierTable.yview)
        
        
        self.SupplierTable.heading("invoice",text="Supplier Invoice")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        
        
        self.SupplierTable["show"]="headings"
        self.SupplierTable.pack(fill=BOTH,expand=1)
        
        self.SupplierTable.column("invoice",width=80)
        self.SupplierTable.column("name",width=90)
        self.SupplierTable.column("contact",width=90)
        self.SupplierTable.column("desc",width=90)
       
        
        self.fatch_data()
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        
    def add(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        
        sup_invoice = self.var_sup_invoice.get()
   
        values = (
        sup_invoice,
        self.var_name.get(),
        self.var_contact.get(),
        self.txt_desc.get("1.0", "end-1c"),
        
    )
        
        my_cursor.execute("SELECT * FROM supplier WHERE invoice = %s", (sup_invoice,))
        existing_record = my_cursor.fetchone()

        if existing_record:
            messagebox.showwarning("Warning", "Supplier invoice already exists. Please use a unique invoice.")
        else:
            sql_query = """INSERT INTO supplier (invoice,name,contact,description) 
                    VALUES (%s, %s, %s, %s)"""
   
        my_cursor.execute(sql_query, values)
        
        messagebox.showinfo("Success", "Supplier has been inserted successfully")
    
        conn.commit()
        my_cursor.close()
        self.fatch_data()
        self.show()
        conn.close()
        
        
        
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        sup_invoice = self.var_sup_invoice.get()

        my_cursor.execute("SELECT * FROM supplier WHERE invoice = %s", (sup_invoice,))
        existing_record = my_cursor.fetchone()

        if not existing_record:
            messagebox.showwarning("Warning", "Supplier invoice does not exist. Cannot update.")
            conn.close()
            return

        values = (
        self.var_name.get(),
        self.var_contact.get(),
        self.txt_desc.get("1.0", "end-1c"),
        sup_invoice
    )

        sql_query = """UPDATE supplier
                   SET name = %s, contact = %s,description = %s
                   WHERE invoice = %s"""

    
        my_cursor.execute(sql_query, values)
        conn.commit()
        messagebox.showinfo("Success", "Supplier record updated successfully")
    
        my_cursor.close()
        conn.close()
        self.fatch_data()
  
        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from supplier")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for  i in  rows:
                self.SupplierTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_data(self,event=""):
        cursor_row=self.SupplierTable.focus()
        content=self.SupplierTable.item(cursor_row)
        row=content['values']
        
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        
        self.txt_desc.delete('1.0', 'end')  
        self.txt_desc.insert('1.0', row[3]) 
        
    def delete(self):
        if self.var_sup_invoice.get()=="":
            messagebox.showerror("Error","First select the invoice") 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
            my_cursor = conn.cursor() 
            query="delete from supplier where invoice=%s"  
            value =(self.var_sup_invoice.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Supplier has been deleted")
            
    def reset(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete("1.0", "end")
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        search_by = self.var_searchby.get()
        search_txt = self.var_searchtxt.get()

        if search_by == "Select" or not search_txt:
            messagebox.showerror("Error", "Please select a search option and enter a search value.")
            return

        if search_by == "Invoice":
            query = "SELECT * FROM supplier WHERE invoice LIKE %s"
            value = ('%' + search_txt + '%',)
        elif search_by == "Name":
            query = "SELECT * FROM supplier WHERE name LIKE %s"
            value = ('%' + search_txt + '%',)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert("", END, values=row)
        else:
            messagebox.showinfo("No Results", "No matching records found.")

        conn.close()
        
    
if __name__ == "__main__":    
    root = Tk()
    obj = supplierclass(root)
    root.mainloop()
