from Movie import ComedyMovie, DramaMovie
from Costomer import Customer  

if __name__ == "__main__":
   
    customer1 = Customer("Alice", "alice@examplegmail.com")
    customer2 = Customer("Bob", "bob@examplegmail.com")

    comedy_movie = ComedyMovie("The Hangover", "Comedy", "R")
    drama_movie = DramaMovie("The Shawshank Redemption", "Drama", "PG-13")

    customer1.rent_movie(comedy_movie, 3)
    customer2.rent_movie(drama_movie, 5)

    customer1.view_rental_history()
    customer2.view_rental_history()

    comedy_movie.return_movie(customer1)
    drama_movie.return_movie(customer2)
