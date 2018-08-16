from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.db.settings import get_base
from app.models.location import Location
from app.models.trip import Trip

sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine', 
                                        "precourse_test.db", echo=True).get_database()

base = get_base()
base.metadata.create_all(sqlite_engine)
