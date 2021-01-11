import unittest

from src.GraphAlgo import GraphALgo
from src.DiGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.g = DiGraph()
        for i in range(11):
            cls.g.add_node(i)

        cls.g.add_edge(0, 1, 3.0)
        cls.g.add_edge(1, 2, 2.0)
        cls.g.add_edge(0, 2, 1.0)
        cls.g.add_edge(2, 0, 1.0)
        cls.g.add_edge(2, 1, 1.0)
        cls.g.add_edge(3, 4, 7.0)
        cls.g.add_edge(4, 6, 3.0)
        cls.g.add_edge(6, 5, 2.0)
        cls.g.add_edge(5, 4, 1.0)
        cls.g.add_edge(3, 5, 5.0)
        cls.g.add_edge(4, 3, 1.0)
        cls.g.add_edge(9, 7, 2.0)
        cls.g.add_edge(8, 10, 1.0)
        cls.g.add_edge(7, 9, 7.0)
        cls.g.add_edge(10, 9, 3.0)
        cls.g.add_edge(10, 7, 9.0)
        cls.g.add_edge(7, 8, 2.0)
        cls.g.add_edge(2, 7, 3.0)
        cls.g.add_edge(1, 3, 18.0)
        cls.g.add_edge(9, 5, 2.0)

        cls.ga = GraphALgo(graph=cls.g)

    def test_shortest_path(self):
        spd = self.ga.shortest_path(1, 3)  # Path between 2 node that in the graph and connected.
        self.assertEqual(15.0, spd[0])
        sp = [1, 2, 7, 8, 10, 9, 5, 4, 3]
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(5, 0)  # Path between 2 node that in the graph and not connected.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(5, 12)  # Path between node in the graph to node that not in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(11, 7)  # Path between node that not in the graph to node in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(15, 12)  # Path between 2 node that not in the graph.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(4, 4)  # Path between node in the graph to himself.
        self.assertEqual(0.0, spd[0])
        sp = [4]
        self.assertEqual(sp, spd[1])

        spd = self.ga.shortest_path(18, 18)  # Path between node that not in the graph to himself.
        self.assertEqual(float('inf'), spd[0])
        sp = []
        self.assertEqual(sp, spd[1])

    def test_connected_component(self):
        scc1 = self.ga.connected_component(2)  # Node in the graph.
        except_scc1 = 3
        self.assertEqual(except_scc1, len(scc1))

        scc2 = self.ga.connected_component(5)  # Node in the graph.
        except_scc2 = 4
        self.assertEqual(except_scc2, len(scc2))

        scc3 = self.ga.connected_component(7)  # Node in the graph.
        except_scc3 = 4
        self.assertEqual(except_scc3, len(scc3))

        scc4 = self.ga.connected_component(13)  # Node that not in the graph.
        except_scc4 = 0
        self.assertEqual(except_scc4, len(scc4))

    def test_connected_components(self):
        list_scc = self.ga.connected_components()
        print(list_scc)
        num_scc1 = len(list_scc)  # graph with nodes.
        except_scc1 = 3
        self.assertEqual(except_scc1, num_scc1)

        ga2 = GraphALgo()
        num_scc2 = ga2.connected_components()  # The graph_algo is None.
        except_scc2 = []
        self.assertEqual(except_scc2, num_scc2)

        g2 = None
        ga2 = GraphALgo(g2)
        num_scc2 = ga2.connected_components()  # The graph is None.
        except_scc2 = []
        self.assertEqual(except_scc2, num_scc2)

        g2 = DiGraph()
        ga3 = GraphALgo(g2)
        num_scc3 = ga3.connected_components()  # Empty graph.
        except_scc3 = []
        self.assertEqual(except_scc3, num_scc3)

    def test_save_to_json(self):
        self.ga.save_to_json('graph.json')
        g_algo2 = GraphALgo()
        g_algo2.load_from_json('graph.json')
        self.assertEqual(self.ga.graph, g_algo2.graph)
