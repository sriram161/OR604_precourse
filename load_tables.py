import csv
import codecs
from sqlalchemy.orm import sessionmaker
from app.db.db_factory import DbFactory
from app.models.location import Location
from app.models.trip import Trip
from app.db.settings import get_base
from itertools import count

sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine', "precourse_test.db", echo=True).get_database()

base = get_base()
base.metadata.bind=sqlite_engine

dbsession = sessionmaker(bind=sqlite_engine)
session = dbsession()
data_path = r"C:\Users/ksrir/Development/OR604_precourse/app/data/"
zip_file = r'Capital_BikeShare_Data.zip'
location_file = r'Capital_Bike_Share_Locations.csv'

with codecs.open(data_path + location_file, 'r', 
                encoding='ascii', errors='ignore') as f_handle:
    reader = csv.DictReader(f_handle)
    for item in reader:
        session.add(Location(**item))
    session.commit()
    print("File_loaded...! location")

import zipfile
with  zipfile.ZipFile(data_path + zip_file) as zipf:
    row_id = count(1,1)
    for f_name in zipf.filelist:
        with zipf.open(f_name, 'r') as f_handle:
            header = next(f_handle).decode().strip('\r\n').split(',')
            header.insert(0, 'ROW_ID')
            for row in f_handle:
                row = row.decode().strip('\r\n').split(',')
                row.insert(0, next(row_id))
                session.add(Trip(**dict(zip(header,row))))
            session.commit()
            print("File_loaded...! {}".format(f_name))


session.close()
