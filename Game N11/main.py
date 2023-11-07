from Developer import Developer
from Transaction import ActionGame, StrategyGame
from Publishier import Publisher

if __name__ == "__main__":
   
    developer1 = Developer("GameDev1", "dev1@examplegmail.com")
    developer2 = Developer("GameDev2", "dev2@examplegmail.com")

    action_game = ActionGame()
    strategy_game = StrategyGame()

    developer1.create_game(action_game, "Action Game 1", "Action", "2023-01-01")
    developer2.create_game(strategy_game, "Strategy Game 1", "Strategy", "2023-02-01")

    publisher = Publisher("GamePublisher", "publisher@example.com")

    publisher.manage_release(developer1.games[0], "2023-01-15")
    publisher.manage_release(developer2.games[0], "2023-02-15")

    print("Games developed by Developer 1:")
    for game in developer1.games:
        print(f"- {game.title} ({game.genre})")

    print("Games developed by Developer 2:")
    for game in developer2.games:
        print(f"- {game.title} ({game.genre})")

    print("Game releases managed by Publisher:")
    for release in publisher.releases:
        print(f"- {release.game.title} released on {release.release_date}")

