import json
from src import DiGraph
from src import GraphInterface


class GraphSerialize(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, GraphInterface.GraphInterface):
            counter = 0
            edges_array = [dict() for x in range(o.e_size())]
            for src in o.get_all_v():
                out_edges = o.all_out_edges_of_node(src)
                if out_edges is not None:
                    for dest in out_edges:
                        edges_array[counter] = {}

                        edges_array[counter]['src'] = src
                        edges_array[counter]['w'] = o.all_out_edges_of_node(src).get(dest)
                        edges_array[counter]['dest'] = dest
                        counter += 1

            counter = 0
            nodes_array = [dict() for x in range(o.v_size())]
            for node in o.get_all_v():
                nodes_array[counter] = {}
                nodes_array[counter]['pos'] = o.get_all_v().get(node).pos
                nodes_array[counter]['id'] = node
                counter += 1

            return {'Edges': edges_array, 'Nodes': nodes_array}

        raise TypeError(f'object {o} is not of type Digraph')


class GraphDeserialize(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(dct):
        graph = DiGraph.DiGraph()
        if 'Nodes' in dct:
            for node in dct['Nodes']:
                graph.add_node(node.key)

        if 'Edges' in dct:
            for edge in dct['Edges']:
                src = edge['src']
                dest = edge['dest']
                weight = edge['w']
                graph.add_edge(src, dest, weight)
                return graph

        return dct
