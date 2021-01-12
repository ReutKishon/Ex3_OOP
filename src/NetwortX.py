import time
import timeit

import networkx as nx
from src.GraphAlgo import GraphAlgo


def loading_graph(file: str) -> nx:
    g_algo = GraphAlgo()
    g_algo.load_from_json(file)

    g = nx.DiGraph()
    g.add_nodes_from(g_algo.get_graph().get_all_v())
    for i in g_algo.get_graph().get_all_v().keys():
        if g_algo.get_graph().all_out_edges_of_node(i) is not None:
            for j, w in g_algo.get_graph().all_out_edges_of_node(i).items():
                g.add_edge(i, j, weight=w)

    return g


def check1():
    g = loading_graph('../data/G_10_80_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 8, 2))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


def check2():
    g = loading_graph('../data/G_100_800_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 13, 99))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


def check3():
    g = loading_graph('../data/G_1000_8000_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 135, 735))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


def check4():
    g = loading_graph('../data/G_10000_80000_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 5937, 2100))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


def check5():
    g = loading_graph('../data/G_20000_160000_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 493, 17500))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


def check6():
    g = loading_graph('../data/G_30000_240000_1.json')

    start1 = time.time()
    print(nx.dijkstra_path(g, 9, 25000))
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(nx.number_strongly_connected_components(g))
    end2 = time.time()
    print(end2 - start2)


if __name__ == '__main__':
    check6()
