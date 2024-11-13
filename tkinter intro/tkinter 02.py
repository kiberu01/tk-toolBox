import tkinter

def Hello():
    print("Hello World")

if __name__=='__main__':
    window=tkinter.Tk()
    window.title("Tkinter First App")
    window.geometry('600x400')
    
    frame = tkinter.Frame(window)
    frame.pack()
    
    label=tkinter.Label(frame, text="Hello World")
    label.pack()
    button=tkinter.Button(frame, text='Hello World', command=Hello)
    button.pack()
    print(str(button))
    
    window.mainloop()
    
    print("Hi")