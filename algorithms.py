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

        self.function_map = {"Simple Dijkstra": simple_dijkstra,
                             "Bidrectional Dijkstra": bidirectional_dijkstra}