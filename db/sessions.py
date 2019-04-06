from db.connection import DBConnection, DBInterface


class Sessions(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_session(self, server_id, game_name, day_of_week, time_of_day):
        db = DBConnection()
        q = db.cursor.mogrify("insert into sessions values(default, %s, %s, now(), %s, %s);", (server_id,
                                                                                               game_name,
                                                                                               day_of_week,
                                                                                               time_of_day))