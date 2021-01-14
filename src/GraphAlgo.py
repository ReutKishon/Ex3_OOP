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
    """
    This class implements GraphAlgoInterface.
    It represents a Directed Weighted Graph Theory algorithms.
    """

    def __init__(self, graph: DiGraph = None):
        """ Constructor. """
        self.__graph = graph

    def __ceil__(self):
        print('called')

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from given node id1 to given node id2. using Dijkstra's Algorithm.
        @param id1: The source node id.
        @param id2: The destination node id.
        @return: The distance of the path (infinite if None),
                 a list of the nodes ids that the path goes through (empty list if None).
        """
        if not (id1 in self.__graph.get_all_v().keys()) or not (id2 in self.__graph.get_all_v().keys()):
            return float('inf'), []
        if id1 == id2:
            return 0.0, [id1]
        prev = {k: None for k in self.__graph.get_all_v().keys()}
        self.dijkstra(id1, id2, prev)
        if self.__graph.get_all_v().get(id2).get_tag() is float('inf'):
            return float('inf'), []
        path = []
        if prev.get(id2) is not None:
            path.insert(0, id2)
            node0 = prev.get(id2).get_key()
            while node0 != id1:
                path.insert(0, node0)
                node0 = prev.get(node0).get_key()
            path.insert(0, node0)
        return self.__graph.get_all_v().get(id2).get_tag(), path

    def dijkstra(self, src: int, dest: int, prev: dict):
        """
        Implements the Dijkstra's algorithm.
        Dijkstra is an algorithm for finding the shortest paths between two nodes in a graph.
        """
        visited = {k: False for k in self.__graph.get_all_v().keys()}
        nodes = []
        for n in self.__graph.get_all_v().values():
            if n.get_key() == src:
                n.set_tag(0.0)
                nodes.append(n)
            else:
                n.set_tag(float('inf'))
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            if rm.get_key() == dest:
                return
            visited[rm.get_key()] = True
            if self.__graph.all_out_edges_of_node(rm.get_key()) is not None:
                for neighbor, weighted in self.__graph.all_out_edges_of_node(rm.get_key()).items():
                    node_neighbor = self.__graph.get_all_v().get(neighbor)
                    if visited[node_neighbor.get_key()] is False:
                        dist = rm.get_tag() + weighted
                        if dist < node_neighbor.get_tag():
                            node_neighbor.set_tag(dist)
                            prev[neighbor] = rm
                            hq.heappush(nodes, node_neighbor)

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that given node id1 is a part of. using BFS's algorithms.
        @param id1: The node id
        @return: The list of nodes in the SCC (empty list if the graph is None or if id1 isn't in the graph).
        """
        if id1 not in self.__graph.get_all_v().keys():
            return []
        cc = self.bfs(id1)
        cc_reverse = self.graph_reverse(id1)

        scc = []
        for n in cc:
            if n in cc_reverse:
                scc.append(n)
        return scc

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph. used BFS's algorithms.
        @return: The list of all SCC (empty list if the graph is None).
        """
        if self.__graph is None or self.__graph.get_all_v() is None:
            return []
        scc = []
        seen = {k: False for k in self.__graph.get_all_v().keys()}
        for i in self.__graph.get_all_v().keys():
            if seen[i] is False:
                path = self.connected_component(i)
                for k in path:
                    seen[k] = True
                scc.append(path)
        return scc

    def bfs(self, src: int) -> list:
        """
        Implements the BFS's algorithm.
        It's help to finding the Strongly Connected Component(SCC) of a node in the graph.
        """
        scc = []
        q = [src]
        visited = {k: False for k in self.__graph.get_all_v().keys()}
        visited[src] = True
        while q:
            rm = q.pop(0)
            if self.__graph.all_out_edges_of_node(rm) is not None:
                for n in self.__graph.all_out_edges_of_node(rm).keys():
                    if visited[n] is False:
                        visited[n] = True
                        q.append(n)
            scc.append(rm)
        return scc

    def graph_reverse(self, src: int) -> list:
        """
        Implements the BFS's algorithm on the graph revers.
        It's help to finding the Strongly Connected Component(SCC) of a node in the graph.
        """
        scc = []
        q = [src]
        visited = {k: False for k in self.__graph.get_all_v().keys()}
        visited[src] = True
        while q:
            rm = q.pop(0)
            if self.__graph.all_in_edges_of_node(rm) is not None:
                for n in self.__graph.all_in_edges_of_node(rm).keys():
                    if visited[n] is False:
                        visited[n] = True
                        q.append(n)
            scc.append(rm)
        return scc

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @return: True if the loading was successful, False if not.
        """
        try:
            with open(file_name) as complex_data:
                data = complex_data.read()
                self.__graph = json.loads(data, object_hook=self.deserialize_objects)
                return True
        except ValueError:
            print('Decoding JSON has failed')
            return False
        except IOError:
            print('not found')
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False if not.
        """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.__graph, f, cls=graphEncoder.GraphSerialize, indent=4)
                return True
        except TypeError:
            print("Unable to serialize the object")
            return False

        except IOError:
            print('not found')
            return False

    @staticmethod
    def deserialize_objects(obj):
        if 'Edges' in obj and 'Nodes' in obj:
            graph_result = DiGraph()

            for node in obj['Nodes']:
                if 'pos' in node:
                    graph_result.add_node(node['id'], eval(node['pos']) if type(node['pos']) is str else node['pos'])
                else:
                    graph_result.add_node(node['id'])

            for edge in obj['Edges']:
                graph_result.add_edge(edge['src'], edge['dest'], edge['w'])
            return graph_result

        return obj

    def plot_graph(self) -> None:
        """
        Plots the graph. using matplotlib library.
        """
        plt.title('Graph')
        random_poses = {}

        for node in self.__graph.get_all_v().values():
            if node.get_pos() is None:
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
                x = node.get_pos()[0]
                y = node.get_pos()[1]
                z = node.get_pos()[2]
                if x not in random_poses or y not in random_poses[x] or z not in random_poses[x][y]:
                    if x not in random_poses:
                        random_poses[x] = {}
                    if y not in random_poses[x]:
                        random_poses[x][y] = {}
                    if z not in random_poses[x][y]:
                        random_poses[x][y] = z

            plt.plot(x, y, 'ro')
            plt.annotate(node.get_key(),  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or center

        for node in self.__graph.get_all_v().values():
            if self.__graph.all_out_edges_of_node(node.get_key()) is not None:
                for dest in self.__graph.all_out_edges_of_node(node.get_key()).keys():
                    plt.annotate("",
                                 xy=(self.__graph.get_all_v()[dest].get_pos()[0],
                                     self.__graph.get_all_v().get(dest).get_pos()[1]), xycoords='data',
                                 xytext=(node.get_pos()[0], node.get_pos()[1]), textcoords='data',
                                 arrowprops=dict(arrowstyle="->",
                                                 color='blue',
                                                 connectionstyle="arc3"),
                                 )

        plt.show()
