from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Goal_Steps_Model(Base):
    __tablename__ = "goal_steps"

    step_id = Column(Integer, primary_key=True, index=True, nullable=False)
    goal_id = Column(Integer, nullable=False)
    step_num = Column(Integer, nullable=False)
    step_text = Column(String, nullable=False)
    state = Column(String)