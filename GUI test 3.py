import tkinter as tk
from tkinter import ttk
import os

def get_txt_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.txt')]

def on_option_selected(event):
    selected_option = combo.get()
    if selected_option:
        with open(os.path.join(folder_path, selected_option), 'r') as file:
            pr = file.read()
        print(pr)  # or do something else with the contents

# Specify the folder containing the text files
folder_path = 'C:\\Users\\bucky\Documents\designMedia\pptxMaker\songs'

# Get a list of all text files in the folder
options = get_txt_files(folder_path)

# Create the main application window
root = tk.Tk()
root.title("Dropdown Example")

# Create a dropdown menu
combo = ttk.Combobox(root, values=options)
combo.set("Select a file")
combo.pack(pady=20)

# Bind the function to the dropdown menu selection event
combo.bind("<<ComboboxSelected>>", on_option_selected)

# Start the main event loop
root.mainloop()
