import tkinter

def onTap():
    print(checkVar.get())

window=tkinter.Tk()
window.title("Tkinter tutorial")

checkVar=tkinter.StringVar()
check=tkinter.Checkbutton(window, text="Check me!", variable=checkVar, onvalue="yes", offvalue="no", command=onTap)
check.pack()

window.mainloop()
