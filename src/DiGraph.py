from src import GraphInterface
from src import Node
import Edge


class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes = {}
        self._outEdges = {}  # all the edges that started from key
        self._inEdges = {}  # all the edges that ended with key
        self._edgesCount = 0
        self._mc = 0

    def v_size(self):
        return len(self._nodes)

    def e_size(self):
        return self._edgesCount

    def get_all_v(self):
        return self._nodes

    def all_in_edges_of_node(self, id1: int):
        return self._inEdges[id1]

    def all_out_edges_of_node(self, id1: int):
        return self._outEdges[id1]

    def get_mc(self):
        return self._mc

    def add_node(self, node_id: int, pos: tuple = None):
        if self._nodes[node_id] is not None:
            return False
        new_node = Node.Node(node_id, pos)
        self._nodes[node_id] = new_node
        self.mc += 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float):
        if self._nodes[id1] is None or self._nodes[id2] is None:
            return False
        if id1 == id2:
            return False

        if self._outEdges[id1][id2] is not None:
            return False
        new_edge = Edge.Edge(id1, id2, weight)
        self._outEdges[id1][id2] = new_edge
        self._inEdges[id2][id1] = new_edge

        self._edgesCount += 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int):
        if self._nodes[node_id] is None:
            return False
        self._mc += 1

        for dest in self._outEdges[node_id]:
            del self._inEdges[dest][node_id]
            self._edgesCount -= 1
            self._mc += 1

        for src in self._inEdges[node_id]:
            del self._outEdges[src][node_id]
            self._edgesCount -= 1
            self._mc += 1

        del self._outEdges[node_id]
        del self._inEdges[node_id]
        del self._nodes[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int):
        if self._outEdges[node_id1][node_id2] is None:
            return False
        del self._outEdges[node_id1][node_id2]
        del self._inEdges[node_id2][node_id1]
        self._edgesCount -= 1
        self._mc += 1
