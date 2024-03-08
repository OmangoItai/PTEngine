import numpy as np
import environment, mapGraph, person, taskQueue, unit

class Simulator:
    env: environment.Env
    def __init__(self, naturalResources: np.ndarray, personList: list[person.Person], unitList: list[unit.Unit], priceVector: np.ndarray, timePeriod: int) -> None:
        
        self.env = environment.Env(naturalResources=naturalResources, personList=personList, unitList=unitList, map=map, priceVector=priceVector, timePeriod=timePeriod)
        
        self.taskQueue = taskQueue.TaskQueue(self.env)
    def exec(self):
        pass
        targetList = [taskQueue.Task.Target(unitId=1, product=np.array([1,0,0,0,0]))]
        self.taskQueue.addTask(taskQueue.Task(endtime=3,targets=targetList))
        while(True):
            self.taskQueue.settleATask()

# 以下放到 main 或配置文件初始化

priceVecotr = np.array([1, 2, 3, 4, 5])
naturalResources = np.array([1,1,0,0,0])

person0 = person.Person(id=0, inventory=[0,0,0,0,0])
person1 = person.Person(id=1, inventory=[0,0,0,0,0])
person2 = person.Person(id=1, inventory=[0,0,0,0,0])
personList = [person0, person1, person2]

unit0 = unit.Unit(id=0, name='factory', inventory=[5,5,5,5,5],personList=[person0, person1])
unit1 = unit.Unit(id=1, name='community', inventory=[0,0,0,0,0], personList=[person0, person1, person2])

unitList = [unit0, unit1]

map = mapGraph.MapGraph(MapSize=len(unitList), priceVectorSize=len(priceVecotr))
map.addEdge(fromEnd=0, toEnd=1, cost=[1,1,1,1,1])
map.floyd_algorithm()

timePeriod = 365

simulator = Simulator(naturalResources=naturalResources, personList=personList, unitList=unitList, priceVector=priceVecotr, timePeriod=timePeriod)
simulator.exec()