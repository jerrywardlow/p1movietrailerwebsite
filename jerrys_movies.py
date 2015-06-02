"""This file stores data about movies and generates a webpage."""

# The media and fresh_tomatoes files are imported so their methods
# can be used.
import media
import fresh_tomatoes

# Each object stores the Title, Storyline, Poster Image, and YouTube Trailer
# link for a specific movie.
falling_down = media.Movie("Falling Down",
                           "An unemployed defense worker"
                           " frustrated with the various flaws"
                           " he sees in society, begins to psychotically"
                           " and violently lash out against them.",
                           "http://upload.wikimedia.org/wikipedia/en/"
                           "2/22/Falling_Down_%281993_film%29_poster.jpg",
                           "https://www.youtube.com/watch?v=KOUdakrP52E")

gone_in_60_seconds = media.Movie("Gone in 60 Seconds",
                                 "A retired master car thief must"
                                 " come back to the industry and steal"
                                 " 50 cars with his crew in one night"
                                 " to save his brother's life.",
                                 "http://upload.wikimedia.org/wikipedia/en/"
                                 "2/2a/Gone_in_sixty_seconds.jpg",
                                 "https://www.youtube.com/watch?v=o6AyAM1buQ8")

star_trek_nemesis = media.Movie("Star Trek: Nemesis",
                                "The Enterprise is diverted to the Romulan"
                                " homeworld Romulus, supposedly because"
                                " they want to negotiate a peace treaty.",
                                "http://upload.wikimedia.org/wikipedia/en/"
                                "9/9c/Star_Trek_Nemesis_poster.jpg",
                                "https://www.youtube.com/watch?v=FckGQzqXgpE")

my_neighbor_totoro = media.Movie("My Neighbor Totoro",
                                 "When two girls move to the country to be"
                                 " near their ailing mother, they have"
                                 " adventures with the wonderous forest"
                                 " spirits who live nearby.",
                                 "http://upload.wikimedia.org/wikipedia/en/"
                                 "0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro"
                                 "_%28Movie_Poster%29.jpg",
                                 "https://www.youtube.com/watch?v=TuLX50_5UAI")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker looking for a way to"
                         " change his life crosses paths with a"
                         " devil-may-care soap maker and they form"
                         " an underground fight club that evolves into"
                         " something much, much more...",
                         "http://upload.wikimedia.org/wikipedia/en/"
                         "f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

back_to_the_future = media.Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years"
                                 " into the past in a time-traveling DeLorean"
                                 " invented by his friend, Dr. Emmett Brown,"
                                 " and must make sure his high-school-age"
                                 " parents unite in order to save"
                                 " his own existence.",
                                 "http://upload.wikimedia.org/wikipedia/en/"
                                 "d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")


# A list containing each movie object is created.
movies = [falling_down, gone_in_60_seconds, star_trek_nemesis,
          my_neighbor_totoro, fight_club, back_to_the_future]

# The HTML is generated using the list of movies and the method from
# the fresh_tomatoes file.
fresh_tomatoes.open_movies_page(movies)
