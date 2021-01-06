from abc import ABC

from src import GraphInterface
from src import GraphAlgoInterface

class GraphALgo(GraphAlgoInterface.GraphAlgoInterface, ABC):

    def __init__(self, graph: GraphInterface = GraphInterface()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self._nodes) or not (id2 in self._nodes):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        