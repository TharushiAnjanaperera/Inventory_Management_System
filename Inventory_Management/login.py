import os
from tkinter import Tk, Label, Frame, Entry, Button, PhotoImage, messagebox
import mysql.connector



class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x500+300+200")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.root.focus_force()

        self.img = PhotoImage(file=r'C:\Users\HP\OneDrive\Documents\python programe\Inventory_Management\images\p3.png')
        Label(self.root, image=self.img, bg='white').place(x=60, y=100)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=370, y=70)

        heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('arial', 23, 'bold'))
        heading.place(x=80, y=5)

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            name = self.user.get()
            if name == '':
                self.user.insert(0, 'Email')

        self.user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('arial', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.code.delete(0, 'end')

        def on_leave(e):
            name = self.code.get()
            if name == '':
                self.code.insert(0, 'Password')

        self.code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('arial', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', on_enter)
        self.code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(frame, width=39, pady=7, text="Log in", bg='#57a1f8', fg="white", border=0, command=self.OK, font=('arial', 12)).place(x=0, y=200)


    def OK(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="register")
            mycursor = conn.cursor()
            email = self.user.get()
            password = self.code.get()
            
            

            sql = "SELECT * FROM employee WHERE email = %s AND pass = %s"
            mycursor.execute(sql, (email, password))
            results = mycursor.fetchall()
            
           

            if results:
               
                    messagebox.showinfo("", "Login Success")
                    self.root.destroy()
                    os.system('python  "c:/Users/HP/OneDrive/Documents/python programe/Inventory_Management/dashbord.py"')

            else:
                messagebox.showinfo("", "Login Unsuccessful.Incorect Email or password")
                
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database connection error: {err}")
        finally:
            if mycursor:
                mycursor.close()
            if conn:
                conn.close()

if __name__ == "__main__":    
    root = Tk()
    obj = LoginClass(root)
    root.mainloop()