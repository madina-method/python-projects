from tkinter import*
import football2

def done():
    global teamName1, teamName2
    teamName1 = en_name1.get()
    teamName2 = en_name2.get()
    size1 = lb_team1.size()
    size2 = lb_team2.size()
    print(size1, size2)
    if teamName1 == "" and teamName2=="":
        lab_error1.config(text="Empty", fg="red")
        lab_error2.config(text="Empty", fg="red")
    elif teamName1 == "":
        lab_error1.config(text="Empty", fg="red")
        lab_error2.config(text="Team name selected!", fg="green")
    elif teamName2 == "":
        lab_error1.config(text="Team name selected!", fg="green")
        lab_error2.config(text="Empty", fg="red")
    elif size1==1 and size2==1:
        lab_errorLen1.config(text="Players're not imported!", fg="red")
        lab_errorLen2.config(text="Players're not imported!", fg="red")
        lab_error1.config(text="Team name selected!", fg="green")
        lab_error2.config(text="Team name selected!", fg="green")
    elif size1==1:
        lab_errorLen1.config(text="Players're not imported!", fg="red")
        lab_errorLen2.config(text="Players're imported!", fg="green")
        lab_error1.config(text="Team name selected!", fg="green")
        lab_error2.config(text="Team name selected!", fg="green")
    elif size2==1:
        lab_errorLen2.config(text="Players're not imported!", fg="red")
        lab_errorLen1.config(text="Players're imported!", fg="green")
        lab_error1.config(text="Team name selected!", fg="green")
        lab_error2.config(text="Team name selected!", fg="green")
    else:
        wn1.destroy()
        football2.show(teamName1, teamlead1, filename1, logoName1, teamName2, teamlead2, filename2, logoName2)

def importPlayers1():
    global teamlead1, filename1
    filename1 = filedialog.askopenfilename()
    file = open(filename1, "r")
    teamlead1 = file.readline().strip()
    lb_teamlead1.config(text="Captian: "+teamlead1)
    line = "q"
    lb_team1.delete(0, END)
    while line!="":
        line = file.readline()
        lb_team1.insert(END, line)
    lab_errorLen1.config(text="Players're imported!", fg="green")

def importPlayers2():
    global teamlead2, filename2
    filename2 = filedialog.askopenfilename()
    file = open(filename2, "r")
    teamlead2 = file.readline().strip()
    lb_teamlead2.config(text="Captian: "+teamlead2)
    line = "q"
    lb_team2.delete(0, END)
    while line!="":
        line = file.readline()
        lb_team2.insert(END, line)
    lab_errorLen2.config(text="Players're imported!", fg="green")
    
def selectLogo1():
    global logoName1
    logoName1 = filedialog.askopenfilename()
    lab_logo1.config(text="Logo selected", fg="green") 
    
def selectLogo2():
    global logoName2
    logoName2 = filedialog.askopenfilename()
    lab_logo2.config(text="Logo selected", fg="green")
    
wn1 = Tk()
wn1.title("Add teams")
wn1.geometry("500x700")

lab_title = Label(text="Choose name and logos for future teams")
lab_title.pack()

lab_div = Label(text="")
lab_div.pack()

# common frame
fr = Frame()
fr.pack()

#first frame
fr_team1 = LabelFrame(fr, text="Team 1")
fr_team1.grid(row=0, column=0)

#second frame
fr_team2 = LabelFrame(fr, text="Team 2")
fr_team2.grid(row=0, column=2)

#filling 1 frame
lab_name1 = Label(fr_team1, text="Enter team name")
lab_name1.pack()
en_name1 = Entry(fr_team1)
en_name1.pack()
lab_error1 = Label(fr_team1, text="", fg="red")
lab_error1.pack()

lab_logo1 = Label(fr_team1, text="Logo is not selected", fg="red")

#select logo1
b_logo1 = Button(fr_team1, text="Select logo", command=selectLogo1)
b_logo1.pack()
lab_logo1.pack()

lb_team1 = Listbox(fr_team1, height=20)
lb_team1.insert(END, "Team members will be here")
lb_team1.pack()

#listbox 1
lb_teamlead1 = Label(fr_team1, text="Captian: ----------")
lb_teamlead1.pack()

b_team1 = Button(fr_team1, text="Import players", command=importPlayers1)
b_team1.pack()
lab_errorLen1 = Label(fr_team1, text="", fg="red")
lab_errorLen1.pack()

#divider
lab_divider = Label(fr, text=" VS ")
lab_divider.grid(row=0, column=1)

#filling 2 frame
lab_name2 = Label(fr_team2, text="Enter team name")
lab_name2.pack()
en_name2 = Entry(fr_team2)
en_name2.pack()
lab_error2 = Label(fr_team2, text="", fg="red")
lab_error2.pack()
lab_logo2 = Label(fr_team2, text="Logo is not selected", fg="red")

b_logo2 = Button(fr_team2, text="Select logo", command=selectLogo2)
b_logo2.pack()
lab_logo2.pack()


lb_team2 = Listbox(fr_team2, height=20)
lb_team2.insert(END, "Team members will be here")
lb_team2.pack()


lb_teamlead2 = Label(fr_team2, text="Captian: ---------")
lb_teamlead2.pack()

b_team2 = Button(fr_team2, text="Import players", command=importPlayers2)
b_team2.pack()

lab_errorLen2 = Label(fr_team2, text="", fg="red")
lab_errorLen2.pack()

#when done
b_done = Button(text="Done", command=done)
b_done.pack()
