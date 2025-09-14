from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Goal_Obstacles_Model(Base):
    __tablename__ = "goal_obstacles"

    obstacle_id = Column(Integer, primary_key=True, index=True, nullable=False)
    goal_id = Column(Integer, nullable=False)
    obstacle_num = Column(Integer, nullable=False)
    obstacle_text = Column(String, nullable=False)
    overcame_it = Column(Boolean, default=False)