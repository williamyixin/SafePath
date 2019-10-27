from node import Node
from edge import Edge

class Algorithms:

    def __init__(self, main_frame):
        # William, format your functions like this

        def simple_dijkstra(start_node, end_node): #only returns the dictionary of distances so far

            # call "main_frame.highlight_node(node)" to highlight a node
            main_frame.highlight_node(start_node)

            # Actual Dijkstra's stuff
            node_list = Node.node_list.copy()
            distances, previous_nodes = {i : float('inf') for i in node_list}, {i : None for i in node_list}
            distances[start_node] = 0
            nodes = node_list.copy()
                    
            while nodes:
                current_node = min(nodes, key=lambda x: distances[x])
                if distances[current_node] == float('inf'):
                    break
                for neighbor in current_node.connections:
                    alternative = distances[current_node] + neighbor.end.weight
                    if alternative < distances[neighbor.end] and not neighbor.end.is_barrier:
                        distances[neighbor.end] = alternative
                        previous_nodes[neighbor.end] = current_node
                    main_frame.highlight_node(neighbor.end)
                nodes.remove(current_node)

            path, current_node = [], end_node
            while previous_nodes[current_node]:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            if path:
                path.insert(0, current_node)
            return path

        def bidirectional_dijkstra(start_node, end_node):
            return []

        def bellman_ford_path_gen(start_node, end_node):


            def bellman_ford(start_node, list_edges, list_nodes):
                #Initializing all the node labels except for the start node
                #as having infinite distance.
                for node in list_nodes:
                    node.label = float("Inf")
                start_node.label = 0

                #Edge relaxation algorithm
                for _ in range(len(list_nodes) - 1):
                    for edge in list_edges:
                        if edge.end.is_barrier or edge.start.is_barrier:
                            continue
                        distance = edge.end.weight - edge.start.weight
                        if distance > 0:
                            distance = pow(2,distance) #double if it's uphill: change to exponential?
                        if edge.end.label > edge.start.label + distance:
                            edge.end.label = edge.start.label + distance
                            edge.end.fastest_trace_previous_node = edge.start
                            main_frame.highlight_node(edge.end.fastest_trace_previous_node)
                #Detect negative weight cycle paradoxes
                #for edge in list_edges:
                 #   if edge.end.label > edge.start.label:
                        #print("Negative weight cycle detected")

            bellman_ford(start_node, Edge.edge_list, Node.node_list)
            return self.getPath(end_node)

        #Gets the path. Assumes the graph has already been processed through
        #an algorithm.

        self.function_map = {"Simple Dijkstra": simple_dijkstra,
                             "Bidrectional Dijkstra": bidirectional_dijkstra,
                             "Bellman Fords": bellman_ford_path_gen}

    def getPath(self, end_node):
        node_list = []

        while end_node != None:
            node_list = [end_node] + node_list
            end_node = end_node.fastest_trace_previous_node
        return node_list
