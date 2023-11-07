from abc import ABC, abstractmethod

class MovieTheater(ABC):
    def __init__(self, location, seating_capacity):
        self.location = location
        self.seating_capacity = seating_capacity
        self.showtimes = []

    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def browse_movies(self):
        movies = set()
        for showtime in self.showtimes:
            movies.add(showtime.movie.title)
        return movies

    def browse_showtimes(self, movie_title):
        showtimes = []
        for showtime in self.showtimes:
            if showtime.movie.title == movie_title:
                showtimes.append(showtime)
        return showtimes

    @abstractmethod
    def reserve_seats(self, showtime, num_seats):
        pass
