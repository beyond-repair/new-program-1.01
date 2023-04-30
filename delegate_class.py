from typing import List
from gpt_agent import GPTAgent
from task_class import Task


class Delegate:
    def __init__(self, agents: List[GPTAgent]):
        self.agents = agents

    def assign_agent(self, task: Task) -> GPTAgent:
        pass

    def delegate_task(self, task: Task, agent: GPTAgent) -> None:
        pass

    def double_check_task(self, task: Task) -> None:
        pass
