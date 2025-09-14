# pyright: reportAttributeAccessIssue=none
# pyright: reportArgumentType=none

from pydantic import BaseModel
from datetime import date

from typing import List, Optional

from app.db.models.goal_model import Goal_Model
from app.db.models.goal_data_model import Goal_Data_Model
from app.db.models.goal_steps_model import Goal_Steps_Model
from app.db.models.goal_obstacles_model import Goal_Obstacles_Model

class GoalDataSchema(BaseModel):
    objective: str
    due_on: date

    # class Config:
    #     allow_mutation = True

    # def populate(self, goal_data: Goal_Data_Model):
    #     self.objective = goal_data.objectives
    #     self.due_on = goal_data.due_on

class GoalStepSchema(BaseModel):
    step_id: int
    step_num: int
    step_text: str
    state: str

    # class Config:
    #     allow_mutation = True

    # def populate(self, goal_step: Goal_Steps_Model):
    #     self.step_id = goal_step.step_id
    #     self.step_num = goal_step.step_num
    #     self.step_text = goal_step.step_text
    #     self.state = goal_step.state

class GoalObstacleSchema(BaseModel):
    obstacle_id: int
    obstacle_num: int
    obstacle_text: str
    overcame_it: bool

    # class Config:
    #     allow_mutation = True

    # def populate(self, goal_obs: Goal_Obstacles_Model):
    #     self.obstacle_id = goal_obs.obstacle_id
    #     self.obstacle_num = goal_obs.obstacle_num
    #     self.obstacle_text = goal_obs.obstacle_text
    #     self.overcame_it = goal_obs.overcame_it


class GoalSchema(BaseModel):
    goal_id: Optional[int] = None
    created_on: Optional[date] = None
    state: Optional[str] = None
    goal_data: Optional[GoalDataSchema] = None
    goal_steps: List[GoalStepSchema] = []
    obstacles: List[GoalObstacleSchema] = []

    class Config:
        allow_mutation = True

    def populate(self, goal: Goal_Model):
        self.goal_id = goal._id 
        self.created_on = goal.created_on
        self.state = goal.state

    def add_data(self, data: Goal_Data_Model):
        self.goal_data = GoalDataSchema(
            objective   = data.objectives, 
            due_on      = data.due_on
        )

    def add_step(self, step: Goal_Steps_Model):
        step_schema = GoalStepSchema(
            step_id     = step.step_id,
            step_num    = step.step_num,
            step_text   = step.step_text,
            state       = step.state
        )
        self.goal_steps.append(step_schema)

    def add_obstacle(self, obstacle: Goal_Obstacles_Model):
        obstacle_schema = GoalObstacleSchema(
            obstacle_id     = obstacle.obstacle_id,
            obstacle_num    = obstacle.obstacle_num,
            obstacle_text   = obstacle.obstacle_text,
            overcame_it     = obstacle.overcame_it
        )
        self.obstacles.append(obstacle_schema)
        