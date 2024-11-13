import tkinter

def spinPressed():
    print(spinVar.get())

window=tkinter.Tk()
window.title("Tkinter tutorial")

spinVar=tkinter.StringVar()

# spin=tkinter.Spinbox(window, from_=0, to='infinity')
# spin=tkinter.Spinbox(window, from_=0, to=10, increment=0.1)
spin=tkinter.Spinbox(window, values=["hello","hi","yes","no"], textvariable=spinVar, command=spinPressed)
spin.pack()

window.mainloop()
