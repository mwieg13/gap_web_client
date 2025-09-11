from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.pg_client import PostgresClient
from app.db.data_aggregator import DataAggregator

# TODO: move this guy into a secure location
DATABASE_URL = "postgresql://postgres:root@localhost:5432/gap"

database = PostgresClient()
aggregator = DataAggregator(database)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on application startup
    print("FastAPI -- starting")
    database.connect(DATABASE_URL)

    yield

    # Code to run on application shutdown
    print("FastAPI -- shutting down")
    database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI and React app!"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.get("/goal/{goal_id}")
def get_goal(goal_id: int):
    return aggregator.collectData(goal_id).model_dump_json()

