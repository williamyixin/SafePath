from node import Node


class Algorithms:

    def __init__(self, main_frame):
        # William, format your functions like this

        def simple_dijkstra(start_node, unvisited_nodes):

            # call "main_frame.highlight_node(node)" to highlight a node
            main_frame.highlight_node(start_node)

            # Actual Dijkstra's stuff
            start_node.label = 0
            curr_smallest_node = None
            while len(unvisited_nodes):
                # Finds node with the smallest distance value
                for node in unvisited_nodes:  #
                    if node.label < curr_smallest_node.label:
                        curr_smallest_node = node

            def dijkstra(curr_node, unvisited_nodes):
                if all([node.visited for node in unvisited_nodes]):
                    return

            print("hi")
            return []

        def bidirectional_dijkstra(start_node, end_node):
            return []

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

        #Gets the path. Assumes the graph has already been processed through
        #an algorithm.
        def getPath(end_node):
            if end_node.fastest_trace_previous_node:
                return getPath(end_node.fastest_trace_previous_node) + [end_node]
            return [end_node]




        self.function_map = {"Simple Dijkstra": simple_dijkstra,
                             "Bidrectional Dijkstra": bidirectional_dijkstra}