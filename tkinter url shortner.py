import tkinter
import pyshortners

def shorten():
    shortener = pyshortners.Shortener()
    short_url = shortener.tinyurl.short(long_url_entry.get())
    print(output_url_entry.insert(0, short_url))

window=tkinter.Tk()
window.title('URL Shortener')
window.geometry('600x400')

long_url_label = tkinter.Label(window, text="Enter Long URL")
long_url_entry = tkinter.Entry(window)
output_label = tkinter.Label(window, text="Output shortened URL")
output_url_entry = tkinter.Entry(window)
shorten_button = tkinter.Button(window, text="Shorten URL", command=shorten)

long_url_label.pack()
long_url_entry.pack()
output_label.pack()
output_url_entry.pack()
shorten_button.pack()



window.mainloop()