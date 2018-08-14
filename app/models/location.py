from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.db.settings import base

class Location(base):
    __tablename__ = 'location'
    OBJECTID= Column(String(12), nullable=False)
    ID= Column(Integer, nullable=False)
    ADDRESS= Column(String(50), nullable=False)
    TERMINAL_NUMBER= Column(String(8), nullable=False)
    LATITUDE= Column(Float, nullable=False)
    LONGITUDE= Column(Float, nullable=False)
    INSTALLED= Column(String(8), nullable=False)
    LOCKED= Column(String(8), nullable=False)
    INSTALL_DATE= Column(DateTime, nullable=True)
    REMOVAL_DATE= Column(DateTime, nullable=True)
    TEMPORARY_INSTALL= Column(String(8), nullable=False)
    NUMBER_OF_BIKES= Column(Integer, nullable=False)
    NUMBER_OF_EMPTY_DOCKS= Column(Integer, nullable=False)
    X= Column(Float, nullable=False)
    Y= Column(Float, nullable=False)
    SE_ANNO_CAD_DATA= Column(String(50), nullable=True)


