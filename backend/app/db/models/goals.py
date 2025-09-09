from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Goal_Model(Base):
    __tablename__ = "goals"

    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    state = Column(String)