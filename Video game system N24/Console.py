
class Console:
    def __init__(self, console_type):
        self.console_type = console_type
        self.games_installed = []

    def install_game(self, game):
        self.games_installed.append(game)

    def play_game(self, game):
        if game in self.games_installed:
            game.play()
        else:
            print(f"{game.title} is not installed on this {self.console_type} console.")
