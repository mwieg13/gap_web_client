from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Goal_Data_Model(Base):
    __tablename__ = "goal_data"

    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    objectives = Column(String)
    due_on = Column(DateTime, default=datetime.datetime.utcnow)
    