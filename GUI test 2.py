import tkinter as tk
from tkinter import ttk
from pptx_class import pptx

def on_option_selected(event):
    selected_option = combo.get()
    if selected_option == "Purple Rain":
        with open('purple_rain.txt', 'r') as file:
            pr = file.read()
        print(pr)
        prs = pptx()
        prs.add_title_slide("Purple Rain")
        prs.add_song_slide(pr)
        prs.save_presentation("test pr.pptx")

# Create the main application window
root = tk.Tk()
root.title("Dropdown Example")

# Create a dropdown menu
options = ["Purple Rain", "Another Option"]
combo = ttk.Combobox(root, values=options)
combo.set("Select an option")
combo.pack(pady=20)

# Bind the function to the dropdown menu selection event
combo.bind("<<ComboboxSelected>>", on_option_selected)

# Start the main event loop
root.mainloop()
