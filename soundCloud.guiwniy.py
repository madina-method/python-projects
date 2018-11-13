from tkinter import*
import requests, bs4, os
from selenium import webdriver


web = webdriver.Chrome("/Users/madina_tj/Downloads/chromedriver")
web.get("http://soundcloud.com")

def search():
    track_name = eName.get()
    track_name = "%20".join(track_name.split())
    url = track_url+track_name
    re = requests.get(url)
    soup = bs4.BeautifulSoup(re.text, "lxml")
    global artists
    artists = soup.select("a")
    artists = artists[7:len(artists)-7]
    
    web.get(url)
    wnGenre = Toplevel()
    wnGenre.geometry("500x600")
    wnGenre.title("Searching "+track_name)
    global canvas2
    canvas2 = Canvas(wnGenre, width=700, height=300)
    canvas2.pack(side=LEFT)

    scrollbar = Scrollbar(wnGenre, command=canvas2.yview)
    scrollbar.pack(side=LEFT, fill='y')

    canvas2.config(yscrollcommand = scrollbar.set)
    canvas2.bind('<Configure>', on_configure2)

    fr = Frame(canvas2)
    canvas2.create_window((0,0), window=fr, anchor='nw')

    for index, artist in enumerate(artists):
        global artist_links
        artist_links.append(artist.get("href"))
        l = Label(fr, text=artist.text)
        l.grid(column=0, row=index)

        b = Button(fr, text = "Listen", command=lambda i = index:searchArtist(i))
        b.grid(column = 1, row = index)
        
def searchArtist(index):
    url = "http://soundcloud.com"+artist_links[index]
    web.get(url)
    
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))   
def on_configure2(event):
    canvas2.configure(scrollregion=canvas2.bbox('all'))

    
def searchG(index):
    print(index)
    wnGenre = Toplevel()
    wnGenre.geometry("600x600")
    wnGenre.title("Songs by "+ str(genres[index].text)+" genre")
    global canvas
    canvas = Canvas(wnGenre, bg="light blue", width=800, height=700)
    canvas.pack(side=LEFT)

    scrollbar = Scrollbar(wnGenre, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill='y')

    canvas.config(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', on_configure)

    fr = Frame(canvas)
    canvas.create_window((0,0), window=fr, anchor='nw')
    
    url = "https://soundcloud.com"+genre_links[index]
    web.get(url)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    global tracks
    tracks = soup.select("h2")[3:]

    for index, track in enumerate(tracks):

        l = Label(fr, text=track.text)
        l.grid(column=0, row=index)

        b = Button(fr, text = "Listen", command=lambda i = index:searchTrack(i))
        b.grid(column = 1, row = index)
        
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
    labEmpty= Label(wnGenre, text = "", font=("Arial", 20))
    labEmpty.pack()
    global labNow
    labNow = Label(wnGenre, text="Choose a track")
    labNow.pack()

def searchTrack(index):
    print(index)
    track_url = track_links[index]
    web.get("http://soundcloud.com"+track_url)
    labNow.config(text="Now playing "+str(tracks[index].text)+". . .", fg="green")

genre_links = []
track_links = []
artist_links = []
track_names = []
tracks = []
"""
на случай, если сайт не будет работать
genres = ["Alternative Rock", "Ambient", "Classical", "Country", "Dance & EDM", "Dancehall", "Deep House",
          "Disco", "Drum & Bass", "Dubstep", "Electronic", "Folk & Singer-Songwriter", "Hip-hop & Rap",
          "House", "Indie", "Jazz & Blues", "Latin", "Metal", "Piano", "Pop", "R&B & Soul",
          "Reggae", "Reggaeton", "Rock", "Soundtrack", "Techno", "Trance", "Trap", "Triphop", "World"]
"""
track_url = "https://soundcloud.com/search/sounds?q="

# Getting genres

r = requests.get("https://soundcloud.com/charts/top?genre=alternativerock&country=US")
soup = bs4.BeautifulSoup(r.text, "lxml")
genres = soup.select("a[href*=genre]")[2:]


wn = Tk()
wn.geometry("700x600")
wn.title("Soundcloud")

labTitle = Label(wn, text = "Search for song or artist", font=("Arial", 20))
labTitle.pack()
labEmpty= Label(wn, text = "", font=("Arial", 20))
labEmpty.pack()

fr = Frame(wn)
fr.pack()

labName = Label(fr, text="Name")
labName.grid(column=0, row=0)

eName = Entry(fr)
eName.grid(column=1, row=0)

bSearch = Button(fr, text="Search", command=search)
bSearch.grid(column=2, row=0)

labEmpty= Label(wn, text = "", font=("Arial", 20))
labEmpty.pack()

labTitle2 = Label(wn, text = "Search by genre", font=("Arial", 20))
labTitle2.pack()

labEmpty= Label(wn, text = "", font=("Arial", 20))
labEmpty.pack()

frGenre = Frame(wn)
frGenre.pack()

col = 0
row = 0

for index, genre in enumerate(genres):
    button = Button(frGenre, text=genre.text, command=lambda i = index:searchG(i))
    button.grid(column=col, row=row)
    genre_links.append(genre.get("href"))
    col+=1
    if col == 5:
        row+=1
        col = 0

wn.mainloop()

