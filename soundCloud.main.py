from selenium import webdriver
import requests, bs4, os
import webbrowser as web

#new, top, mix, track, artists urls

top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search?q="
artist_url = "http://soundcloud.com/charts/people?q="
mix_url_end = "&filter.duration=epic"


#create the selenium browser

web = webdriver.Chrome("/Users/madina_tj/Downloads/chromedriver")
web.get("http://soundcloud.com")


#web.open("http://soundcloud.com")


while True:
    print("\tMenu:")
    print("\t1. Search for a track")
    print("\t2. Search for an artist")
    print("\t3. Search for a mix")
    print("\t4. Top charts")
    print("\t5. New & hot charts")
    print("\t0. Exit\n")

    choice = int(input("Your choice: \n"))


    if choice == 0:
        print("Bye!")
        break
    if choice == 1:
        track_name = input("\nName of the track: ")
        "%20".join(track_name.split())
        web.get(track_url+track_name)
    if choice == 4:
        r = requests.get(top_url)
        soup = bs4.BeautifulSoup(r.text, "lxml")
        genres = soup.select("a[href*=genre]")[2:]
        genre_links = []
        for index, genre in enumerate(genres):
            print(index, ":", genre.text)
            genre_links.append(genre.get("href"))

        genre_choice = int(input("\nChoose genre number: "))
        url = "http://soundcloud.com"+genre_links[genre_choice]
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, "lxml")

        tracks = soup.select("h2")[3:]

        track_links = []
        track_names = []
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(index, ":", track.text, "\n")

        track_choice = int(input("\nChoose track number: "))
        url = "http://soundcloud.com"+track_links[track_choice]
        web.get(url)
        print("\n\tNOW PLAYING", track_names[track_choice], "...\n")
        a = input("Next step: ")
            
        
        






    
