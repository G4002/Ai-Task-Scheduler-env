import random

class TaskSchedulerEnv:
    def __init__(self):
        self.tasks = []
        self.current_step = 0

    def reset(self):
        self.tasks = [
            {"name": "Task1", "priority": 3},
            {"name": "Task2", "priority": 1},
            {"name": "Task3", "priority": 2}
        ]
        self.current_step = 0
        return self.tasks

    def step(self, action):
        # action = index of selected task
        selected_task = self.tasks[action]

        # check if it's highest priority
        max_priority = max(task["priority"] for task in self.tasks)

        if selected_task["priority"] == max_priority:
            reward = 1
        else:
            reward = -1

        self.current_step += 1
        done = self.current_step >= 3

        return self.tasks, reward, done