import unittest

from src import DiGraph


class TestGraph(unittest.TestCase):

    @staticmethod
    def createGraph():
        graph = DiGraph.DiGraph()
        for i in range(0, 5):
            graph.add_node(i, (0, 0, 0))

        graph.add_edge(0, 4, 4)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 4, 12)
        graph.add_edge(4, 1, 1)
        graph.add_edge(2, 1, 10)
        graph.add_edge(3, 2, 8)

        return graph

    def test_add_edge_test(self):
        graph = self.createGraph()
        self.assertEqual(graph.get_mc(), 11)

        self.assertEqual(graph.e_size(), 6)
        graph.add_edge(0, 4, 4)
        self.assertEqual(graph.e_size(), 6)
        graph.add_edge(3, 0, 2)
        graph.add_edge(3, 4, 6)
        self.assertEqual(graph.e_size(), 8)
        self.assertEqual(graph.get_mc(), 13)

    def test_remove_edge_test(self):
        graph = self.createGraph()
        res = graph.all_out_edges_of_node(3).get(2)
        self.assertEqual(res, 8)
        graph.remove_edge(3, 2)
        self.assertEqual(graph.e_size(), 5)
        res = graph.all_out_edges_of_node(3).get(2)
        self.assertEqual(res, None)

        graph.remove_edge(2, 2)
        self.assertEqual(graph.e_size(), 5)
        graph.remove_edge(3, 2)
        self.assertEqual(graph.e_size(), 5)

        res = graph.all_out_edges_of_node(1).get(4)
        self.assertEqual(res, 12)
        graph.remove_edge(1, 4)
        self.assertEqual(graph.e_size(), 4)
        res = graph.all_out_edges_of_node(1).get(4)
        self.assertEqual(res, None)
        self.assertEqual(graph.get_mc(), 13)

    def test_remove_node(self):
        graph = self.createGraph()
        graph.remove_node(2)
        self.assertEqual(graph.e_size(), 3)
        self.assertEqual(graph.v_size(), 4)
        graph.remove_node(10)
        self.assertEqual(graph.get_mc(), 12)
        graph.remove_node(3)
        self.assertEqual(graph.get_mc(), 13)
        graph.remove_node(3)
        graph.remove_node(10)
        self.assertEqual(graph.get_mc(), 13)

    def test_add_node(self):
        graph = self.createGraph()
        graph.add_node(6, (1, 2, 2))
        graph.add_node(7, (1, 2, 2))
        self.assertEqual(graph.v_size(), 7)
        self.assertEqual(graph.get_mc(), 13)

    def test_empty_graph(self):
        graph = DiGraph.DiGraph()
        graph.remove_node(10)
        self.assertEqual(graph.get_mc(), 0)
        graph.add_edge(0, 8, 10)
        graph.add_edge(8, 8, 10)

        self.assertEqual(graph.get_mc(), 0)
        graph.remove_edge(3, 10)
