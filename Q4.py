from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import literal
from sqlalchemy.orm import aliased
from app.db.db_factory import DbFactory
from app.models.location import Location
from app.models.trip import Trip
from app.db.settings import get_base
from app.services.computational.haver_vincenty import haversine_
from collections import defaultdict

# write context manager for sqlite database session us that session to create functions.

def get_terminal_dist():
    base = get_base()
    sqlite_engine = DbFactory.get_db_engine('SqliteDbEngine', 'precourse.db').get_database()
    dbsession = sessionmaker(bind=sqlite_engine)
    session = dbsession()

    session.query(Location).count()
    location_alias = aliased(Location)
    dist_dict = defaultdict(None)
    for items in session.query(Location, location_alias).join(
              location_alias, literal(True)).all():
        items = sorted(items, key=lambda x: x.TERMINAL_NUMBER)
        dict_key = tuple(map(lambda x: x.TERMINAL_NUMBER, items))
        if dist_dict.get(dict_key):
            continue
        dist_dict[dict_key] = haversine_(
            (items[0].LATITUDE, items[0].LONGITUDE), (items[1].LATITUDE, items[0].LONGITUDE))

    session.close()
    return dist_dict
    
# Q5

def get_neighbour_stations(data,source_terminal , dist):
    return list({ele for item in filter(lambda x: x[0] != x[1] and data[x] > dist ,data) for ele in item})

# Q6
def get_trip_count(start_station, end_station, start_date, end_date):
    pass