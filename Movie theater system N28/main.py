from Movie import Movie
from Theacher import StandardTheater, IMAXTheater
from Showtime import Showtime

if __name__ == "__main__":
    movie1 = Movie("Movie 1", "Action", 120)
    movie2 = Movie("Movie 2", "Comedy", 90)

    standard_theater = StandardTheater("Theater 1", 1550)
    imax_theater = IMAXTheater("Theater 2", 775)

  
    showtime1 = Showtime(movie1, standard_theater, "2023-11-01 18:00", standard_theater.seating_capacity)
    showtime2 = Showtime(movie2, imax_theater, "2023-11-01 20:00", imax_theater.seating_capacity)

    standard_theater.add_showtime(showtime1)
    imax_theater.add_showtime(showtime2)

    available_movies = standard_theater.browse_movies()
    print("Available movies:")
    for movie in available_movies:
        print(movie)

    movie_title = "Movie 1"
    showtimes = standard_theater.browse_showtimes(movie_title)
    print(f"Showtimes for '{movie_title}':")
    for showtime in showtimes:
        print(f"{showtime.datetime} - Available Seats: {showtime.available_seats}")

    num_seats_to_reserve = 2
    if standard_theater.reserve_seats(showtime1, num_seats_to_reserve):
        print(f"Reserved {num_seats_to_reserve} seats for '{showtime1.movie.title}'")
    else:
        print("Failed to reserve seats: Insufficient available seats.")


   
