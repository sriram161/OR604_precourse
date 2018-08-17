from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.db.settings import get_base
from app.models.location import Location
from app.models.trip import Trip

sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine', 
                                        "precourse.db", echo=True).get_database()

base = get_base()

Location.__table__.create(sqlite_engine, checkfirst=True)
Trip.__table__.create(sqlite_engine, checkfirst=True)
