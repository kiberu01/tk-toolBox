import tkinter as tk
import random

def impress_crush():
    pickup_lines = [
        "Do you have a map? I keep getting lost in your eyes.",
        "Is your name Google? Because you have everything I've been searching for.",
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Excuse me, but I think you dropped something: my jaw.",
        "Is your dad a baker? Because you're a cutie pie!",
        "Do you believe in love at first sight, or should I walk by again?",
        "If you were a vegetable, you'd be a cute-cumber.",
        "I deleted google when I found you, because I knew that the search is done",
        "Do you have a Band-Aid? I just scraped my knee falling for you.",
        "Are you a camera? Because every time I look at you, I smile.",
        "Is your name Wi-Fi? Because I'm really feeling a connection."
    ]
    
    pickup_line = random.choice(pickup_lines)
    label.config(text=pickup_line)

# Create the main window
window = tk.Tk()
window.title("Impress Her")
window.geometry("400x300")

# Create a label to display the pickup lines
label = tk.Label(window, text="Click the button, it has something for you...")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Click ME", command=impress_crush)
button.pack()

label2 = tk.Label(window, text="The messages are many and random")
label3 = tk.Label(window, text="So, just continue clicking")
label4 = tk.Label(window, text="Hope it brings a smile on your face")

label2.pack()
label3.pack()
label4.pack()

# Start the main event loop
window.mainloop()