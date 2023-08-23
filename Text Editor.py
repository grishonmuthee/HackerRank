from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import font, Menu

root = Tk()
root.geometry ("400x400")
root.title("Grishon Text Editor")
root.minsize(height=560)

#Text widget
text = Text(root)
text.pack(fill= BOTH, expand = True)

# scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT, fill = Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand = scrollbar.set)

def save():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text.get("1.0", "end-1c")  # Get all text from the Text widget
        output_file.write(text)
    root.title(f"Entitled - {filepath}")

def toggle_bold():
    current_tags = text.tag_names(tk.SEL_FIRST)

    if "bold" in current_tags:
        text.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST)
    else:
        text.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST)

    
#Menu
menubar = Menu(root)
root.config(menu = menubar)

#File Menu
file_menu = Menu(menubar, tearoff = 0)
file_menu.add_command(label = "New")
file_menu.add_command(label = "Open")
file_menu.add_command(label = "Save", command = save)
file_menu.add_command(label = "Save as..")
file_menu.add_command(label = "Close")

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')
file_menu.add_cascade(label="Preferences", menu=sub_menu)

file_menu.add_separator()
file_menu.add_command(label = "Exit", command =  root.quit)


menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu (menubar, tearoff = 0)
edit_menu.add_command (label = "Undo")
edit_menu.add_command (label = "Copy")
edit_menu.add_command (label = "Cut")
edit_menu.add_command (label = "Find")
edit_menu.add_command(label = "Replace")

menubar.add_cascade(label = "Edit", menu = edit_menu)


Boldbutton = Button (root, text = "Bold", command = toggle_bold)
Boldbutton.place(x = 250, y = 350)
bold_font = font.Font(text, text.cget("font"))
bold_font.configure(weight = "bold")
text.tag_configure("bold", font = bold_font)



root.mainloop()



