from db.connection import DBConnection, DBInterface


class Subscriptions(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_subscriptions(self, session_id, user_id, user_name):
        db = DBConnection()
        q = db.cursor.mogrify("insert into subscriptions values(%s, %s, %s);",
                              (session_id, user_id, user_name))
        success = self._execute(db, q)
        db.close()
        return success

    def get_subscriptions_names_by_session(self, session_id):
        db = DBConnection()
        q = db.cursor.mogrify("select user_name from subscriptions where session_id=%s;",
                              (session_id,))
        success = self._execute(db, q)
        out = db.cursor.fetchall()
        db.close()
        return out

    def get_subscriptions_count_by_session(self, session_id):
        db = DBConnection()
        q = db.cursor.mogrify("select count(user_id) from subscriptions where session_id=%s;",
                              (session_id,))
        success = self._execute(db, q)
        out = db.cursor.fetchone()
        db.close()
        return out

    def delete_subscriptions(self):
        pass