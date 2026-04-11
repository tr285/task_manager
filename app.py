from fastapi import FastAPI
from pydantic import BaseModel
from models import Observation, Action
from environment import MiniGameEnv

app = FastAPI(title="RL Mini-Game OpenEnv", description="Grid-based RL environment following OpenEnv specs.")

# Global instance of the environment
env = MiniGameEnv()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Welcome to OpenEnv RL Mini-Game",
        "endpoints": ["/reset", "/step", "/state", "/docs"]
    }

class ResetResponse(BaseModel):
    observation: Observation

class StepResponse(BaseModel):
    observation: Observation
    reward: float
    done: bool

@app.post("/reset", response_model=ResetResponse)
def reset_env():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step", response_model=StepResponse)
def step_env(action: Action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }

@app.get("/state", response_model=Observation)
def get_state():
    return env.get_observation()