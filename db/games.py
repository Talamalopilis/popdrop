from db.connection import DBConnection, DBInterface


class Games(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_game(self, game_name, image_path=None, max_players=None, genre=None):
        db = DBConnection()
        q = db.cursor.mogrify("insert into games values(%s,%s, %s, %s);", (game_name, image_path, max_players, genre))
        self._execute(db, q)

    def update_game(self, game_name, image_path=None, max_players=None, genre=None):
        self.update_game_image(game_name, image_path)
        self.update_game_metadata(game_name, max_players, genre)

    def update_game_image(self, game_name, image_path):
        db = DBConnection()
        q = db.cursor.mogrify("update games set image_path=%s where game_name=%s;", (image_path, game_name))
        self._execute(db, q)

    def update_game_metadata(self, game_name, max_players=None, genre=None):
        db = DBConnection()
        q = db.cursor.mogrify("update games set max_players=%s genre=%s where game_name=%s;", (max_players, genre, game_name))
        self._execute(db, q)

    def delete_game(self, game_name):
        db = DBConnection()
        q = db.cursor.mogrify("delete from games where game_name=%s", (game_name,))
        self._execute(db, q)