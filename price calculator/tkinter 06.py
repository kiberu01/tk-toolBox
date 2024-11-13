import tkinter

def computePrice():
    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
    totalprice_entry.insert(0, string=str(totalprice))
    
    
window=tkinter.Tk()

frame=tkinter.Frame(window)

priceperitem_label=tkinter.Label(frame, text="Price per item")
priceperitem_entry=tkinter.Entry(frame)
numberofitems_label=tkinter.Label(frame, text="Number of items")
numberofitems_entry=tkinter.Entry(frame)
totalprice_label=tkinter.Label(frame, text="Total price:")
totalprice_entry=tkinter.Entry(frame)
calculate_button=tkinter.Button(frame, text="Calculate total", command=computePrice)

priceperitem_label.grid(row=0, column=0)
priceperitem_entry.grid(row=0, column=1)
numberofitems_label.grid(row=1, column=0)
numberofitems_entry.grid(row=1, column=1)
totalprice_label.grid(row=2, column=0)
totalprice_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)

frame.pack()

# rows=4
# columns=2
# for i in range(rows):
#     window.grid_rowconfigure(i, weight=1)
# for i in range(columns):
#     window.grid_columnconfigure(i, weight=1)


window.mainloop()