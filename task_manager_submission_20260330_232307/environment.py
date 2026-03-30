import random
from models import Task, Observation, Action

class TaskManagerEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.time = 0
        self.tasks = []

        for i in range(5):
            t = Task(
                id=i,
                priority=random.randint(1, 5),
                deadline=random.randint(5, 15),
                duration=random.randint(1, 3),
                completed=False
            )
            self.tasks.append(t)

        self.completed = 0
        self.missed = 0

        return self.state()

    def state(self):
        return Observation(
            time=self.time,
            tasks=self.tasks,
            completed=self.completed,
            missed=self.missed
        )

    def step(self, action: Action):
        reward = 0

        # work on task
        for t in self.tasks:
            if t.id == action.task_id and not t.completed:
                t.duration -= 1
                reward += 1   # partial progress

                if t.duration <= 0:
                    t.completed = True
                    self.completed += 1
                    reward += t.priority * 2

        # penalty for missed
        for t in self.tasks:
            if not t.completed and self.time > t.deadline:
                t.completed = True
                self.missed += 1
                reward -= 5

        self.time += 1

        done = self.time > 20

        return self.state(), reward, done, {}