import webbrowser

class Movie():
    """this is the class documentation docstring, the class objects are:
    movies (i.e: Inside Man,Deja Vu,Phiadelphia etc.)"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """this is the constructor method docstring initializing
        different functions of the class Movie that output information
        such as movie title,storyline,poster image and trailer """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
       webbrowser.open(self.trailer_youtube_url)
       """this function allows for the webpage of
       the movie trailer to be opened """
