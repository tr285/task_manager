from environment import MiniGameEnv
from grader import grade_easy, grade_medium, grade_hard
from models import Action

def run_agent(difficulty: str, seed: int = 42):
    print(f"[START] task={difficulty}", flush=True)
    env = MiniGameEnv(difficulty=difficulty)
    obs = env.reset(seed=seed)
    
    done = False
    
    while not done:
        agent_x, agent_y = obs.agent_position
        goal_x, goal_y = obs.goal_position
        
        # Simple blind baseline: move right then down
        if agent_x < goal_x:
            action = Action(direction="right")
        elif agent_y < goal_y:
            action = Action(direction="down")
        else:
            break # Reached or some issue
            
        obs, reward, done, _ = env.step(action)
        print(f"[STEP] step={env.steps_taken} reward={reward}", flush=True)
        
    return env

if __name__ == "__main__":
    print("Running baseline agent evaluation...", flush=True)
    
    # Easy
    env_easy = run_agent("easy")
    score_easy = grade_easy(env_easy)
    print(f"[END] task=easy score={score_easy:.2f} steps={env_easy.steps_taken}", flush=True)
    
    # Medium
    env_med = run_agent("medium")
    score_med = grade_medium(env_med)
    print(f"[END] task=medium score={score_med:.2f} steps={env_med.steps_taken}", flush=True)
    
    # Hard
    env_hard = run_agent("hard")
    score_hard = grade_hard(env_hard)
    print(f"[END] task=hard score={score_hard:.2f} steps={env_hard.steps_taken}", flush=True)