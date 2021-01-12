import time

from src.GraphAlgo import GraphAlgo


def check1():
    g_algo = GraphAlgo()
    file = '../data/G_10_80_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(8, 2)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(9))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check2():
    g_algo = GraphAlgo()
    file = '../data/G_100_800_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(13, 99)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(54))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check3():
    g_algo = GraphAlgo()
    file = '../data/G_1000_8000_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(135, 732)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(825))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check4():
    g_algo = GraphAlgo()
    file = '../data/G_10000_80000_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(5937, 2100)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(3000))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check5():
    g_algo = GraphAlgo()
    file = '../data/G_20000_160000_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(493, 17500)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(900))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check6():
    g_algo = GraphAlgo()
    file = '../data/G_30000_240000_1.json'
    g_algo.load_from_json(file)
    start1 = time.time()
    dist, path = g_algo.shortest_path(9, 25000)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(g_algo.connected_component(20000))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(g_algo.connected_components())
    end3 = time.time()
    print(end3 - start3)


if __name__ == '__main__':
    # start = timeit.default_timer()
    check6()
    # end = timeit.default_timer()
    # print(end-start)
