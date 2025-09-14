from app.db.pg_client import PostgresClient
from app.db.schemas import *

class DataAggregator:

    def __init__(self, database: PostgresClient):
        self.database = database

    def collectData(self, goal_id: int):
        data = GoalSchema()

        goalModel = self.database.get_goal(goal_id)
        goalDataModel = self.database.get_goal_data(goal_id)

        goalStepModels = self.database.get_goal_steps(goal_id)
        goalObstacleModels = self.database.get_goal_obstacles(goal_id)

        # if we didn't get data from the goal table, assume that all further queries returned no data
        if goalModel is None:
            return data
        
        data.populate(goalModel)

        if goalDataModel is not None:
            data.add_data(goalDataModel)

        if goalStepModels is not None:
            for model in goalStepModels:
                data.add_step(model)

        if goalObstacleModels is not None:
            for model in goalObstacleModels:
                data.add_obstacle(model)

        return data
