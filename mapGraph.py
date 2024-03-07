import numpy as np


class mapGraph:
    
    class Node:
        id: int
        name: str
        def __init__(self, id: int, name: str) -> None:
            self.id = id
            self.name = name
    
    nodes: list[Node]
    costs: np.ndarray[np.ndarray[np.ndarray]]
    
    def __init__(self) -> None:
        pass

    def addNode(self, name: str):
        self.nodes.append(id = self.Node(len(self.nodes), name = name))

    def floyd_algorithm(self):
        n = len(self.nodes)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.costs[i][j] > self.costs[i][k] + self.costs[k][j] :
                        self.costs[i][j] = self.costs[i][k] + self.costs[k][j]