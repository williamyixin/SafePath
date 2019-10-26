from node import Node
import heapq

def __init__(self, main_frame):
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