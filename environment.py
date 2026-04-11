import random
from typing import Tuple, Dict, Any
from models import Observation, Action

class MiniGameEnv:
    def __init__(self, size: int = 10, difficulty: str = "easy"):
        self.size = size
        self.difficulty = difficulty
        self.reset()
        
    def reset(self, seed: int = None) -> Observation:
        if seed is not None:
            random.seed(seed)
            
        self.agent_pos = (0, 0)
        self.goal_pos = (self.size - 1, self.size - 1)
        self.steps_taken = 0
        
        self.traps = set()
        self.rewards = set()
        
        if self.difficulty == "easy":
            num_traps = 5
            num_rewards = 5
        elif self.difficulty == "medium":
            num_traps = 15
            num_rewards = 5
        else: # hard
            num_traps = 25
            num_rewards = 3
            
        def get_rand_pos():
            while True:
                p = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if p != self.agent_pos and p != self.goal_pos:
                    return p
                    
        for _ in range(num_traps):
            p = get_rand_pos()
            self.traps.add(p)
            
        for _ in range(num_rewards):
            p = get_rand_pos()
            if p not in self.traps:
                self.rewards.add(p)
                
        return self.get_observation()
        
    def get_observation(self) -> Observation:
        return Observation(
            agent_position=self.agent_pos,
            goal_position=self.goal_pos,
            grid_size=self.size,
            steps_taken=self.steps_taken
        )
        
    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict[str, Any]]:
        self.steps_taken += 1
        x, y = self.agent_pos
        
        if action.direction == "up":
            y = max(0, y - 1)
        elif action.direction == "down":
            y = min(self.size - 1, y + 1)
        elif action.direction == "left":
            x = max(0, x - 1)
        elif action.direction == "right":
            x = min(self.size - 1, x + 1)
            
        self.agent_pos = (x, y)
        reward = -1.0
        done = False
        
        if self.agent_pos == self.goal_pos:
            reward += 10.0
            done = True
        elif self.agent_pos in self.traps:
            reward -= 5.0
        elif self.agent_pos in self.rewards:
            reward += 3.0
            self.rewards.remove(self.agent_pos) 
            
        return self.get_observation(), reward, done, {}