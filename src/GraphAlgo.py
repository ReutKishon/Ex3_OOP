from abc import ABC
import heapq as hq

from src import GraphInterface
from src import GraphAlgoInterface

class GraphALgo(GraphAlgoInterface.GraphAlgoInterface, ABC):

    def __init__(self, graph: GraphInterface = GraphInterface):
        self.graph = graph

    def __ceil__(self):
        print('called')

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self.graph.) or not (id2 in self._nodes):
            return (float('inf'), [])
        if id1 == id2:
            return (0.0, [id1])
        self.Dijkstra(id1)

    def Dijkstra(self, id: int):
        seen = []
        nodes = []
        for k, n in self.graph.get_all_v:
            nodes.append(n)
        for n in nodes:
            if n.key == id:
                n.tag = 0.0
            else:
                n.tag = float('inf')
        hq.heapify(nodes)
        while nodes:
            rm = hq.heappop(nodes)
            seen.append(rm)
            for neighbor, weighted in self.graph.all_out_edges_of_node(id):
                if neighbor not in seen:
                    dist = rm.tag + weighted
                    if dist < neighbor.tag:
                        neighbor.tag = dist
                        hq.heappush(nodes, neighbor)

        """
      while(!q.isEmpty()) {
         node_data rm= q.poll();
         for(edge_data edge: g.getE(rm.getKey())) {
            if(g.getNode(edge.getDest()).getInfo().equals("unvisited")) {
               double weight= g.getEdge(rm.getKey(), edge.getDest()).getWeight();
               double path= ((NodeData)rm).dist+weight;
               if(((NodeData)g.getNode(edge.getDest())).dist > path) {
                  q.remove(g.getNode(edge.getDest()));
                  ((NodeData)g.getNode(edge.getDest())).dist = path;
                  ((NodeData)g.getNode(edge.getDest())).prev = rm;
                  q.add(g.getNode(edge.getDest()));
               }
            }
         }
         rm.setInfo("visited");
      }
        """
