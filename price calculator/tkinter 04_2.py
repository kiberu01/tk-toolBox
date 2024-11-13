import tkinter

def computePrice():
    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
    totalprice_entry.insert(0, string=str(totalprice))
    
    
window=tkinter.Tk()
window.geometry('300x250')

priceperitem_label=tkinter.Label(window, text="Price per item")
priceperitem_entry=tkinter.Entry(window)
numberofitems_label=tkinter.Label(window, text="Number of items")
numberofitems_entry=tkinter.Entry(window)
totalprice_label=tkinter.Label(window, text="Total price:")
totalprice_entry=tkinter.Entry(window)
calculate_button=tkinter.Button(window, text="Calculate total", command=computePrice)

# priceperitem_label.place(x=0, y=0)
# priceperitem_entry.place(x=0, y=50)

widgets = [priceperitem_label, priceperitem_entry, numberofitems_label, numberofitems_entry, 
            totalprice_label, totalprice_entry, calculate_button]

for i in range(len(widgets)):
    widgets[i].place(x=0, y=i*20)


window.mainloop()