from typing import Dict, List
import numpy as np
import functools
import taskQueue
class Entity:
    id: int
    name: str
    triggers: Dict[str: np.ufunc]
    inventory: np.ndarray
    personList: List[int]
    # todo personList 是记编号还是引用
    
    def __init__(self, id: int, name: str, inventory: np.ndarray | list[float], personList: list[int]) -> None:
        self.id = id
        self.name = name
        self.inventory = np.array(inventory) if isinstance(inventory,list) else inventory
        self.personList = personList
        self.produceTrigger = {}
    
    def setTrigger(self, name, func) -> taskQueue.Task:
        self.triggers[name] = np.frompyfunc(functools.partial(func, self), 1, 1)