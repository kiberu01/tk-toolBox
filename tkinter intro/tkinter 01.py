import tkinter

def hello():
    print("Hello world")

window=tkinter.Tk()
button=tkinter.Button(window, text='Hello World', command=hello)
button.pack()
window.mainloop()
