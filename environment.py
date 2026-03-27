from environment import TaskManagerEnv

env = TaskManagerEnv()
state = env.reset()

print(state)

state, reward, done = env.step(0)
print(state, reward, done)