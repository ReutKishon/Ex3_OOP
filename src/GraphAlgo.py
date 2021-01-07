import heapq as hq
from typing import List

from src.GraphInterface import GraphInterface
from src import GraphAlgoInterface
from jsonEncoders import graphEncoder
import json

from src.DiGraph import DiGraph


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
        if id1 not in self.graph.get_all_v():
            return []
        visited = []
        stack = []
        self.dfs(self.graph, id1, visited, stack)
        graph_revers = GraphInterface()
        for i in stack:
            for neighbor, w in self.graph.all_in_edges_of_node(i):
                graph_revers.add_edge(neighbor.key, i, w)
        self.dfs(graph_revers, id1, visited, stack)
        return stack

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        scc = []
        nodes = self.graph.get_all_v()
        for i, n in nodes:
            if i not in scc:
                path = self.connected_component(i)
                scc.append(path)
        return scc

    @staticmethod
    def dfs(graph: GraphInterface, src: int, visited: list, stack: list):
        for n, w in graph.all_out_edges_of_node(src):
            if n.key not in visited:
                GraphALgo.dfs(n.key, visited, stack)
        stack.insert(0, src)

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