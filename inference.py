from environment import MiniGameEnv
from grader import grade_easy, grade_medium, grade_hard
from models import Action

def run_agent(difficulty: str, seed: int = 42):
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
        
    return env

if __name__ == "__main__":
    print("Running baseline agent evaluation...")
    
    # Easy
    env_easy = run_agent("easy")
    score_easy = grade_easy(env_easy)
    print(f"Easy Score: {score_easy:.2f} | Steps: {env_easy.steps_taken}")
    
    # Medium
    env_med = run_agent("medium")
    score_med = grade_medium(env_med)
    print(f"Medium Score: {score_med:.2f} | Steps: {env_med.steps_taken}")
    
    # Hard
    env_hard = run_agent("hard")
    score_hard = grade_hard(env_hard)
    print(f"Hard Score: {score_hard:.2f} | Steps: {env_hard.steps_taken}")