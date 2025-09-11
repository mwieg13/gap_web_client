from pydantic import BaseModel
from datetime import date

from typing import List, Optional

from app.db.models.goals import Goal_Model

class GoalDataSchema(BaseModel):
    objective: str
    due_on: date

class GoalStepSchema(BaseModel):
    step_id: int
    step_num: int
    step_text: str
    state: str

class GoalObstacleSchema(BaseModel):
    obstacle_id: int
    obstacle_num: int
    obstacle_text: str
    overcame_it: bool

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
        