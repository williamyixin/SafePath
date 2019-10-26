from node import Node
import heapq


class Algorithms:

    def __init__(self, main_frame):
        # William, format your functions like this

        def simple_dijkstra(start_node, end_node): #only returns the dictionary of distances so far

            # call "main_frame.highlight_node(node)" to highlight a node
            main_frame.highlight_node(start_node)

            # Actual Dijkstra's stuff
            priority_queue, node_list = [(0, start_node)], Node.node_list[:]
            distances = {i : float('inf') for i in node_list}
            distances[start_node] = 0
            # Finds node with the smallest distance value
            while priority_queue:
                current_distance, current_vertex = heapq.heappop(priority_queue)
                if current_distance < distances[current_vertex]:
                    neighbors = [i for i in node_list if i is current_vertex][0].connections
                    for n in neighbors:
                        distance = current_distance + n.weight
                        if distance < distances[n]:
                            distances[n] = distance
                            heapq.heappush(priority_queue, (distance, n))
            return distances

        def bidirectional_dijkstra(start_node, end_node):
            return []

        def bellman_ford_path_gen(start_node, end_node):


            def bellman_ford(start_node, list_edges, list_nodes):
                #Initializing all the node labels except for the start node
                #as having infinite distance.
                for node in list_nodes:
                    node.label = float("Inf");
                start_node.label = 0

                #Edge relaxation algorithm
                for edge in list_edges:
                    distance = edge.end.weight - edge.start.weight
                    if distance > 0:
                        distance = pow(2,distance) #double if it's uphill: change to exponential?
                    if edge.end.label > edge.start.label + distance:
                        edge.end.label = edge.start.label + distance
                        edge.fastest_trace_previous_node = edge.start
                #Detect negative weight cycle paradoxes
                for edge in list_edges:
                    if edge.end.label > edge.start.label:
                        print("Negative weight cycle detected")

            return self.getPath(end_node)

        #Gets the path. Assumes the graph has already been processed through
        #an algorithm.

        self.function_map = {"Simple Dijkstra": simple_dijkstra,
                             "Bidrectional Dijkstra": bidirectional_dijkstra,
                             "Bellman Fords": bellman_ford_path_gen}

    def getPath(end_node):
        if end_node.fastest_trace_previous_node:
            return getPath(end_node.fastest_trace_previous_node) + [end_node]
        return [end_node]