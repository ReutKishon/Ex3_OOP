import heapq as hq
from typing import List

import ax as ax

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

    def dijkstra(self, src: int, dest: int, prev: dict):
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
            if rm.key == dest:
                return
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
                if 'pos' in node:
                    graph_result.add_node(node['id'], eval(node['pos']))
                else:
                    graph_result.add_node(node['id'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj

    def plot_graph(self) -> None:
        plt.title('Graph')
        random_poses = {}

        x = y = z = 0
        for node in self.graph.get_all_v().values():
            if node.pos is None:
                while True:
                    x_r = np.random.rand(1)
                    y_r = np.random.rand(1)
                    z_r = np.random.rand(1)
                    x = x_r[0]
                    y = y_r[0]
                    z = z_r[0]

                    if x not in random_poses or y not in random_poses[x] or z not in random_poses[x][y]:
                        if x not in random_poses:
                            random_poses[x] = {}
                        if y not in random_poses[x]:
                            random_poses[x][y] = {}
                        if z not in random_poses[x][y]:
                            random_poses[x][y] = z
                        node.set_pos((x, y, z))
                        break

            else:
                x = node.pos[0]
                y = node.pos[1]
                z = node.pos[2]
                if x not in random_poses or y not in random_poses[x] or z not in random_poses[x][y]:
                    if x not in random_poses:
                        random_poses[x] = {}
                    if y not in random_poses[x]:
                        random_poses[x][y] = {}
                    if z not in random_poses[x][y]:
                        random_poses[x][y] = z

            plt.plot(x, y, 'ro')
            plt.annotate(node.key,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center

        for node in self.graph.get_all_v().values():
            if self.graph.all_out_edges_of_node(node.key) is not None:
                for dest in self.graph.all_out_edges_of_node(node.key).keys():
                    plt.annotate("",
                                 xy=(self.graph.get_all_v()[dest].pos[0],
                                     self.graph.get_all_v().get(dest).pos[1]), xycoords='data',
                                 xytext=(node.pos[0], node.pos[1]), textcoords='data',
                                 arrowprops=dict(arrowstyle="->",
                                                 color='blue',
                                                 connectionstyle="arc3"),
                                 )

        plt.show()
