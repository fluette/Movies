import media
import fresh_tomatoes
#movie classes:{title,storyline,poster image}
#movies = [Deja Vu,Inside Man, Training Day,
#American Gangster, Philadelphia, Man on Fire]
#external rendering function: fresh_tomatoes.open_movies_page(movies)

deja_vu = media.Movie("Deja Vu",
          "ATF Agent travels back in time to prevent terrorist attack",
          "https://upload.wikimedia.org/wikipedia/en/c/cf/DejaVuBigPoster.jpg", #noqa
          "https://www.youtube.com/watch?v=uxdS8TP37I4")

inside_man = media.Movie("Inside Man",
          "The investigation of a hostage situation in a bank",
          "https://upload.wikimedia.org/wikipedia/en/a/a2/Inside_Man_%28film_poster%29.jpg",#noqa
          "https://www.youtube.com/watch?v=3WRxsmqercg")

training_day = media.Movie("Training Day",
          "The 24-hour training of a rookie Los Angeles policeman",
          "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",#noqa
          "https://www.youtube.com/watch?v=gKTVQPOH8ZA")

american_gangster = media.Movie("American Gangster",
          "A chauffeur turned into Harlem's most powerful crime bosses",
          "https://upload.wikimedia.org/wikipedia/en/9/9f/American_Gangster_poster.jpg",#noqa
          "https://www.youtube.com/watch?v=BV_nssS6Zkg")

philadelphia = media.Movie("Philadelphia",
          "The lawsuit of a man with AIDS fired because of his conidtion",
          "https://upload.wikimedia.org/wikipedia/en/0/00/Philadelphia_imp.jpg",#noqa
          "https://www.youtube.com/watch?v=cl4B9AU45P4")

man_on_fire = media.Movie("Man on Fire",
          "A former  assassin avenges the family he was hired to protect",
          "https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg",#noqa
          "https://www.youtube.com/watch?v=g4kLizDXLY0")


movies = [deja_vu, inside_man, training_day,
american_gangster, philadelphia, man_on_fire]
fresh_tomatoes.open_movies_page(movies)
