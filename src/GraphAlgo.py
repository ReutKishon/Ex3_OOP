from abc import ABC

from src import GraphInterface
from src import GraphAlgoInterface
from jsonEncoders import graphEncoder
import json


class GraphALgo(GraphAlgoInterface.GraphAlgoInterface, ABC):

    def __init__(self, graph: GraphInterface = GraphInterface):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self._nodes) or not (id2 in self._nodes):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]

    # def load_from_json(self, file_name: str):
    #
    #

    def save_to_json(self, file_name: str):
        with open(file_name, 'w') as f:
            json.dump(self.graph, f, cls=graphEncoder.GraphEncoder, indent=4)
