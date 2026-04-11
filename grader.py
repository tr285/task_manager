from environment import MiniGameEnv

def grade_easy(env: MiniGameEnv) -> float:
    """Reach the goal."""
    if env.agent_pos == env.goal_pos:
        return 1.0
    return 0.0

def grade_medium(env: MiniGameEnv) -> float:
    """Reach the goal with fewer steps."""
    if env.agent_pos != env.goal_pos:
        return 0.0
    
    optimal_steps = (env.size - 1) * 2
    extra_steps = max(0, env.steps_taken - optimal_steps)
    
    score = 1.0 - (extra_steps * 0.02)
    return max(0.0, score)

def grade_hard(env: MiniGameEnv) -> float:
    """Reach the goal under strict step limit."""
    if env.agent_pos != env.goal_pos:
        return 0.0
    
    optimal_steps = (env.size - 1) * 2
    strict_limit = optimal_steps + 10
    
    if env.steps_taken > strict_limit:
        return 0.0
        
    extra_steps = max(0, env.steps_taken - optimal_steps)
    score = 1.0 - (extra_steps * 0.1)
    return max(0.0, score)