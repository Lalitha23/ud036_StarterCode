import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "November 22, 1995",
                        "8.3/10 IMDb ratings",
                        "http://www.imdb.com/title/tt0114709")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "December 18, 2009",
                     "7.3/10 IMDb ratings",
                     "http://www.imdb.com/title/tt0499549")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "October 3, 2003",
                             "7.1/10 IMDb ratings",
                             "http://www.imdb.com/title/tt0332379")

ratatouille = media.Movie("Ratatouille", "Story of rat who aspires to become a cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "June 29, 2007",
                          "8/10 IMDb ratings",
                          "http://www.imdb.com/title/tt0382932")

midnight_in_paris = media.Movie("Midnight in Paris", "A story of a nostalgic writer who goes back to 1920 every midnight in paris",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "May 20, 2011",
                                "7.7/10 IMDb ratings",
                                "http://www.imdb.com/title/tt1605783")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo",
                           "March 12, 2012",
                           "7.3/10 IMDb ratings",
                           "http://www.imdb.com/title/tt1392170/")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
