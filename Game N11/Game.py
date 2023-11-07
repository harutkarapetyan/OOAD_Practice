class Game:
    def __init__(self, developer, title, genre, release_date, game_type):
        self.developer = developer
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.game_type = game_type

class GameRelease:
    def __init__(self, game, release_date):
        self.game = game
        self.release_date = release_date
