from typing import Dict, List
import numpy as np
import functools
class Unit:
    id: int
    name: str
    triggers: Dict[str, np.ufunc]
    inventory: np.ndarray
    personList: List[int]
    
    def __init__(self, id: int, name: str, inventory: np.ndarray | list[float], personList: list[int]) -> None:
        self.id = id
        self.name = name
        self.inventory = np.array(inventory) if isinstance(inventory,list) else inventory
        self.personList = personList
        self.triggers = {}
    
    def setTrigger(self, name, func) -> any:
        self.triggers[name] = np.frompyfunc(functools.partial(func, self), 1, 1)