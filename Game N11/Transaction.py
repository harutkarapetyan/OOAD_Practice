from abc import ABC, abstractmethod
from Game import Game
# Abstract class for game operations
class GameOperation(ABC):
    @abstractmethod
    def create_game(self, developer, title, genre, release_date):
        pass

    @abstractmethod
    def manage_game(self, developer, game):
        pass

# Concrete classes for different types of games
class ActionGame(GameOperation):
    def create_game(self, developer, title, genre, release_date):
        game = Game(developer, title, genre, release_date, "action")
        return game

    def manage_game(self, developer, game):
        developer.manage_game(game)

class StrategyGame(GameOperation):
    def create_game(self, developer, title, genre, release_date):
        game = Game(developer, title, genre, release_date, "strategy")
        return game

    def manage_game(self, developer, game):
        developer.manage_game(game)