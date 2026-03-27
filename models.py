from pydantic import BaseModel
from typing import List
class Task (BaseModel):
    id: int
    priority :int
    deadlinr :int
    duration :int
    complete :bool

    class Obeservation (BaseModel):
      time:int
      tasks:List[Task]
      complete:int
      missed: int

      class Action (BaseModel):
        task_id : int
        
      class Reward(BaseModel):
        value :float
        


