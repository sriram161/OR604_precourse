from collections import defaultdict
from app.db.db_interface import Database

class DbFactory(object):
    databases = {class_.__name__: class_ for class_ in Database.__subclasses__()}
    singletons = defaultdict()

    @classmethod
    def get_db_engine(cls, systemname, dbfile, **kargs):
      if cls.singletons.get(systemname):
          return cls.singletons.get(systemname)
      cls.singletons[systemname] = cls.databases.get(systemname)(dbfile, **kargs)
      return cls.singletons.get(systemname)