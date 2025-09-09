from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class PostgresClient:

    def __init__(self):
        self.connected = False
        self.engine = None
        self.SessionLocal = None

    def connect(self, db_url: str):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.connected = True

    def disconnect(self):
        if self.connected and self.SessionLocal is not None:
            self.SessionLocal.close_all()
        self.connected = False


    def get_session(self):
        if self.connected and self.SessionLocal is not None:
            return self.SessionLocal()
        else:
            raise Exception("Database not connected. Call connect() first.")
        
