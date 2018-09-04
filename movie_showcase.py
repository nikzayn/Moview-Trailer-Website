#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Contains the inforamtion related to movies and desplay them on the website"""

import project
import fresh_tomatoes

 # Creates the objects which initailsing the Movie instances.

dark_knight = project.Movie('The Dark Knight',
                            'Batman to save Gotham city from Joker',
                            'https://prod1.agileticketing.net/images/user/ct_12655/Dark%20Knight.jpg'
                            ,
                            'https://www.youtube.com/watch?v=kmJLuwP3MbY'
                            , 'Rating: 9/10')

love_simon = project.Movie('Love Simon',
                           'A normal teenage and not so openly gay in school'
                           ,
                           'https://upload.wikimedia.org/wikipedia/en/b/bc/Love%2C_Simon_poster.png'
                           ,
                           'https://www.youtube.com/watch?v=ykHeGtN4m94'
                           , 'Rating: 7.9/10')

inception = project.Movie('Inception',
                          'The young girl who is the architect of the dreams.'
                          ,
                          'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg'
                          ,
                          'https://www.youtube.com/watch?v=d3A3-zSOBT4'
                          , 'Rating: 8.8/10')

interstellar = project.Movie('Interstellar',
                             'For the search of new sustainable life in the heart of interstellar.'
                             ,
                             'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg'
                             ,
                             'https://www.youtube.com/watch?v=zSWdZVtXT7E'
                             , 'Rating: 8.6/10')

forrest_gump = project.Movie('Forrest Gump',
                             'Forrest Gump, a man with a low I.Q., joins the army for service'
                             ,
                             'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg'
                             ,
                             'https://www.youtube.com/watch?v=SgduyXzxwS8'
                             , 'Rating: 8.8/10')

fight_club = project.Movie('Fight Club',
                           'An insomniac with his mind problems',
                           'https://image.tmdb.org/t/p/w300_and_h450_bestv2/adw6Lq9FiC9zjYEpOqfq03ituwp.jpg'
                           ,
                           'https://www.youtube.com/watch?v=JOFgLVjchHU'
                           , 'Rating: 8.8/10')

    # Store the Movie objects in a list.

movies = [
    dark_knight,
    love_simon,
    inception,
    interstellar,
    forrest_gump,
    fight_club,
    ]

    # Opens the movie website in the user's browsers.

fresh_tomatoes.open_movies_page(movies)
