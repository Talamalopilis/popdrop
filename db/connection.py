import psycopg2, sys, os
# Open your DB connection here
psql_user = 'postgres'  # Change this to your username
psql_db = 'popdrop'  # Change this to your personal DB name
psql_password = os.environ['PSQL_PASSWORD']  # Put your password (as a string) here
psql_server = 'localhost'
psql_port = 5432


class DBConnection:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


class DBInterface:
    def __init__(self):
        pass

    @staticmethod
    def _execute(db, query):
        success = False
        try:
            db.cursor.execute(query)
            db.conn.commit()
            success = True
        except psycopg2.ProgrammingError as err:
            # ProgrammingError is thrown when the database error is related to the format of the query (e.g. syntax error)
            print("Caught a ProgrammingError:", file=sys.stderr)
            print(err, file=sys.stderr)
            db.conn.rollback()
        except psycopg2.IntegrityError as err:
            # IntegrityError occurs when a constraint (primary key, foreign key, check constraint or trigger constraint) is violated.
            print("Caught an IntegrityError:", file=sys.stderr)
            print(err, file=sys.stderr)
            db.conn.rollback()
        except psycopg2.InternalError as err:
            # InternalError generally represents a legitimate connection error, but may occur in conjunction with user defined functions.
            # In particular, InternalError occurs if you attempt to continue using a cursor object after the transaction has been aborted.
            # (To reset the connection, run conn.rollback() and conn.reset(), then make a new cursor)
            print("Caught an IntegrityError:", file=sys.stderr)
            print(err, file=sys.stderr)
            db.conn.rollback()

        return success