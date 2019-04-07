from db.games import Games


def test_games():
    games = Games()
    games.insert_game("Payday 2", 1, "test/", 4, "coop_shooter")
    print(games.get_game("Payday 2", 1))


test_games()
