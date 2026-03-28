def grade_easy(env):
    return env.completed / len(env.tasks)


def grade_medium(env):
    total = sum(t.priority for t in env.tasks)
    done = sum(t.priority for t in env.tasks if t.completed)
    return done / total


def grade_hard(env):
    score = env.completed - env.missed
    return max(0.0, min(1.0, score / len(env.tasks)))