import numpy as np
from typing import Tuple
import queue

from environment import Env
from mapGraph import MapGraph
from person import Person
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
            newTask: Task = self.env.unitList[t.unitId].triggers[' ']()
            newTask.endtime += self.env.time # 校准时钟
            if newTask:
                self.addTask(newTask)
        self.env.setTime(cEndtime)

class PTEngine:
    envModel: Env
    taskModel: TaskQueue
    def __init__(self, naturalResources: np.ndarray, personList: list[Person], unitList: list[Unit], map: MapGraph, priceVector: np.ndarray, timePeriod: int) -> None:
        self.envModel = Env(naturalResources=naturalResources, personList=personList, unitList=unitList, map=map, priceVector=priceVector, timePeriod=timePeriod)
        self.taskModel = TaskQueue(self.envModel)
    def exec(self):
        pass
        # todo load task
        targetList = [Task.Target(unitId=1, product=np.array([1,0,0,0,0]))]
        self.taskModel.addTask(Task(endtime=3,targets=targetList))
        while(True):
            self.taskModel.settleATask()

# 以下放到 main 或配置文件初始化

priceVecotr = np.array([1, 2, 3, 4, 5])
naturalResources = np.array([1,1,0,0,0])

person0 = Person(id=0, inventory=[0,0,0,0,0])
person1 = Person(id=1, inventory=[0,0,0,0,0])
person2 = Person(id=1, inventory=[0,0,0,0,0])
personList = [person0, person1, person2]

unit0 = Unit(id=0, name='factory', inventory=[5,5,5,5,5],personList=[person0, person1])
unit1 = Unit(id=1, name='community', inventory=[0,0,0,0,0], personList=[person0, person1, person2])
unitList = [unit0, unit1]

map = MapGraph(size=len(unitList), priceVectorSize=len(priceVecotr))
map.addEdge(fromEnd=0, toEnd=1, cost=[1,1,1,1,1])
map.floyd_algorithm()

timePeriod = 365

engine = PTEngine(naturalResources=naturalResources, personList=personList, unitList=unitList, map=map, priceVector=priceVecotr, timePeriod=timePeriod)
engine.exec()