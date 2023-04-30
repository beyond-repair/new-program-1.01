from typing import List
from task_class import Task
from delegate_class import Delegate


class TaskQueue:
    def __init__(self, tasks: List[Task], delegate: Delegate):
        self.tasks = tasks
        self.delegate = delegate

    def add_task(self, task: Task) -> None:
        pass

    def next_task(self, agent: GPTAgent) -> Task:
        pass

    def complete_task(self, task: Task) -> None:
        pass
