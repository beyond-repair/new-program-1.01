from typing import List

class Task:
    def __init__(self, name: str, agents: List, priority: int, status: str):
        self.name = name
        self.agents = agents
        self.priority = priority
        self.status = status
