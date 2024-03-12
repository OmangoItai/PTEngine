from typing import Tuple
import queue
import numpy as np
from environment import Env
from entity import Entity

class Task:

    class Target:
        entityId: int
        product: np.ndarray
    
        def __init__(self, entityId: int, product: np.ndarray) -> None:
            self.entityId = entityId
            self.product = product
    
    endtime: int
    targets: list[Target]
    
    def __init__(self, endtime: int, targets: list[Target]) -> None:
        self.endtime = endtime
        self.targets = targets
        
class TaskQueue:
    env: Env
    tasks: queue.PriorityQueue[Tuple[int, Task]]
    def __init__(self, env) -> None:
        self.env = env
        self.tasks = queue.PriorityQueue()
    
    def addTask(self, task: Task):
        self.tasks.put((task.endtime, task))
    
    def settleATask(self):
        cEndtime, cTask = self.tasks.get()
        for t in cTask.targets:
            newTask: Task = t.entity.produceTrigger()
            newTask.endtime += self.env.time # 校准时钟
            if newTask:
                self.addTask(newTask)
        self.env.setTime(cEndtime)