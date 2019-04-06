from db.games import Games


def test_games():
    games = Games()
    games.insert_game("Payday 2", "test/", 4, "coop_shooter")


test_games()
