import json

architecture = {
    "project": "Task Manager",
    "type": "Python RL Environment",
    "structure": {
        "Core": {
            "app.py": "Main entry point - runs the task manager agent",
            "environment.py": "TaskManagerEnv - RL environment with tasks, deadlines, priorities",
            "models.py": "Pydantic models: Task, Observation, Action",
            "tasks.py": "Grading functions: easy, medium, hard"
        },
        "Configuration": {
            "Dockerfile": "Docker containerization",
            "requirements.txt": "Dependencies: pydantic",
            "openenv.yaml": "Agent configuration",
            ".gitignore": "Git ignore rules"
        }
    },
    "flow": [
        "1. TaskManagerEnv initializes 5 random tasks",
        "2. Each task has: id, priority, deadline, duration",
        "3. Agent selects highest priority incomplete task",
        "4. Agent works on task (decreases duration)",
        "5. Completed tasks give reward based on priority",
        "6. Missed deadlines incur penalty (-5)",
        "7. Simulation ends at time=20",
        "8. Final score: completed - missed tasks"
    ],
    "output": "Total Reward (optimized task completion score)"
}

print(json.dumps(architecture, indent=2))
