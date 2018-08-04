from app.db.db_interface import Database
from sqlalchemy import create_engine

class SqliteDbEngine(Database):
    def __init__(self, dbfile, **kargs):
        self.db = create_engine("sqlite:///{}".format(dbfile), **kargs)

    def get_database(self, dbfile, **kargs):
        return SqliteDbEngine(dbfile, **kargs)