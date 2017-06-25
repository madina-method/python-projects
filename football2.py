from tkinter import*
import time

def show(teamName1, teamlead1, filename1, logoName1, teamName2, teamlead2, filename2, logoName2):
    global score1, score2
    score1 = 0
    score2 = 0
    file1 = open(filename1, "r")
    file2 = open(filename2, "r")
    def refreshScore():
        global score1, score2
        score1 = 0
        score2 = 0
        lab_score1.config(text=" 0 ")
        lab_score2.config(text=" 0 ")
    def addPoint1():
        global score1
        score1 +=1
        lab_score1.config(text=" "+str(score1)+" ")
    def addPoint2():
        global score2
        score2 +=1
        lab_score2.config(text=" "+str(score2)+" ")
        
    def timer():
        seconds = 0
        minutes = 0
        while True:
            strsec = str(seconds)
            strmin = str(minutes)
            if minutes == 1:
                messagebox.showinfo("Game is over", "Game has finished")
                if score1<score2:
                    winner = teamName2
                    lab_winner.config(text=winner+" is the champion!")
                elif score1>score2:
                    winner = teamName1
                    lab_winner.config(text=winner+" is the champion!")
                else:
                    lab_winner.config(text="Draw!")
                
                break
                
            if seconds==5:
                minutes+=1
                seconds = 0
            if len(str(seconds))==1:
                strsec = "0"+str(seconds)
            if len(str(minutes)) == 1:
                strmin = "0"+str(minutes)
            lab_time.config(text=" "+strmin+" : "+strsec+" ")
            time.sleep(1)
            seconds+=1
            wn2.update()
        
    wn2 = Tk()
    wn2.title("Football Board")
    wn2.geometry("700x700")
    
    # common frame
    fr = Frame(wn2)
    fr.pack()

    #score

    fr_score = Frame(fr)
    fr_score.grid(row=0, column=1)
    lab_score1 = Label(fr_score, text=" 0 ", font=("Arial", 40))
    lab_score1.grid(row=0, column=0)
    lab_score2 = Label(fr_score, text=" 0 ",  font=("Arial", 40))
    lab_score2.grid(row=0, column=2)
    lab_score = Label(fr_score, text=":",  font=("Arial", 40))
    lab_score.grid(row=0, column=1)

    b_zero = Button(fr, text="Refresh Score", command=refreshScore)
    b_zero.grid(row=1, column=1)

    #first frame
    fr_team1 = LabelFrame(fr, text=teamName1)
    fr_team1.grid(row=0, column=0)
    lb_teamlead1 = Label(fr_team1, text="Captian: "+teamlead1)
    lb_teamlead1.pack()

    b_plus1 = Button(fr_team1, text="+1", command=addPoint1)
    b_plus1.pack()
    line=file1.readline()
    lb_team1 = Listbox(fr_team1, height=20)
    lb_team1.pack()
    while line!="":
        line = file1.readline()
        lb_team1.insert(END, line)

    #second frame
    fr_team2 = LabelFrame(fr, text=teamName2)
    fr_team2.grid(row=0, column=2)
    lb_teamlead2 = Label(fr_team2, text="Captian: "+teamlead2)
    lb_teamlead2.pack()
    b_plus2 = Button(fr_team2, text="+1", command=addPoint2)
    b_plus2.pack()
    lb_team2 = Listbox(fr_team2, height=20)
    lb_team2.pack()
    line = file2.readline()
    while line!="":
        line = file2.readline()
        lb_team2.insert(END, line)

    #timer

    fr_timer = LabelFrame(wn2, text="Timer")
    fr_timer.pack()
    lab_time = Label(fr_timer, text=" 00 : 00 ", font=("Arial", 45))
    lab_time.pack()
    b_start = Button(fr_timer, text="Start", command=timer)
    b_start.pack()

    lab_winner = Label(wn2, text="")
    lab_winner.pack()

