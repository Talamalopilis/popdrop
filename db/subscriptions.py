from db.connection import DBConnection, DBInterface


class Subscriptions(DBInterface):
    def __init__(self):
        super().__init__()

    def insert_subscriptions(self, session_id, user_id, user_name):
        pass

    def delete_subscriptions(self):
        pass