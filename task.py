from typing import Tuple
import queue
import numpy as np
from unit import Unit

class Task:

    class Target:
        unit: Unit
        product: np.ndarray
    
        def __init__(self, unit: Unit, product: np.ndarray) -> None:
            self.Unit = unit
            self.product = product
    
    name: str
    endtime: int
    targets: list[Target]
    
    def __init__(self, name: str, endtime: int) -> None:
        self.name = name
        self.endtime = endtime
        
class TaskQueue:
    
    tasks: queue.PriorityQueue[Tuple[int, Task]]
    time: int
    # todo: time 全局
    def __init__(self) -> None:
        self.time = 0
    
    def addTask(self, task: Task):
        self.tasks.put((task.endtime, task))
    
    def settle(self):
        cendtime, cTask = self.tasks.get()
        for t in cTask.targets:
            newTask = t.unit.produceTrigger()
            if newTask:
                self.addTask(newTask)
        self.time = cendtime