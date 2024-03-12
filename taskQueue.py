from typing import Tuple
import queue
import numpy as np
from environment import Env
from unit import Unit

class Task:

    class Target:
        unitId: int
        product: np.ndarray
    
        def __init__(self, unitId: int, product: np.ndarray) -> None:
            self.unitId = unitId
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
            newTask: Task = t.unit.produceTrigger()
            newTask.endtime += self.env.time # 校准时钟
            if newTask:
                self.addTask(newTask)
        self.env.setTime(cEndtime)