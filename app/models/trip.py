from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.orm import relationship
from app.db.settings import base

class Trip(base):
    __tablename__ = 'trip'
    TRIP_DURATION = Column(BigInteger, nullable=False)
    START_DATE= Column(DateTime, nullable=False)
    START_STATION= Column(String(8), nullable=False)
    STOP_DATE= Column(DateTime, nullable=False)
    STOP_STATION= Column(String(8), nullable=False)
    BIKE_ID= Column(String(6), nullable=False)
    USER_TYPE= Column(String(15), nullable=False)
