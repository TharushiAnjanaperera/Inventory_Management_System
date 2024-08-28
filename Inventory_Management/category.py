from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

class categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1228x600+300+135")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.root.focus_force()
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        title = Label(self.root, text="Manage Product Category", font=("arial",18, "bold"), bg="#cf94d1", fg='black',relief=RIDGE,bd=3)
        title.pack(side=TOP,fill=X,padx=10,pady=2)
        
        lbl_name = Label(self.root, text="Enter Category Name", font=("arial", 13), fg='black',bg='white')
        lbl_name.place(x=50, y=100)
        
        txt_name= Entry(self.root,textvariable=self.var_name, font=("arial", 12), bg='#ddc5ed')
        txt_name.place(x=100, y=130, width=250,height=30)
        
        btn_add = Button(self.root, text='Add', font=("arial", 12, "bold"),command=self.add,bg='green', cursor="hand2")
        btn_add.place(x=400, y=130, width=110, height=28)
        
        btn_delete = Button(self.root, text='Delete', font=("arial", 12, "bold"),command=self.delete, bg='red', cursor="hand2")
        btn_delete.place(x=550, y=130, width=110, height=28)
        
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=750,y=120,width=450,height=150)
        
        Scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        Scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.categoryTable=ttk.Treeview(cat_frame,columns=("CID","name"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.categoryTable.xview)
        Scrolly.config(command=self.categoryTable.yview)
        
        
        self.categoryTable.heading("CID",text="CID")
        self.categoryTable.heading("name",text="Name")
        
        
        self.categoryTable["show"]="headings"
        self.categoryTable.pack(fill=BOTH,expand=1)
        
        self.categoryTable.column("CID",width=80)
        self.categoryTable.column("name",width=90)
        
        self.show_data()
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        
        self.im1=Image.open("C:/Users/HP/OneDrive/Documents/python programe/Inventory_Management/images/cat1.png")
        self.im1=self.im1.resize((400,300),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=3,relief=RIDGE)
        self.lbl_im1.place(x=50,y=220)
        
        self.im2=Image.open("C:/Users/HP/OneDrive/Documents/python programe/Inventory_Management/images/cat2.png")
        self.im2=self.im2.resize((500,300),Image.Resampling.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2,bd=3,relief=RIDGE)
        self.lbl_im2.place(x=600,y=290)
        
    def add(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
            
           
        name= self.var_name.get()
    
        
        my_cursor.execute("SELECT * FROM category WHERE name = %s", (name,))
        existing_record = my_cursor.fetchone()

        if existing_record:
            messagebox.showwarning("Warning", "Category Already Present. Please try different")
        else:
            sql_query = """INSERT INTO category (name) 
                    VALUES (%s)"""
   
        my_cursor.execute(sql_query,(name,))
        
        messagebox.showinfo("Success", "Category has been inserted successfully")
    
        conn.commit()
        self.show_data()
        my_cursor.close()
        conn.close()
        
    def show_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from category")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.categoryTable.delete(*self.categoryTable.get_children())
            for  i in  rows:
                self.categoryTable.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_data(self,event=""):
        cursor_row=self.categoryTable.focus()
        content=self.categoryTable.item(cursor_row)
        row=content['values']
        
        self.var_name.set(row[1])
       
        
    def delete(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","First select the Category") 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
            my_cursor = conn.cursor() 
            query="delete from category where name=%s"  
            value =(self.var_name.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.show_data()
            conn.close()
            
            messagebox.showinfo("Success","Supplier has been deleted")
        
if __name__ == "__main__":    
    root = Tk()
    obj = categoryclass(root)
    root.mainloop()
