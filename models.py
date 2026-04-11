from pydantic import BaseModel
from typing import Tuple, Literal

class Observation(BaseModel):
    agent_position: Tuple[int, int]
    goal_position: Tuple[int, int]
    grid_size: int
    steps_taken: int

class Action(BaseModel):
    direction: Literal["up", "down", "left", "right"]