import numpy as np

class MapGraph:

    costs: np.ndarray[np.ndarray[np.ndarray]]
    size: int
    def __init__(self, size: int, priceVectorSize: int) -> None:
        self.size = size
        self.costs = np.zeros((size, size, priceVectorSize), dtype=np.ndarray)
        pass

    def addEdge(self, fromEnd: int, toEnd: int, cost: np.ndarray):
        self.costs[fromEnd][toEnd] = self.costs[toEnd][fromEnd] = cost

    def getCost(self, fromEnd: int, toEnd: int):
        return self.costs[fromEnd][toEnd]

    def floyd_algorithm(self):
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    # todo 路径花费偏序关系
                    if np.linalg.norm(self.costs[i][j]) > np.linalg.norm(self.costs[i][k] + self.costs[k][j]) :
                        self.costs[i][j] = self.costs[i][k] + self.costs[k][j]