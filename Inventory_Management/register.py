import mysql.connector
from tkinter import PhotoImage, Tk, Label, Entry, Button, messagebox



def open_login_window(register_window):
    register_window.destroy()
    
    

def register_user(firstname, lastname, email, password):
    if not (firstname and lastname and email and password):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="register"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)",
                       (firstname, lastname, email, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def open_register_window():
    register_window = Tk()
    register_window.title("User Registration")
    register_window.geometry("725x500+300+200")
    register_window.config(bg="white")
    register_window.resizable(False, False)

    image = PhotoImage(file='C:/Users/HP/OneDrive/Documents/python programe/Inventory_Management/images/p8.png')
    Label(register_window, image=image, bg="white").grid(row=0, column=1, rowspan=4, padx=0, pady=20)

    register_window.columnconfigure(0, weight=1)
    register_window.columnconfigure(1, weight=1)
    register_window.columnconfigure(2, weight=1)
    register_window.columnconfigure(3, weight=1)
    register_window.columnconfigure(4, weight=1)
    register_window.rowconfigure(0, weight=1)
    register_window.rowconfigure(1, weight=1)
    register_window.rowconfigure(2, weight=1)
    register_window.rowconfigure(3, weight=1)
    register_window.rowconfigure(4, weight=1)

    Label(register_window, text="First Name", font=('Arial', 12)).grid(row=0, column=2, pady=10, padx=10, sticky="e")
    entry_first_name = Entry(register_window, font=('Arial', 12), width=25)
    entry_first_name.grid(row=0, column=3, pady=10, padx=10, sticky="w")

    Label(register_window, text="Last Name", font=('Arial', 12)).grid(row=1, column=2, pady=10, padx=10, sticky="e")
    entry_last_name = Entry(register_window, font=('Arial', 12), width=25)
    entry_last_name.grid(row=1, column=3, pady=10, padx=10, sticky="w")

    Label(register_window, text="Email", font=('Arial', 12)).grid(row=2, column=2, pady=10, padx=10, sticky="e")
    entry_email = Entry(register_window, font=('Arial', 12), width=25)
    entry_email.grid(row=2, column=3, pady=10, padx=10, sticky="w")

    Label(register_window, text="Password", font=('Arial', 12)).grid(row=3, column=2, pady=10, padx=10, sticky="e")
    entry_password = Entry(register_window, font=('Arial', 12), width=25, show="*")
    entry_password.grid(row=3, column=3, pady=10, padx=10, sticky="w")


    Button(register_window, text="Register", font=('Arial', 15), bg='blue', fg='white', width=30, command=lambda: register_user(
        entry_first_name.get(),
        entry_last_name.get(),
        entry_email.get(),
        entry_password.get()
    )).grid(row=4, column=2, columnspan=2, pady=20, padx=20)

    register_window.mainloop()

