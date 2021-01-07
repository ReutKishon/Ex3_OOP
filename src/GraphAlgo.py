import heapq as hq

from src.GraphInterface import GraphInterface
from src import GraphAlgoInterface
from jsonEncoders import graphEncoder
import json


class GraphALgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = GraphInterface()):
        self.graph = graph

    def __ceil__(self):
        print('called')

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self.graph.get_all_v()) or not (id2 in self.graph.get_all_v()):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        prev = {k:None for k in self.graph.get_all_v()}
        self.dijkstra(id1, prev)
        if self.graph.get_all_v().get(id2).tag is float('inf'):
            return float('inf'), []
        path = [id2]
        node0 = prev.get(id2).key
        while node0 != id1:
            path.insert(0, node0)
            node0 = prev.get(node0).key
        path.insert(0, node0)
        return self.graph.get_all_v().get(id2).tag, path

    def dijkstra(self, src: int, prev: dict):
        seen = []
        nodes = []
        for k, n in self.graph.get_all_v():
            nodes.append(n)
        for n in nodes:
            if n.key == src:
                n.tag = 0.0
            else:
                n.tag = float('inf')
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            seen.append(rm)
            for neighbor, weighted in self.graph.all_out_edges_of_node(rm):
                if neighbor not in seen:
                    dist = rm.tag + weighted
                    if dist < neighbor.tag:
                        neighbor.tag = dist
                        prev[neighbor.key] = rm
                        hq.heappush(nodes, neighbor)

    def connected_component(self, id1: int) -> list:
        pass

    def save_to_json(self, file_name: str):
        with open(file_name, 'w') as f:
            json.dump(self.graph, f, cls=graphEncoder.GraphEncoder, indent=4)

