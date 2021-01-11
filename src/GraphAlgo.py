import heapq as hq
from typing import List
from jsonEncoders import graphEncoder
import json

import matplotlib.pyplot as plt
import numpy as np

from src.GraphInterface import GraphInterface
from src import GraphAlgoInterface

from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface.GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def __ceil__(self):
        print('called')

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self.graph.get_all_v().keys()) or not (id2 in self.graph.get_all_v().keys()):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        prev = {k: None for k in self.graph.get_all_v().keys()}
        self.dijkstra(id1, prev)
        if self.graph.get_all_v().get(id2).tag is float('inf'):
            return float('inf'), []
        path = []
        if prev.get(id2) is not None:
            path.insert(0, id2)
            node0 = prev.get(id2).key
            while node0 != id1:
                path.insert(0, node0)
                node0 = prev.get(node0).key
            path.insert(0, node0)
        return self.graph.get_all_v().get(id2).tag, path

    def dijkstra(self, src: int, prev: dict):
        visited = []
        nodes = []
        for n in self.graph.get_all_v().values():
            if n.key == src:
                n.tag = 0.0
                nodes.append(n)
            else:
                n.tag = float('inf')
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            visited.append(rm)
            if self.graph.all_out_edges_of_node(rm.key) is not None:
                for neighbor, weighted in self.graph.all_out_edges_of_node(rm.key).items():
                    node_neighbor = self.graph.get_all_v().get(neighbor)
                    if node_neighbor not in visited:
                        dist = rm.tag + weighted
                        if dist < node_neighbor.tag:
                            node_neighbor.tag = dist
                            prev[neighbor] = rm
                            hq.heappush(nodes, node_neighbor)

    def connected_component(self, id1: int) -> list:
        if id1 not in self.graph.get_all_v().keys():
            return []
        scc = []
        self.bfs(self.graph, id1, scc)
        graph_revers = DiGraph()
        for i in scc:
            graph_revers.add_node(i)
        for i in scc:
            if self.graph.all_out_edges_of_node(i) is not None:
                for neighbor, w in self.graph.all_out_edges_of_node(i).items():
                    graph_revers.add_edge(neighbor, i, w)
        scc = []
        self.bfs(graph_revers, id1, scc)
        return scc

    def connected_components(self) -> List[list]:
        if self.graph is None or self.graph.get_all_v() is None:
            return []
        scc = []
        seen = []
        for i in self.graph.get_all_v().keys():
            if i not in seen:
                path = self.connected_component(i)
                seen += path
                scc.append(path)
        return scc

    @staticmethod
    def bfs(graph: GraphInterface, src: int, scc: list):
        q = [src]
        visited = [src]
        while q:
            rm = q.pop(0)
            if graph.all_out_edges_of_node(rm) is not None:
                for n in graph.all_out_edges_of_node(rm).keys():
                    if n not in visited:
                        visited.append(n)
                        q.append(n)
            scc.append(rm)

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
                if 'pos' in obj['Nodes']:
                    graph_result.add_node(node['id'], node['pos'])
                else:
                    graph_result.add_node(node['id'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj

    def plot_graph(self) -> None:
        x = []
        y = []
        for i, n in self.graph.get_all_v().items():
            x.append(n.pos[0])
            y.append(n.pos[1])
        plt.plot(x, y, "o")
        plt.show()


# if __name__ == '__main__':
#     g = DiGraph()
#     g.add_node(0, (1, 3, 0))
#     g.add_node(1, (2, 6, 0))
#     g.add_node(2, (3, 5, 0))
#     g.add_node(3, (5, 2, 0))
#     g.add_node(4, (9, 7, 0))
#     ga = GraphAlgo(graph=g)
#     ga.plot_graph()

