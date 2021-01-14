from src import GraphInterface
from src import Node


class DiGraph(GraphInterface.GraphInterface):
    """
    This class implements GraphInterface.
    It represents a directed weighted graph.
    """

    def __init__(self):
        """ Constructor """
        self.__nodes = {}
        self.__outEdges = {}  # all the edges that started from key
        self.__inEdges = {}  # all the edges that ended with key
        self.__edgesCount = 0
        self.__mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.__nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edgesCount

    def get_all_v(self) -> dict:
        """
        Returns a dictionary of all the nodes in the Graph.
        Each node is represented using a pair (node_id, node_data).
        @return: dictionary of all the nodes in the Graph.
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary of all the nodes connected to (into) the node with id1 key.
        Each node is represented using a pair (other_node_id, weight).
        @param id1: the node_id destination of all the edges which the method returns.
        @return: dictionary of all the nodes connected to (into) the node with id1 key.
        """
        if id1 in self.__inEdges:
            return self.__inEdges[id1]
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary of all the nodes connected from the node with id1 key.
        Each node is represented using a pair (other_node_id, weight).
        @param id1: the node_id source of all the edges which the method returns.
        @return: dictionary of all the nodes connected from the node with id1 key.
        """
        if id1 in self.__outEdges:
            return self.__outEdges[id1]
        return {}

    def get_mc(self) -> int:
        """
        Returns the current version of this graph.
        @return: number of the changes made to the graph.
        """
        return self.__mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node_id.
        @param pos: The position of the node.
        @return: True if the node was added successfully, False if not.
        """
        if not (node_id in self.__nodes):
            new_node = Node.Node(node_id, pos)
            self.__nodes[node_id] = new_node
            self.__mc += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The source node of the edge.
        @param id2: The destination node of the edge.
        @param weight: The weight of the edge.
        @return: True if the edge was added successfully, False if not.
        """
        if not (id1 in self.__nodes) or not (id2 in self.__nodes):
            return False
        if id1 == id2:
            return False

        if id1 in self.__outEdges and id2 in self.__outEdges[id1]:
            return False

        if not (id1 in self.__outEdges):
            self.__outEdges[id1] = {}
        if not (id2 in self.__inEdges):
            self.__inEdges[id2] = {}

        self.__outEdges[id1][id2] = weight
        self.__inEdges[id2][id1] = weight
        self.__edgesCount += 1
        self.__mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node_id to remove.
        @return: True if the node was removed successfully, False if not.
        """
        if node_id not in self.__nodes:
            return False
        self.__mc += 1
        if node_id in self.__outEdges:
            for dest in self.__outEdges[node_id]:
                del self.__inEdges[dest][node_id]
                self.__edgesCount -= 1
            del self.__outEdges[node_id]
        if node_id in self.__inEdges:
            for src in self.__inEdges[node_id]:
                del self.__outEdges[src][node_id]
                self.__edgesCount -= 1
            del self.__inEdges[node_id]

        del self.__nodes[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The source node of the edge.
        @param node_id2: The destination node of the edge
        @return: True if the edge was removed successfully, False if not.
        """
        if node_id1 in self.__outEdges and node_id2 in self.__outEdges[node_id1]:
            del self.__outEdges[node_id1][node_id2]
            del self.__inEdges[node_id2][node_id1]
            self.__edgesCount -= 1
            self.__mc += 1
            return True
        return False

    def __eq__(self, other):
        """
        Equals between to graphs.
        """
        if isinstance(other, DiGraph):
            if self.e_size() != other.e_size() or self.v_size() != other.v_size():
                return False

        for node in self.__nodes:
            v = other.get_all_v()[node]
            if v is None:
                return False
            else:
                if self.__nodes[node].get_pos() is not None and v.get_pos() is not None:
                    if self.__nodes[node].get_pos()[0] != v.get_pos()[0] or self.__nodes[node].get_pos()[1] != \
                            v.get_pos()[1]:
                        return False
            for neighbor in self.all_out_edges_of_node(node).keys():
                if other.get_all_v().get(neighbor) is None:
                    return False
                if self.all_out_edges_of_node(node).get(neighbor) != other.all_out_edges_of_node(node).get(
                        neighbor):
                    return False

        return True
