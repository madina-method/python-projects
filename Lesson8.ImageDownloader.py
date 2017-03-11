from tkinter import*
import requests, bs4, os

os.makedirs("images", exist_ok = True)

def d():
    link = en.get()
    try:
        data= requests.get(link) #important startswith http/https
        code = bs4.BeautifulSoup(data.text, "html.parser")
        images = code.select("img")
        for image in images:
            src = image.get("src")
            pos = src.rfind("/") + 1
            filename = src[pos:]
            status.config(text="Downloading "+filename+"....", fg="green")
            wn.update()
            data2 = requests.get(src)
            file = open("images/"+filename, "wb")
            file.write(data2.content)
            file.close()
        status.config(text="Finished", fg="blue")
    except:
        status.config(text="Connection or link error", fg="red")

wn = Tk()
wn.title("Image Downloader")
wn.geometry("450x200")

fr = Frame(wn)
fr.pack()

label = Label(fr, text="Link: ")
label.grid(row=0, column=0)

en = Entry(fr)
en.grid(row=0, column=1)

b = Button(fr, text="Download", command=d)
b.grid(row=0, column=2)

status = Label(text="0 % downloaded")
status.pack()
