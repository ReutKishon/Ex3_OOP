from abc import ABC

from src import GraphInterface
from src import GraphAlgoInterface
from jsonEncoders import graphEncoder
import json

from src.DiGraph import DiGraph


class GraphALgo(GraphAlgoInterface.GraphAlgoInterface, ABC):

    def __init__(self, graph=None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self._nodes) or not (id2 in self._nodes):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]

    def load_from_json(self, file_name: str):
        with open(file_name) as complex_data:
            data = complex_data.read()
            self.graph = json.loads(data, object_hook=self.deserialize_objects)

    def save_to_json(self, file_name: str):
        with open(file_name, 'w') as f:
            json.dump(self.graph, f, cls=graphEncoder.GraphSerialize, indent=4)

    @staticmethod
    def deserialize_objects(obj):
        if 'Edges' in obj and 'Nodes' in obj:
            graph_result = DiGraph()

            for node in obj['Nodes']:
                graph_result.add_node(node['id'], node['pos'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj
