from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.models.location import Location
from app.models.trip import Trip
from app.db.settings import get_base

sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine', 'precourse.db').get_database()
base = get_base()
base.metadata.bind = sqlite_engine
dbsession = sessionmaker(bind=sqlite_engine)
session = dbsession()
session.query(Location).first()
print('Location table count: ', session.query(Location).count())
print('Trip table count: ',session.query(Trip).count())
session.commit()
session.close()
