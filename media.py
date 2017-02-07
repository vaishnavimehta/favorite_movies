import webbrowser


class Movie():
    # This class contains 2 methods
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # This method sets the values of the variables title,
        # storyline, poster_image_url and trailer_youtube_url
        # which define our class Movie.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # This method uses a function of webbrowser to open the link of the
        # trailer provided as an arguement.
        webbrowser.open(self.trailer_youtube_url)
