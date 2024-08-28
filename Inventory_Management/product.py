from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

class productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1228x600+300+135")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.root.focus_force()
        
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.categories_list=[]
        self.supplier_list=[]
        self.fetch_categories_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        SearchFrame = LabelFrame(self.root, text="Search Product", font=("times new roman", 15), bd=2, relief=RIDGE, bg='white')
        SearchFrame.place(x=550, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Name", "Supplier"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("times new roman", 12), bg='#d2b3f2')
        txt_search.place(x=200, y=10, width=180)
        
        btn_search = Button(SearchFrame, text='Search', font=("arial", 12, "bold"),command=self.search, bg='#57fa32', cursor="hand2")
        btn_search.place(x=400, y=6, width=100, height=30)
        
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=15,width=450,height=480)
        
        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style",15, "bold"), bg="#cf94d1", fg='black')
        title.pack(side=TOP,fill=X)
        
        lbl_category = Label(self.root, text="Category", font=("goudy old style",13), bg="white", fg='black')
        lbl_category.place(x=30,y=60)
        lbl_supplier = Label(self.root, text="Supplier", font=("goudy old style",13), bg="white", fg='black')
        lbl_supplier.place(x=30,y=110)
        lbl_productName = Label(self.root, text="Product Name", font=("goudy old style",13), bg="white",fg="black")
        lbl_productName.place(x=30,y=160)
        lbl_price = Label(self.root, text="Price", font=("goudy old style",13), bg="white", fg='black')
        lbl_price.place(x=30,y=210)
        lbl_quantity = Label(self.root, text="Quantity", font=("goudy old style",13), bg="white", fg='black')
        lbl_quantity.place(x=30,y=260)
        lbl_status = Label(self.root, text="Status", font=("goudy old style",13), bg="white", fg='black')
        lbl_status.place(x=30,y=310)
        
        cmb_cat = ttk.Combobox(self.root, textvariable=self.var_cat,values=self.categories_list, state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)
         
               
        cmb_sup = ttk.Combobox(self.root, textvariable=self.var_sup,values=self.supplier_list, state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)
        
        txt_name= Entry(self.root,textvariable=self.var_name, font=("arial", 12), bg='#ddc5ed')
        txt_name.place(x=150, y=160, width=200)
        
        txt_price= Entry(self.root,textvariable=self.var_price, font=("arial", 12), bg='#ddc5ed')
        txt_price.place(x=150, y=210, width=200)
        
        txt_qty= Entry(self.root,textvariable=self.var_qty, font=("arial", 12), bg='#ddc5ed')
        txt_qty.place(x=150, y=260, width=200)
        
        cmb_status = ttk.Combobox(self.root, textvariable=self.var_status,values=("Selected","Active","Inactive"), state='readonly', justify=CENTER, font=("times new roman", 12))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)
        
        btn_add = Button(self.root, text='Save',font=("arial", 12, "bold"),command=self.add,bg='#4f68e3', cursor="hand2")
        btn_add.place(x=20, y=400, width=90, height=28)

        btn_update = Button(self.root, text='Update',font=("arial", 12, "bold"),command=self.update, bg='#1ee649', cursor="hand2")
        btn_update.place(x=120, y=400, width=90, height=28)

        btn_delete = Button(self.root, text='Delete',font=("arial", 12, "bold"),command=self.delete, bg='#f5331d', cursor="hand2")
        btn_delete.place(x=220, y=400, width=90, height=28)

        btn_clear = Button(self.root, text='Clear',font=("arial", 12, "bold"),command=self.reset, bg='#827a79', cursor="hand2")
        btn_clear.place(x=320, y=400, width=90, height=28)
        
        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=500,y=100,width=730,height=450)
        
        Scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        Scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)
        
        self.ProductTable=ttk.Treeview(pro_frame,columns=("pid","category","supplier","name","price","qty","status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.ProductTable.xview)
        Scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("pid",text="PID")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Qty")
        self.ProductTable.heading("status",text="Status")
        
        
        self.ProductTable["show"]="headings"
        self.ProductTable.pack(fill=BOTH,expand=1)
        
        self.ProductTable.column("pid",width=50)
        self.ProductTable.column("category",width=50)
        self.ProductTable.column("supplier",width=50)
        self.ProductTable.column("name",width=50)
        self.ProductTable.column("price",width=50)
        self.ProductTable.column("qty",width=50)
        self.ProductTable.column("status",width=50)
        
        
        self.fatch_data()
        self.fetch_categories_sup()
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        
    def add(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        
        pro_name = self.var_name.get()
   
        values = (
        
        self.var_cat.get(),
        self.var_sup.get(),
        pro_name,
        self.var_price.get(),
        self.var_qty.get(),
        self.var_status.get(),
        
        
    )
        
        my_cursor.execute("SELECT * FROM product WHERE name = %s", (pro_name,))
        existing_record = my_cursor.fetchone()

        if existing_record:
            messagebox.showwarning("Warning", "Product already exists.")
        else:
            sql_query = """INSERT INTO product (category,supplier,name,price,qty,status) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
   
        my_cursor.execute(sql_query, values)
        
        messagebox.showinfo("Success", "Product has been inserted successfully")
    
        conn.commit()
        my_cursor.close()
        self.fatch_data()
        conn.close()
        
       
       
        
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        pro_name = self.var_name.get()

        my_cursor.execute("SELECT * FROM product WHERE name = %s", (pro_name,))
        existing_record = my_cursor.fetchone()

        if not existing_record:
            messagebox.showwarning("Warning", "Product does not exist. Cannot update.")
            conn.close()
            return

        values = (
        self.var_cat.get(),
        self.var_sup.get(),
        self.var_price.get(),
        self.var_qty.get(),
        self.var_status.get(),
        pro_name
    )

        sql_query = """UPDATE product
               SET category = %s, supplier = %s, price = %s, qty = %s, status = %s
               WHERE name = %s"""


    
        my_cursor.execute(sql_query, values)
        conn.commit()
        messagebox.showinfo("Success", "Product record updated successfully")
    
        my_cursor.close()
        conn.close()
        self.fatch_data()
  
        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from product")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.ProductTable.delete(*self.ProductTable.get_children())
            for  i in  rows:
                self.ProductTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_data(self, ev):
        cursor_row = self.ProductTable.focus()
        content = self.ProductTable.item(cursor_row)
        row = content['values']

        if row:
            self.var_cat.set(row[1])   # Category
            self.var_sup.set(row[2])   # Supplier
            self.var_name.set(row[3])  # Name
            self.var_price.set(row[4]) # Price
            self.var_qty.set(row[5])   # Quantity
            self.var_status.set(row[6]) # Status

    def delete(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","First select the product") 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
            my_cursor = conn.cursor() 
            query="delete from product where name=%s"  
            value =(self.var_name.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Product has been deleted")
            
    def reset(self):
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()

        search_by = self.var_searchby.get()
        search_txt = self.var_searchtxt.get()

        if search_by == "Select" or not search_txt:
            messagebox.showerror("Error", "Please select a search option and enter a search value.")
            return

        if search_by == "Category":
            query = "SELECT * FROM product WHERE category LIKE %s"
            value = ('%' + search_txt + '%',)
        elif search_by == "Name":
            query = "SELECT * FROM product WHERE name LIKE %s"
            value = ('%' + search_txt + '%',)
            
        elif search_by == "Supplier":
            query = "SELECT * FROM product WHERE supplier LIKE %s"
            value = ('%' + search_txt + '%',)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:    
                self.ProductTable.insert("", END, values=row)

        else:
            messagebox.showinfo("No Results", "No matching records found.")

        conn.close()
        
    def fetch_categories_sup(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        self.categories_list.append("Empty")
        self.supplier_list.append("Empty")
        try:
            my_cursor.execute("SELECT name FROM category") 
            categories = my_cursor.fetchall() 
            if len(categories)>0:
                del self.categories_list[:]
                self.categories_list.append("Selected")
            
                for i in categories:
                    self.categories_list.append(i[0])
        
            
            my_cursor.execute("SELECT name FROM supplier") 
            supplier = my_cursor.fetchall() 
            if len(supplier)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Selected")
            
                for i in supplier:
                    self.supplier_list.append(i[0])
            
          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       
        
if __name__ == "__main__":    
    root = Tk()
    obj = productclass(root)
    root.mainloop()