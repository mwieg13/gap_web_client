# pyright: reportOptionalCall=none
# type: ignore

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models.goals import Goal_Model

class PostgresClient:

    def __init__(self):
        self.connected = False
        self.engine = None
        self.SessionLocal = None

    def connect(self, db_url: str):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
        if self.SessionLocal is not None:
            self.connected = True
            print("Successfully connected to database.")

    def is_connected(self):
        return self.connected and self.SessionLocal is not None
    
    def disconnect(self):
        if self.is_connected():
            self.SessionLocal.close_all()
        self.connected = False

    def get_session(self):
        if self.is_connected():
            return self.SessionLocal()
        else:
            raise Exception("Database not connected. Call connect() first.")
        
    def get_goal(self, goal_id: int):
        if not self.is_connected():
            raise Exception("Database not connected. Call connect() first.")

        session = self.SessionLocal()

        try:    
            goal = session.query(Goal_Model).where(Goal_Model._id == goal_id).first()

            if goal is None:
                print(f'WARN - No results returned for goal_id: {goal_id}')

        finally:
            session.close()

        return goal
