class Node:
    """This class represents vertex in graph."""

    def __init__(self, key: int, pos: tuple = None):
        """ Constructor. """
        self.__key = key
        self.__tag = 0
        self.__pos = pos

    def __call__(self):
        print('called')

    def get_key(self) -> int:
        """
        Returns the node_id.
        @return: the node_id
        """
        return self.__key

    def get_tag(self) -> float:
        """
        Returns temporal data which can be used by algorithms.
        @return: node_tag
        """
        return self.__tag

    def get_pos(self) -> tuple:
        """
        Returns the position of the node in the graph, if None return None.
        @return: the position of this node.
        """
        return self.__pos

    def set_tag(self, t: float):
        """
        Allows setting the "tag" value for temporal marking an node-
        common practice for marking by algorithms.
        @param t: the new value of the tag
        """
        self.__tag = t

    def set_pos(self, pos: tuple):
        """
        If this node's pos is None,
        this method given pos to the node, which be used by plot method.
        @param pos: the mew pos of the node
        """
        self.__pos = pos

    def __lt__(self, other):
        return self.get_tag() < other.get_tag()
