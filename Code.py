
# ----------------------------------------------------------------------------

from tkinter import Tk,Menu,Text,Button
from tkinter import filedialog,Canvas,Label,Entry
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# including the menu bar item workings..---------------------------------------
def NewFile():
    global file
    root.title("Untitled - Notepad")
    file= None
    text.delete(1.0, END)
    
def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def SaveAs():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut_text():
    copy_text()
    text.delete("sel.first","sel.last")

def paste_text():
    text.insert('insert',text.clipboard_get())

def undo_text():
    text.edit_undo()

def redo_text():
    text.edit_redo()

def about_page():
        showinfo("WritePad","WritePad - By Akshat Srivastava")           
        
    
# Entering the Window -----------------------------------------------------------
root = Tk()
root.title("Writepad")
root.geometry("1000x625")

# Entering the Menu bar --------------------------------------------------------
menu_bar=Menu(root)
# Entering File menu -----------------------------------------------------------
fileMenu = Menu(menu_bar,tearoff=0)
fileMenu.add_command(label="Open",command=OpenFile)
fileMenu.add_command(label="New",command=NewFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=SaveAs)
fileMenu.add_command(label="Save As")
fileMenu.add_separator()
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.destroy)
menu_bar.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu_bar)
# Entering Edit menu -----------------------------------------------------------
editMenu = Menu(menu_bar,tearoff=0)
editMenu.add_command(label="Undo",command=undo_text)
editMenu.add_command(label="Redo",command=redo_text)
editMenu.add_separator()
editMenu.add_command(label="Cut",command=cut_text)
editMenu.add_command(label="Copy",command=copy_text)
editMenu.add_command(label="Paste",command=paste_text)
menu_bar.add_cascade(label="Edit",menu=editMenu)
root.config(menu=menu_bar)

# Entering Help menu ------------------------------------------------------------
helpMenu = Menu(menu_bar,tearoff=0)
helpMenu.add_command(label="About Writepad",command=about_page)
menu_bar.add_cascade(label="Help",menu=helpMenu)
root.config(menu=menu_bar)

# Entering the text -------------------------------------------------------------
text= Text(root,bd=4,wrap='word',undo=True,font="Times,60,bold")
file= None
text.pack(expand=True,fill=BOTH)

# Entering the Scroll Bar ------------------------------------------------------------

Scroll = Scrollbar(text)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=text.yview)
text.config(yscrollcommand=Scroll.set)


root.mainloop()
