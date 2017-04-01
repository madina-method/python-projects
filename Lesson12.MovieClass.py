import generator

class Movie:
    def __init__(self, title, genre, year, poster_url, trailer_url):
        self.title = title
        self.genre = genre
        self.year = year
        self.poster_url = poster_url
        self.trailer_url = trailer_url
        

m1 = Movie("Deadpool", "Action, Comedy", 2016, "http://www.terzapagina.it/wp-content/uploads/2016/02/DEADPOOL_OOH_70X100_CmpJ-02.jpg", "https://www.youtube.com/watch?v=Xithigfg7dA")
m2 = Movie("Logan", "Action", 2017, "http://www.terzapagina.it/wp-content/uploads/2016/02/DEADPOOL_OOH_70X100_CmpJ-02.jpg", "https://www.youtube.com/watch?v=Div0iP65aZo")
m3 = Movie("The Boss Baby", "Cartoon, Comedy", 2017, "http://www.terzapagina.it/wp-content/uploads/2016/02/DEADPOOL_OOH_70X100_CmpJ-02.jpg", "https://www.youtube.com/watch?v=25TI_Uv2mmw")

generator.open_movies_page([m1, m2, m3])
