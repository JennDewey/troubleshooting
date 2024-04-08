import tkinter as tk

# Create a new Tkinter window.
window = tk.Tk()

# Configure the window's grid to expand with the window size.
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

# Create a frame widget to hold the other widgets.
frame = tk.Frame(window)

# Set the frame widget's grid configuration to have 1 column and 6 rows.
frame.grid_columnconfigure(0, weight=1)
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

# Create 6 widgets and add them to the frame widget, one per row.
for i in range(6):
    widget = tk.Label(frame, text=f"Button")
    widget.grid(row=i, column=0, sticky=tk.N+tk.S)

# Pack the frame widget into the window.
frame.grid(sticky=tk.N+tk.S+tk.E+tk.W)

# Start the mainloop.
window.mainloop()