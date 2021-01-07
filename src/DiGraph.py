from src import GraphInterface
from src import Node
from src import Edge


class DiGraph(GraphInterface.GraphInterface):

    def __init__(self):
        self._nodes = {}
        self._outEdges = {}  # all the edges that started from key
        self._inEdges = {}  # all the edges that ended with key
        self._edgesCount = 0
        self._mc = 0

    def v_size(self) -> int:
        return len(self._nodes)

    def e_size(self) -> int:
        return self._edgesCount

    def get_all_v(self) -> dict:
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self._inEdges:
            return self._inEdges[id1]
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self._outEdges:
            return self._outEdges[id1]
        return None

    def get_mc(self) -> int:
        return self._mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not (node_id in self._nodes):
            new_node = Node.Node(node_id, pos)
            self._nodes[node_id] = new_node
            self._mc += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not (id1 in self._nodes) or not (id2 in self._nodes):
            return False
        if id1 == id2:
            return False

        if id1 in self._outEdges and id2 in self._outEdges[id1]:
            return False

        if not (id1 in self._outEdges):
            self._outEdges[id1] = {}
        if not (id2 in self._inEdges):
            self._inEdges[id2] = {}

        self._outEdges[id1][id2] = weight
        self._inEdges[id2][id1] = weight
        self._edgesCount += 1
        self._mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
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

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self._outEdges and node_id2 in self._outEdges[node_id1]:
            del self._outEdges[node_id1][node_id2]
            del self._inEdges[node_id2][node_id1]
            self._edgesCount -= 1
            self._mc += 1
            return True
        return False
