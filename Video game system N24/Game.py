from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, title, genre, release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @abstractmethod
    def play(self):
        pass

class SportsGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Sports", release_date)

    def play(self):
        print(f"Playing sports game: {self.title}")

class AdventureGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Adventure", release_date)

    def play(self):
        print(f"Playing adventure game: {self.title}")
