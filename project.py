#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Defines the Movie class that contains
the information of movies list"""

import webbrowser


class Movie:

    """This class Movie is way to store the
           related information of movies"""

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        ratings_rank,
        ):
        """Initialises class Movie via using instance variables"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = ratings_rank

    def show_trailer(self):
        """Plays the movie trailer related to that particular movie"""

        webbrowser.open(self.trailer_youtube_url)
