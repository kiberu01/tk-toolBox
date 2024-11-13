import tkinter


root = tkinter.Tk()

# creating the text
text = tkinter.Text(root, width=80, height=15)
text.pack()

def getText():
    print(text.get("1.0","end"))
    
get_button = tkinter.Button(root, text="Get Text", command=getText)
get_button.pack()

def insertText():
    text.insert("1.0", "just inserted text")

insert_button = tkinter.Button(root, text="Insert text", command=insertText)
insert_button.pack()

def deleteText():
    text.delete("2.0", "end")

delete_button = tkinter.Button(root, text="Delete text", command=deleteText)
delete_button.pack()

root.mainloop()