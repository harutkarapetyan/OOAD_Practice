from validate_decorators import validate_email, validate_non_empty_string

class Developer:
    @validate_non_empty_string("nmae")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.games = []

    def create_game(self, game_type, title, genre, release_date):
        game = game_type.create_game(self, title, genre, release_date)
        self.games.append(game)

    def manage_game(self, game):
        print(f"{self.name} is managing the game '{game.title}'.")
