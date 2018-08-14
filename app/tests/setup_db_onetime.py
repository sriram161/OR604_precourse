from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.db.settings import base

sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine',"sqlite:///OR604_precourse.db")
base.metadata.create_all(bind=sqlite_engine)

dbsession = sessionmaker(bind=sqlite_engine)
session = dbsession()
session.commit()
session.close()
