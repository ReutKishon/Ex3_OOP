# Ex3

Our project is about directed weighted graph implementation, and a list of algorithms that operate on graphs.

**Definition of directed weighted graph**:
a directed graph is a graph that is made up of a set of vertices connected by edges, where the edges have a direction
associated with them. And weights assigned to their arrows

### Part 1:

**Graph implementation**

The nodes in the graph are represented by Node class.   
The graph implementation and functionality is in Digraph class
which implements the GraphInterface

### Part 2:

**Algorithms:**   
GraphAlgo implements GraphAlgoInterface.   
The algorithms we were required to implement are:

* shortest_path: finds the distance of the shortest path from node id1 to node id2 using Dijkstra's Algorithm
* connected_component: finds the Strongly Connected Component (SCC) that node id1 is a part of.
* connected_components: finds all the Strongly Connected Component (SCC) in the graph.
* save_to_json: saves the graph in JSON format to a file.
* load_from_json: loads a graph from a json file.
* plot_graph: plots the graph , a sketch of the graph.

examples of graph plot:
![graph1](/graph1.jpeg =100x20?raw=true "Optional Title")

<a href="url"><img src="/graph1.jpeg" align="left" height="70" width="70" ></a>

![graph2](/graph2.jpeg =100x20?raw=true "Optional Title")

