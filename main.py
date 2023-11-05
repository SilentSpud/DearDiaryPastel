import os
from sys import exit
import tkinter as tk
from tkinter import messagebox
from src import dependencies

# Check if jpexs/ffdec.jar exists
if not os.path.exists("jpexs/ffdec.jar"):
    # Prompt user to install
    response = messagebox.askyesno("Install JPEXS?", "JPEXS Free Flash Decompiler is required for this app. Would you like to install it now?")
    if response == tk.YES:
        # Run setup_jpexs function
        dependencies.setup_jpexs()
    else:
        # Tell user it's required and close app
        messagebox.showerror("Error", "JPEXS is required. Closing app.")
        exit(-1)

# Create GUI
root = tk.Tk()
root.title("Skyrim SWF Patcher")

# Set dark mode theme
root.tk_setPalette(background='#1E1E1E', foreground='white', activeBackground='#3F3F3F', activeForeground='white')

# Create buttons
patch_swf_button = tk.Button(root, text="Patch SWF")
scour_all_button = tk.Button(root, text="Scour All")
svgo_all_button = tk.Button(root, text="SVGO All")
reinstall_jpexs_button = tk.Button(root, text="Reinstall JPEXS")

# Pack buttons
patch_swf_button.pack()
scour_all_button.pack()
svgo_all_button.pack()
reinstall_jpexs_button.pack()

# Run GUI
root.mainloop()
