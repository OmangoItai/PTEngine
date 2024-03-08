import numpy as np
import functools

class Unit:
    id: int
    name: str
    produceTrigger: np.ufunc
    inventory: np.ndarray
    personList: list[int]
    # todo personList 是记编号还是引用
    
    def __init__(self, id: int, name: str, inventory: np.ndarray | list[float], personList: list[int]) -> None:
        self.id = id
        self.name = name
        self.inventory = np.array(inventory) if isinstance(inventory,list) else inventory
        self.personList = personList
        self.produceTrigger = None
    
    def setProduceTrigger(self, func):
        self.produceTrigger = np.frompyfunc(functools.partial(func, self), 1, 1)
