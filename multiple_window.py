import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def ask_yes_no():
    messagebox.askquestion('Title', 'Body')
    
def create_window():
    # The word "global" is to make the variable global
    global extra_window
    extra_window = tk.Toplevel()
    extra_window.title('Extra Window')
    extra_window.geometry('500x300')
    ttk.Label(extra_window, text="A label").pack()
    ttk.Button(extra_window, text="Button").pack()
    ttk.Label(extra_window, text="Another label").pack(expand=True)

def close_window():
    extra_window.destroy()


window = tk.Tk()
window.geometry('600x400')
window.title('Multiple Window')

button1 = ttk.Button(window, text='Open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text='create yes no window', command=ask_yes_no)
button3.pack(expand=True)


window.mainloop()