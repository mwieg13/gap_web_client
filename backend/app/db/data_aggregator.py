from app.db.pg_client import PostgresClient
from app.db.schemas import *

class DataAggregator:

    def __init__(self, database: PostgresClient):
        self.database = database

    def collectData(self, goal_id: int):
        goal = GoalSchema()

        goalModel = self.database.get_goal(goal_id)

        if goalModel is not None:
            goal.populate(goalModel)

        return goal
