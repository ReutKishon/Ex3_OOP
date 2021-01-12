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
        self.dijkstra(id1, id2, prev)
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

    def dijkstra(self, src: int, dest: int,  prev: dict):
        visited = {k: False for k in self.graph.get_all_v().keys()}
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
            if rm.key == dest:
                return
            visited[rm.key] = True
            if self.graph.all_out_edges_of_node(rm.key) is not None:
                for neighbor, weighted in self.graph.all_out_edges_of_node(rm.key).items():
                    node_neighbor = self.graph.get_all_v().get(neighbor)
                    if visited[node_neighbor.key] is False:
                        dist = rm.tag + weighted
                        if dist < node_neighbor.tag:
                            node_neighbor.tag = dist
                            prev[neighbor] = rm
                            hq.heappush(nodes, node_neighbor)

    def connected_component(self, id1: int) -> list:
        if id1 not in self.graph.get_all_v().keys():
            return []
        cc = self.bfs(id1)
        cc_reverse = self.graph_reverse(id1)

        scc = []
        for n in cc:
            if n in cc_reverse:
                scc.append(n)
        return scc

    def connected_components(self) -> List[list]:
        if self.graph is None or self.graph.get_all_v() is None:
            return []
        scc = []
        seen = {k: False for k in self.graph.get_all_v().keys()}
        for i in self.graph.get_all_v().keys():
            if seen[i] is False:
                path = self.connected_component(i)
                for k in path:
                    seen[k] = True
                scc.append(path)
        return scc

    def bfs(self, src: int) -> list:
        scc = []
        q = [src]
        visited = {k: False for k in self.graph.get_all_v().keys()}
        visited[src] = True
        while q:
            rm = q.pop(0)
            if self.graph.all_out_edges_of_node(rm) is not None:
                for n in self.graph.all_out_edges_of_node(rm).keys():
                    if visited[n] is False:
                        visited[n] = True
                        q.append(n)
            scc.append(rm)
        return scc

    def graph_reverse(self, src: int) -> list:
        scc = []
        q = [src]
        visited = {k: False for k in self.graph.get_all_v().keys()}
        visited[src] = True
        while q:
            rm = q.pop(0)
            if self.graph.all_in_edges_of_node(rm) is not None:
                for n in self.graph.all_in_edges_of_node(rm).keys():
                    if visited[n] is False:
                        visited[n] = True
                        q.append(n)
            scc.append(rm)
        return scc

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
                if 'pos' in node:
                    graph_result.add_node(node['id'], eval(node['pos']))
                else:
                    graph_result.add_node(node['id'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj

    def plot_graph(self) -> None:
        x = []
        y = []
        z = []
        for i, n in self.graph.get_all_v().items():
            x.append(n.pos[0])
            y.append(n.pos[1])
            z.append(n.pos[2])
        plt.plot(x, y, "o")
        for i, n in self.graph.get_all_v().items():
            if self.graph.all_out_edges_of_node(i) is not None:
                for j in self.graph.all_out_edges_of_node(i).keys():
                    d = self.graph.get_all_v().get(j)
                    plt.arrow(n.pos[0], n.pos[1], d.pos[0]-n.pos[0], d.pos[1]-n.pos[1])
        plt.show()
