import tkinter
from tkinter import messagebox

def openMessageBox():
    # messagebox.showinfo(title="Info Message", message="This is an info message")
    # messagebox.showerror(title="Error", message="You made an error")
    # messagebox.showwarning(title="Warning", message="Do not close this window")
    
    # messagebox.askokcancel(title="Qusetion", message="Wanna proceed?")
    # result = messagebox.askretrycancel(title="Question", message="Wanna retry?")
    # print(result)
    # result_question = messagebox.askquestion(title="Question", message="Do you wish to continue?")
    
    # result_yesno = messagebox.askyesno(title="Question", message="Do you wish to continue?")
    # if result_question=="yes":
    #     print("User chose Yes")
    # else:
    #     print("User chose No")
    rslt = messagebox.askyesnocancel(title="Question", message="Wanna proceed?")
    print(rslt)


window=tkinter.Tk()

button = tkinter.Button(window, text="Press Me", command=openMessageBox)
button.pack()

window.mainloop()