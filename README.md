# Task Manager OpenEnv

## Description
This environment simulates real-world task scheduling where an AI agent must prioritize and complete tasks before deadlines.

## Observation Space
- time (int)
- tasks (list of tasks with priority, deadline, duration)
- completed (int)
- missed (int)

## Action Space
- task_id (int)

## Reward Function
- +1 for working on task (progress)
- +priority*2 for completion
- -5 for missed deadlines

## Tasks
- Easy: maximize completed tasks
- Medium: maximize weighted priority
- Hard: minimize missed deadlines

## Run
python run_agent.py

## Docker
docker build -t task-env .
docker run task-env