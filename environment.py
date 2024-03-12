import numpy as np
from mapGraph import MapGraph

from person import Person
from unit import Unit

class Env:
    naturalResources: np.ndarray
    naturalResourcesInventory: np.ndarray
    personList: list[Person]
    unitList: list[Unit]
    map: MapGraph
    priceVector: np.ndarray
    timePeriod: int
    time: int

    def __init__(self, naturalResources: np.ndarray, personList: list[Person], unitList: list[Unit], map: MapGraph, priceVector: np.ndarray, timePeriod: int) -> None:
        self.naturalResources = naturalResources
        self.naturalResourcesInventory = naturalResources
        self.personList = personList
        self.unitList = unitList
        self.map = map
        self.priceVector = priceVector
        self.timePeriod = timePeriod
        self.time = 0

    def setTime(self, time: int):
        self.time = time