from fastapi import FastAPI

from app.db.pg_client import PostgresClient
from app.db.models.goals import Goal_Model

# todo: move this guy into a secure location
DATABASE_URL = "postgresql://postgres:root@localhost:5432/gap"

database = PostgresClient()
database.connect(DATABASE_URL)

print(f'Is the database connected? -- {database.connected}')

# Get a session
session = database.get_session()

# Query all goals
goals = session.query(Goal_Model).all()

print(f'Retrieved {len(goals)} goals.')

for goal in goals:
    print(goal._id, goal.created_on, goal.state)

session.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI and React app!"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


