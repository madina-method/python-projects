from tkinter import*


def popup(event):
    pmenu.tk_popup(event.x_root, event.y_root)


def app():
    messagebox.showinfo("About the app", "Version 1.0\nMade in Kz")

def author():
    messagebox.showinfo("About the author", "Madina Torgayeva")

def close():
    if messagebox.askyesno("Exit", "Do u really want to exit?"):
        wn.destroy()

def newfile(event=None):
    wn.title("Untitled.txt")
    pole.delete(1.0, END)

def openfile(event=None):
    filename = filedialog.askopenfilename()
    pos = filename.rfind("/") + 1
    newName = filename[pos:]
    
    file = open(filename, "r")
    content = file.read()
    pole.insert(1.0, content)
    file.close()
    wn.title(newName)
def savefile(event=None):
    filename = filedialog.asksaveasfilename()
    file = open(filename+".txt", "w")
    content = pole.get(1.0, END)
    file.write(content)
    file.close()

def cut():
    pole.event_generate("<<Cut>>")
def copy():
    pole.event_generate("<<Copy>>")
def paste():
    pole.event_generate("<<Paste>>")
def undo():
    pole.event_generate("<<Undo>>")
def redo():
    pole.event_generate("<<Redo>>")
wn = Tk()
wn.geometry("400x400")
wn.title("Notepad")

menubar = Menu()
wn.config(menu=menubar)

fmenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fmenu)

fmenu.add_command(label="New File", accelerator="Ctrl+N", command=newfile)
fmenu.add_command(label="Open", accelerator="Ctrl+O", command=openfile)
fmenu.add_command(label="Save", accelerator="Ctrl+S", command=savefile)
fmenu.add_command(label="Close", accelerator="Ctrl+W")

aboutmenu = Menu(menubar)
menubar.add_cascade(label="About", menu=aboutmenu)

aboutmenu.add_command(label="About the app", command=app)
aboutmenu.add_command(label="About author", command=author)

nfi = PhotoImage(file="icons/newfile.gif")
ofi = PhotoImage(file="icons/openfile.gif")
sfi = PhotoImage(file="icons/save.gif")
ui = PhotoImage(file="icons/undo.gif")

panel = Frame(wn)
panel.pack()

nfb = Button(panel, image=nfi, command=newfile)
nfb.grid(row=0, column=0)

ofb = Button(panel, image=ofi)
ofb.grid(row=0, column=1)
sfb = Button(panel, image=sfi)
sfb.grid(row=0, column=2)
ub = Button(panel, image=ui, command=undo)
ub.grid(row=0, column=3)

pole = Text(wn, undo=True)
pole.pack()

pmenu = Menu(pole)
pmenu.add_command(label="Cut", command=cut)
pmenu.add_command(label="Copy", command=paste)
pmenu.add_command(label="Paste", command=paste)

pole.bind("<Button-2>", popup)
wn.protocol("WM_DELETE_WINDOW", close)
pole.bind("<Control-n>", newfile)
pole.bind("<Control-o>", newfile)
pole.bind("<Control-s>", newfile)
















