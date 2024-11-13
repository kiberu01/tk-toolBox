import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login form")
window.geometry('440x340')
window.configure(bg='#333333')

def login():
    username="Elly KIBERU"
    password="123456789"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in")
    else:
        messagebox.showerror(title="Error", message="Login failed")

frame=tkinter.Frame(bg='#333333')

# Creating the widgets
login_label=tkinter.Label(frame, text="Login", bg='#333333', fg='#FF3399', font=("Arial", 20))
username_label=tkinter.Label(frame, text="Username", bg='#333333', fg='#FFFFFF', font=("Arial", 12))
username_entry=tkinter.Entry(frame, font=("Arial", 12))
password_label=tkinter.Label(frame, text="Password", bg='#333333', fg='#FFFFFF', font=("Arial", 12))
password_entry=tkinter.Entry(frame, show="*", font=("Arial", 12))
login_button=tkinter.Button(frame, text="Login", bg='#FF3399', fg='#FFFFFF', font=("Arial", 12), command=login)

# Placing the widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=35)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=15)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=15)
login_button.grid(row=3, column=0, columnspan=2, pady=25)

frame.pack()

window.mainloop()