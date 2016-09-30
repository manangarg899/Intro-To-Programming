import webbrowser
#In this project,we will define a class Movie so as to create instance for each movie at current iteration
class Movie():    
#init is a method used to initialize an object for the aspects of current movies
#underscore before and after init defines that it is a predefined variable.
#like movie_title, movie_storyline, poster_image, trailer_youtube, run_time.These variables are acting as instance variables in this class
#to access the given  values 
#self is a value which initializes itself at runtime and later used as object to create different instances for each movie
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,run_time):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.run_time=run_time
#run_time is used to access running time of the movie
#defination show trailer is defined to access trailer of the movie in a webbrowser
#here value of self will be the value of current accessed movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
        
