import numpy as np
import functools

class Unit:
    name: str
    produceTrigger: np.ufunc
    inventory: np.ndarray
    personList: np.ndarray
    
    def __init__(self, name: str, inventory: np.ndarray, personList: np.ndarray) -> None:
        self.name = name
        self.inventory = inventory
        self.personList = personList
        self.produceTrigger = None
    
    def setProduceTrigger(self, func):
        self.produceTrigger = np.frompyfunc(functools.partial(func, self), 1, 1)
