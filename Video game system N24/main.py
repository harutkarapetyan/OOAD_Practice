from Game import SportsGame, AdventureGame
from Console import Console 
from Player import Player



if __name__ == "__main__":
    sports_game = SportsGame("FIFA 2023", "2022-10-15")
    adventure_game = AdventureGame("Assassin's Creed", "2022-09-20")

    xbox_console = Console("Xbox")
    xbox_console.install_game(sports_game)
    xbox_console.install_game(adventure_game)

    player1 = Player("Alice", "alice@examplegmail.com")
    player2 = Player("Bob", "bob@examplegmail.com")

    player1.play_game(xbox_console, sports_game)
    player2.play_game(xbox_console, adventure_game)

    
