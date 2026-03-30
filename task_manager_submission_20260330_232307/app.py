from environment import TaskManagerEnv
from models import Action

def main():
    env = TaskManagerEnv()
    state = env.reset()

    total_reward = 0

    while True:
        tasks = state.tasks

        best = None
        max_p = -1

        for t in tasks:
            if not t.completed and t.priority > max_p:
                best = t
                max_p = t.priority

        if best is None:
            break

        action = Action(task_id=best.id)

        state, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    print("Running in Hugging Face Docker")
    print("Final Reward:", total_reward)


if __name__ == "__main__":
    main()