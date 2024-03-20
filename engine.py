import numpy as np
from typing import Tuple
import queue

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
        
class PTEngine:
    naturalResources: np.ndarray
    naturalResourcesInventory: np.ndarray
    personList: list[Person]
    unitList: list[Unit]
    map: MapGraph
    priceVector: np.ndarray
    timePeriod: int
    time: int

    taskQueue: queue.PriorityQueue[Tuple[int, Task]]

    def __init__(self, naturalResources: np.ndarray, personList: list[Person], unitList: list[Unit], map: MapGraph, priceVector: np.ndarray, timePeriod: int) -> None:
        self.naturalResources = naturalResources
        self.naturalResourcesInventory = naturalResources
        self.personList = personList
        self.unitList = unitList
        self.map = map
        self.priceVector = priceVector
        self.timePeriod = timePeriod
        self.time = 0
        self.taskQueue = queue.PriorityQueue()
    
    def setTime(self, time: int):
        self.time = time

    def addTask(self, task: Task):
        self.taskQueue.put((task.endtime, task))
    
    def settleATask(self):
        cEndtime, cTask = self.taskQueue.get()
        for t in cTask.targets:
            newTask: Task = self.unitList[t.unitId].triggers[' ']()
            newTask.endtime += self.time # 校准时钟
            if newTask:
                self.addTask(newTask)
        self.setTime(cEndtime)

    def exec(self):
        pass
        # todo load task
        targetList = [Task.Target(unitId=1, product=np.array([1,0,0,0,0]))]
        self.addTask(Task(endtime=3,targets=targetList))
        while(True):
            self.settleATask()

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