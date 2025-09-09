from pydantic import BaseModel
from typing import Optional

class Goal(BaseModel):
    _id: Optional[int] = None
    created_on: str
    state: str