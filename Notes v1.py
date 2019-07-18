from tkinter import *
from tkinter import ttk

root = Tk()

# editable text area
textBox = Text(root)
textBox.grid(column=0, row=0, sticky=(N,W,E,S))

# vertical scroll bar
vertScroll = ttk.Scrollbar(root, orient=VERTICAL, command=textBox.yview)
vertScroll.grid(column=1, row=0, sticky=(N,S))
textBox['yscrollcommand'] = vertScroll.set
# horizantal scroll bar
horzScroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=textBox.xview)
horzScroll.grid(column=0, row=1, sticky=(W,E))
textBox['xscrollcommand'] = horzScroll.set

# resizing grip
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# menu setup
root.option_add('*tearOff', FALSE)  # disables 'tear-off' menus
menubar = Menu(root)

# file menu
filemenu = Menu(menubar)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Page Setup")
filemenu.add_command(label="Print")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# edit menu
editMenu = Menu(menubar)
editMenu.add_command(label="Undo")
editMenu.add_separator()
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Delete")
editMenu.add_separator()
editMenu.add_command(label="Find")
editMenu.add_command(label="Find Next")
editMenu.add_command(label="Replace")
editMenu.add_command(label="Go To")
editMenu.add_separator()
editMenu.add_command(label="Select All")
editMenu.add_command(label="Time/Date")
menubar.add_cascade(label="Edit", menu=editMenu)

# format menu
formatMenu = Menu(menubar)
formatMenu.add_command(label="Word Wrap")
formatMenu.add_command(label="Font")
menubar.add_cascade(label="Format", menu=formatMenu)

# view menu
viewMenu = Menu(menubar)
viewMenu.add_command(label="Status Bar")
menubar.add_cascade(label="View", menu=viewMenu)

# help menu
helpMenu = Menu(menubar)
helpMenu.add_command(label="View Help")
helpMenu.add_separator()
helpMenu.add_command(label="About this program")
menubar.add_cascade(label="Help", menu=helpMenu)

# display the menu
root.config(menu=menubar)

# run!
root.mainloop()