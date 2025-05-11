import sys
from collections import defaultdict
import heapq


"""
This file contains all code related to Q1 and Q2.
"""


#
#   Graph
#

# Graph class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    # This method is for MST only
    def initializeDistances(self):
        for i in self.nodes:
            for j in self.nodes:
                self.distances[(i, j)] = sys.maxsize

        for i in self.nodes:
            self.distances[(i, "")] = 0

    # Prim's algorithm for Q2
    def Prim( self, start ):
        # variables
        visited = set() # track visited nodes
        Prim_edges = [] #
        total_cost = 0  #
        min_heap = [ (0, start, None) ] # weight, current, prev

        # 
        while min_heap and len( visited ) < len( self.nodes ):
            weight, current, prev = heapq.heappop( min_heap )

            # if node has been visited already, skip
            if current in visited:
                continue

            # update visited
            visited.add( current )

            # if current node has a previous, add it to Prim edges and update total cost
            if prev is not None:
                Prim_edges.append( (prev, current, weight)  )
                total_cost += weight

            # for neighbors of current
            for neighbor in self.edges[ current ]:
                # if the neighbor hasn't been visited, get the edge cost (infinity if none) and add it to the min heap
                if neighbor not in visited:
                    edge_weight = self.distances.get( (current, neighbor), sys.maxsize )
                    heapq.heappush( min_heap, (edge_weight, neighbor, current) )

            print( f'{current} is selected. Distance: {weight}' )
            
        # if after going through all reachable nodes and visited is less than the number of nodes, it is not fully connected
        if len( visited ) < len( self.nodes ):
            print("Graph is not fully connected. MST cannot reach all nodes.")
            return None
        
        return Prim_edges, total_cost


# Build graph
def build_graph( nodes, edges ):
    # initialize graph
    my_graph = Graph( )

    # add nodes
    for node in nodes:
        my_graph.add_node( node )

    # add edges
    for edge in edges:
        my_graph.add_edge( *edge )

    return my_graph
   


#
#   Dijkstra's
#
def Dijkstra( graph, start ):
    # variables
    visited = set()         # keep track of nodes visited excluding relaxation
    all_visited = set()     # keep track of nodes visited including relaxation
    distances = { node:float('inf') for node in graph.nodes }   # keep track of mininum distances, unknowns are set to inf, start is set to 0
    distances[ start ] = 0
    paths = {}              # keep track of paths
    heap = [ (0, start) ]   # initialize starting node to weight 0
    nodes = graph.nodes

    # while there are still nodes remaining
    while heap:
        # get current weight and node of smallest node in min heap
        current_weight, current_node = heapq.heappop( heap )
        
        # if node has been visited, skip it
        if current_node in visited:
           continue
        visited.add( current_node )         # update visited
        all_visited.add( current_node )     # update all visited
        print( f'\nNode( {current_node} ) with Weight( {current_weight} ) is added to the Visited( {all_visited} )' )   # print message when checking a node
        
        # relax neighbors if needed
        for neighbor in graph.edges[ current_node ]:
            all_visited.add( neighbor )         # update all visited
            weight = graph.distances[( current_node, neighbor )]
            distance = current_weight + weight
           
            if distance < distances[ neighbor ]:
                distances[ neighbor ] = distance
                paths[ neighbor ] = current_node    # update paths
                heapq.heappush( heap, (distance, neighbor) )
                print( f'    Relaxed: vertex( {neighbor} ): Old ( {distances[neighbor]} ), New ( {distance} ), Paths {paths}' )

            else:
               print( f'    No edge relaxation is needed for Node( {neighbor} )' )

        # if node has no neighbors, display message
        if not graph.edges[current_node]:
            print( f'    No unvisited outgoing edge from Node( {current_node} )' )

    return distances, paths


#
#   rebuild shortest paths from Dijkstra's
#
def rebuild_paths_Dijkstra( paths, distances, start, end ):
    path = []
    current = end

    while current != start:
        path.append( current )
        current = paths.get( current )  # return none if key not present

        # if key not present, no path exists
        if current is None:
            return []

    path.append( start )
    return path[ ::-1 ], distances[ end ]