import tkinter

if __name__=='__main__':
    
    def printMsg():
        print(textentry.get())
    
    window=tkinter.Tk()
    window.title("Tkinter First App")
    window.geometry('600x400')
    
    label=tkinter.Label(window, text='Hello World', bg="yellow", fg="red", width=50)
    label.pack()
    textentry=tkinter.Entry(window, bg="pink", width=50)
    textentry.pack()
    button=tkinter.Button(window, text='Hello', bg="green", activebackground="purple", command=printMsg)
    button.pack()
    
    
    window.mainloop()