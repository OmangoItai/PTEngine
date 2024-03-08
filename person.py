import numpy as np

class Person:
    id: int
    name: str
    inventory: np.ndarray
    
    def __init__(self, id: int, inventory: np.ndarray | list[float]) -> None:
        self.id = id
        self.inventory = np.array(inventory) if isinstance(inventory,list) else inventory