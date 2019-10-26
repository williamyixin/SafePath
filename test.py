from node import Node
from collections import deque

def __init__(self, main_frame):
    def simple_dijkstra(start_node, end_node): #only returns the dictionary of distances so far

        # call "main_frame.highlight_node(node)" to highlight a node
        main_frame.highlight_node(start_node)

        # Actual Dijkstra's stuff
        node_list = Node.node_list[:]
        distances, previous_nodes = {i : float('inf') for i in node_list}, {i : None for i in node_list}
        distances[start_node] = 0
        nodes = node_list.copy()
                
        while nodes:
            current_node = min(nodes, lambda x: distances[x])
            if distances[current_node] == float('inf'):
                break
            for neighbor in current_node.connections:
                alternative = distances[current_node] + neighbor.weight
                if alternative < distances[neighbor]:
                    distances[neighbor] = alternative
                    previous_nodes[neighbor] = current_node
        nodes.remove(current_node)

        path, current_node = [], end_node
        while previous_nodes[current_node]:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.insert(0, current_node)
        return path

        # Finds node with the smallest distance value
        # while priority_queue:
        #     current_node = min([x for x,y in distances.items()])
        #     if current_node is end_node:
        #         return distances[current_node]
        #     for neighbor in current_node.connections:
        #         distance = neighbor.weight - current_node.weight
        #         if distance < distances[neighbor]:
        #             distances[neighbor] = distance
        #             priority_queue += (distance, neighbor)