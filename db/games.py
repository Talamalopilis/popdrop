from db.connection import DBConnection, DBInterface


class Games(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_game(self, game_name, server_id, image_path=None, max_players=None, genre=None):
        db = DBConnection()
        q = db.cursor.mogrify("insert into games values(%s, %s, %s, %s, %s);", (game_name, server_id, image_path, max_players, genre))
        success = self._execute(db, q)
        db.close()
        return success

    def update_game(self, game_name, server_id, image_path=None, max_players=None, genre=None):
        s1 = self.update_game_image(game_name, server_id, image_path)
        s2 = self.update_game_metadata(game_name, server_id, max_players, genre)
        return s1 and s2

    def update_game_image(self, game_name, server_id, image_path):
        db = DBConnection()
        q = db.cursor.mogrify("update games set image_path=%s where game_name=%s and server_id=%s;", (image_path, game_name, server_id))
        success = self._execute(db, q)
        db.close()
        return success

    def update_game_metadata(self, game_name, server_id, max_players=None, genre=None):
        db = DBConnection()
        q = db.cursor.mogrify("update games set max_players=%s genre=%s where game_name=%s and server_id=%s;", (max_players, genre, game_name, server_id))
        success = self._execute(db, q)
        db.close()
        return success

    def delete_game(self, game_name):
        db = DBConnection()
        q = db.cursor.mogrify("delete from games where game_name=%s;", (game_name,))
        success = self._execute(db, q)
        db.close()
        return success

    def get_game(self, game_name, server_id):
        db = DBConnection()
        q = db.cursor.mogrify("select * from games where game_name=%s and server_id=%s;", (game_name, server_id))
        self._execute(db, q)
        out = db.cursor.fetchone()
        db.close()
        return out

    def get_games(self, server_id):
        db = DBConnection()
        q = db.cursor.mogrify("select game_name from games where server_id=%s;", (server_id,))
        self._execute(db, q)
        out = db.cursor.fetchall()
        db.close()
        return out
