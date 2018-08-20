import csv
import codecs
import zipfile
from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.db.settings import get_base
from app.models.location import Location
from app.models.trip import Trip
from app.db.context import DBSession
from itertools import count

def create_tables(systemname, dbfile):
    base = get_base()
    sqlite_engine = DbFactory.get_db_engine(systemname, 
                                        dbfile).get_database()
    Location.__table__.create(sqlite_engine, checkfirst=True)
    Trip.__table__.create(sqlite_engine, checkfirst=True)
    sqlite_engine.dispose()


def load_location_table(data_path, location_file, systemname, dbfile):
    with DBSession(systemname, dbfile) as session, codecs.open(data_path + location_file, 'r',
                                                               encoding='ascii', errors='ignore') as f_handle:
        reader = csv.DictReader(f_handle)
        for item in reader:
            session.add(Location(**item))
        print("File_loaded...! {}".format(location_file))

def load_trip_table(data_path, zip_file, systemname, dbfile):
    with zipfile.ZipFile(data_path + zip_file) as zipf:
        row_id = count(1, 1)
        for f_name in zipf.filelist:
            with DBSession(systemname, dbfile) as session, zipf.open(f_name, 'r') as f_handle:
                header = next(f_handle).decode().strip('\r\n').split(',')
                header.insert(0, 'ROW_ID')
                for row in f_handle:
                    row = row.decode().strip('\r\n').split(',')
                    row.insert(0, next(row_id))
                    session.add(Trip(**dict(zip(header, row))))
                print("File_loaded...! {}".format(f_name))
