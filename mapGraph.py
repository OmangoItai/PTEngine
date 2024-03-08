import numpy as np

class MapGraph:

    costs: np.ndarray[np.ndarray[np.ndarray]]
    
    def __init__(self, MapSize: int, priceVectorSize: int) -> None:
        self.costs = np.zeros((MapSize, MapSize, priceVectorSize), dtype=np.ndarray)
        pass

    def addEdge(self, fromEnd: int, toEnd: int, cost: np.ndarray):
        self.costs[fromEnd][toEnd] = self.costs[toEnd][fromEnd] = cost

    def getCost(self, fromEnd: int, toEnd: int):
        return self.costs[fromEnd][toEnd]

    def floyd_algorithm(self):
        n = len(self.nodes)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.costs[i][j] > self.costs[i][k] + self.costs[k][j] :
                        self.costs[i][j] = self.costs[i][k] + self.costs[k][j]