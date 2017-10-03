from tkinter import*
import requests

# API выглядит как link1+название_города+link2
link1 = "http://api.openweathermap.org/data/2.5/weather?q="
link2 = "&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d"


def getW():
    city = en.get() # берем название с ентри
    link = link1+city+link2 # лепим новую рабочую ссылку
    data = requests.get(link) # делаем на нее запрос
    temp = data.json()['main']['temp'] # вытаскиваем температуру
    country = data.json()['sys']['country'] # вытаскиваем страну
    pogoda = data.json()['weather'][0]['main'] # вытаскиваем саму погоду

    #if elif для картинок canvas.create_image() взависимости от переменной pogoda
    #if else для пустоты, если человек ничего не напишет, выдать ошибку

    
    # рисуем спарсенные данные на канвасе
    canvas.create_text(210, 30, text="Temp= "+str(temp)+"°C", font="Arial 25")
    canvas.create_text(250, 60, text=pogoda, font="Arial 25")
    canvas.create_text(250, 90, text=country, font="Arial 25")

wn = Tk()
wn.title("Canvas")
wn.geometry("300x200")

fr = Frame()
fr.pack()

lab = Label(fr, text="City: ")
lab.grid(row=0, column=0)

en = Entry(fr)
en.grid(row=0, column=1)

b = Button(fr, text="Get", command=getW)
b.grid(row=0, column=2)

canvas = Canvas(width=300, height=200, bg="yellow")
canvas.pack()

#img = PhotoImage(file="batman.gif")
#canvas.create_image(100, 100, image=img)
