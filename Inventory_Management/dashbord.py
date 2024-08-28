from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from employee import employeeclass
import mysql.connector
from supplier import supplierclass
from category import categoryclass
from product import productclass
import login
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x785+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        title=Label(self.root,text="Inventory Management System", bg="#cf94d1", fg="black",bd=10,relief=RIDGE,font=("times new roman",25,"bold"),padx=0,pady=2)
        title.pack(side=TOP,fill=X)
        btn_logout=Button(self.root,text="Logout", bg="#d94559",fg="black",command=self.logout,cursor='hand2',font=("times new roman",15,"bold")).place(x=1300,y=10,height=40,width=150)
        
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", bg="#e8cfe4", fg="black",bd=10,font=("times new roman",15))
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=35)
        
        
        self.MenuLogo=Image.open("C:/Users/HP/OneDrive/Documents/python programe/Inventory_Management/images/i1.png")
        self.MenuLogo=self.MenuLogo.resize((250,250),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=6,relief=RIDGE,bg='white')
        LeftMenu.place(x=0,y=102,width=300,height=638)
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu=Label(LeftMenu,text="Menu", bg="#f711d1",fg="black",cursor='hand2',font=("times new roman",18,"bold")).pack(side=TOP,fill=X, pady=(0,40))
        
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee, bg="#cf94d1",fg="black",bd=3,cursor='hand2',font=("times new roman",15,"bold")).pack(side=TOP,fill=X,pady=(0, 12))
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier, bg="#cf94d1",fg="black",bd=3,cursor='hand2',font=("times new roman",15,"bold")).pack(side=TOP,fill=X,pady=(0, 12))
        btn_category=Button(LeftMenu,text="Category",command=self.category, bg="#cf94d1",fg="black",bd=3,cursor='hand2',font=("times new roman",15,"bold")).pack(side=TOP,fill=X,pady=(0, 12))
        btn_product=Button(LeftMenu,text="Product",command=self.product, bg="#cf94d1",fg="black",bd=3,cursor='hand2',font=("times new roman",15,"bold")).pack(side=TOP,fill=X,pady=(0, 12))
        btn_exit=Button(LeftMenu,text="Exit", bg="#cf94d1",fg="black",bd=3,cursor='hand2',font=("times new roman",15,"bold")).pack(side=TOP,fill=X)
        
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#9a5bde",fg="black",font=("times new roman",15,"bold"))
        self.lbl_employee.place(x=400,y=200,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="#9a5bde",fg="black",font=("times new roman",15,"bold"))
        self.lbl_supplier.place(x=750,y=200,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#9a5bde",fg="black",font=("times new roman",15,"bold"))
        self.lbl_category.place(x=1100,y=200,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#9a5bde",fg="black",font=("times new roman",15,"bold"))
        self.lbl_product.place(x=700,y=400,height=150,width=300)




       
        lbl_footer=Label(self.root,text=" Inventory Management System | Tharushi Anjana\n For any Technical Issue Contact:0771630706", bg="#e8cfe4", fg="black",font=("times new roman",12)).pack(side=BOTTOM,fill=X)
        
        self.update_content()
        
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)
        
    def update_content(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
        my_cursor = conn.cursor()
        try:
            my_cursor.execute("select * from product")
            product=my_cursor.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ {str(len(product))} ]')
            
            my_cursor.execute("select * from category")
            category=my_cursor.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')
            
            my_cursor.execute("select * from employee")
            employee=my_cursor.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')
            
            my_cursor.execute("select * from supplier")
            supplier=my_cursor.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')
            
            current_time = time.strftime("%I:%M:%S %p")
            current_date = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {current_date}\t\t Time: {current_time}")
            self.root.after(1000, self.update_content)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def logout(self):
        
        self.root.destroy()
        
        login_window = Tk()
        login.LoginClass(login_window)
        login_window.mainloop()

if __name__=="__main__":    
    root=Tk()
    obj=IMS(root)
    root.mainloop()