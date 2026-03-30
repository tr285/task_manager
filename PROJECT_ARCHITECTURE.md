# Task Manager - Project Architecture

## 📋 Project Overview
**Type:** Python Reinforcement Learning Environment  
**Purpose:** AI Agent learns to prioritize and complete tasks within deadlines  
**Language:** Python 3.10  
**Containerized:** Yes (Docker)

---

## 🏗️ Project Structure

```
task_manager/
├── app.py                 # Main entry point - runs the agent loop
├── environment.py         # TaskManagerEnv - RL environment core
├── models.py              # Pydantic models (Task, Observation, Action)
├── tasks.py               # Grading functions (easy/medium/hard)
├── run_agent.py           # Agent runner script
├── requirements.txt       # Dependencies (pydantic)
├── Dockerfile             # Docker containerization
├── openenv.yaml           # Agent configuration
├── .gitignore             # Git settings
└── README.md              # Documentation
```

---

## 🔄 Agent Flow Diagram

```
┌─────────────────────────────────────┐
│  Initialize TaskManagerEnv          │
│  - 5 random tasks                   │
│  - Random priority (1-5)            │
│  - Random deadline (5-15)           │
│  - Random duration (1-3)            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Agent Decision Loop                │
│  1. Find highest priority task      │
│  2. Select that task               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Execute Action (work on task)      │
│  - Decrease task duration by 1      │
│  - Reward += 1 (progress bonus)     │
│  - If complete: reward += priority*2│
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Check for Missed Deadlines         │
│  - If time > deadline:              │
│    - Mark task complete             │
│    - missed += 1                    │
│    - Reward -= 5 (penalty)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Increment Time (time += 1)         │
│  Check if done (time > 20)          │
└──────────────┬──────────────────────┘
               │
        No ────┴────────┐
               │         │
               ▼         │
    ┌─────────────────┐  │
    │ Continue Loop   │  │
    └────────┬────────┘  │
             └───────────┘
                    │
                   Yes
                    │
                    ▼
         ┌──────────────────────┐
         │ Return Final Score   │
         │ (completed - missed) │
         └──────────────────────┘
```

---

## 📊 Task Properties

Each task has:
- **id:** Unique identifier (0-4)
- **priority:** Importance level (1-5) - affects reward
- **deadline:** Time limit to complete (5-15)
- **duration:** Work time needed (1-3 steps)
- **completed:** Boolean flag

---

## 🏆 Scoring System

### Easy Grade
```
Score = completed_tasks / total_tasks
```

### Medium Grade
```
Score = sum(priority of completed tasks) / sum(all priorities)
```

### Hard Grade
```
Score = max(0, completed_tasks - missed_tasks) / total_tasks
```

---

## 🐳 Docker Setup

**Base Image:** `python:3.10`  
**Dependencies:** `pydantic`  
**Entrypoint:** `python app.py`

---

## 🚀 To Build & Run

```bash
# Build image
docker build -t task-manager .

# Run container
docker run --rm task-manager
```

**Output:**
```
Running in Hugging Face Docker
Final Reward: [score]
```

---

## 🔧 Technologies Used

- **Python 3.10** - Core language
- **Pydantic** - Data validation & modeling
- **Docker** - Containerization
- **Reinforcement Learning** - Agent decision-making

---

## 📝 Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main agent loop - selects & executes actions |
| `environment.py` | RL environment - manages state, rewards, done conditions |
| `models.py` | Type definitions using Pydantic |
| `tasks.py` | Three difficulty-level grading functions |
| `Dockerfile` | Container configuration |
| `requirements.txt` | Python dependencies |

---

## 🎯 Agent Strategy

The current agent uses a **greedy priority-based strategy**:
1. Always select the incomplete task with highest priority
2. Work on it until complete
3. Move to next highest priority task
4. Continue until time limit (20 steps) or all tasks done

**Optimal Goal:** Maximize completed task count while respecting deadlines.

---

Generated: Task Manager Project Architecture
