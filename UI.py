import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My GUI")

# Add a label
label = tk.Label(window, text="Hello, World!")
label.pack()

# Add a button
button = tk.Button(window, text="Click me!", command=lambda: print("Button clicked!"))
button.pack()

# Start the event loop
window.mainloop()