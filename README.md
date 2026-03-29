# Task Manager OpenEnv

## Description
This environment simulates a real-world task scheduling system.

## Observation
- time
- tasks (priority, deadline, duration)
- completed
- missed

## Action
- task_id

## Reward
- +1 progress
- +priority*2 completion
- -5 missed tasks

## Run
python run_agent.py

## Docker
docker build -t task-env .
docker run task-env