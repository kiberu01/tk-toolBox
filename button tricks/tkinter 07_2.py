import tkinter

def onClick():
    print(radioVar.get())

window=tkinter.Tk()
window.title("Tkinter tutorial")

radioVar=tkinter.StringVar()
radio=tkinter.Radiobutton(window, variable=radioVar, text="june", value="june month", command=onClick)
radio1=tkinter.Radiobutton(window, variable=radioVar, text="july", value="july month", command=onClick)
radio2=tkinter.Radiobutton(window, variable=radioVar, text="august", value="august month", command=onClick)
radio3=tkinter.Radiobutton(window, variable=radioVar, text="september", value="september month", command=onClick)

radio.pack()
radio1.pack()
radio2.pack()
radio3.pack()

window.mainloop()
