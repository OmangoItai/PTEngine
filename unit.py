import numpy as np
import functools
import taskQueue
class Unit:
    id: int
    name: str
    produceTrigger: np.ufunc
    consumeTrigger: np.ufunc
    inventory: np.ndarray
    personList: list[int]
    # todo personList 是记编号还是引用
    
    def __init__(self, id: int, name: str, inventory: np.ndarray | list[float], personList: list[int]) -> None:
        self.id = id
        self.name = name
        self.inventory = np.array(inventory) if isinstance(inventory,list) else inventory
        self.personList = personList
        self.produceTrigger = None
    
    def setProduceTrigger(self, func) -> taskQueue.Task:
        self.produceTrigger = np.frompyfunc(functools.partial(func, self), 1, 1)

    def setConsumeTrigger(self, func):
        self.consumeTrigger = np.frompyfunc(functools.partial(func, self), 1, 1)
