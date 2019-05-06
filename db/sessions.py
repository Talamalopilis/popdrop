from db.connection import DBConnection, DBInterface


class ActiveSession():
    def __init__(self, hash_val, session_ids):
        self.hash_val = hash_val
        self.session_ids = session_ids


class Sessions(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_session(self, server_id, game_name, date_of_session, time_of_day):
        db = DBConnection()
        q = db.cursor.mogrify("insert into sessions values(default, %s, %s, now(), %s, %s);", (server_id,
                                                                                               game_name,
                                                                                               date_of_session,
                                                                                               time_of_day))
        success = self._execute(db, q)
        db.close()
        return success

    def get_active_sessions(self, server_id):
        db = DBConnection()
        q = db.cursor.mogrify("select * from sessions where server_id=%s and date_of_session>=now()::date;", (server_id,))
        self._execute(db, q)
        out = db.cursor.fetchall()
        db.close()
        return out

    def get_session_id(self, server_id, game_name, date_of_session):
        db = DBConnection()
        q = db.cursor.mogrify("select session_id from sessions where server_id=%s and game_name=%s and "
                              "date_of_session=%s", (server_id, game_name, date_of_session))
        self._execute(db, q)
        out = db.cursor.fetchone()
        db.close()
        return out

    def get_session(self, session_id):
        db = DBConnection()
        q = db.cursor.mogrify("select * from sessions where session_id=%s", (session_id,))
        self._execute(db, q)
        out = db.cursor.fetchone()
        db.close()
        return out

    def delete_session(self, session_id):
        pass