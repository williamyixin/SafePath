
import sys
from node import Node

class IOManager:

    def __init__(self):
        self.elevation_data = [[]]

    # node_list passed is a two-dimensional array
    def set_nodes_list(self, node_list):
        self.node_list = node_list

    def read_elevation_data(self, path):
        file = open(path, "r")
        data_point_info = None

        max = -1

        for data_point in file:
            data_point_info = data_point.split(" ")
            self.node_list[int(data_point_info[1])][int(data_point_info[0])].weight = int(data_point_info[2])
            self.elevation_data.append(Point(data_point_info[0], data_point_info[1]))

            if int(data_point_info[2]) > max:
                max = int(data_point_info[2])
        Node.max_weight = max




class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

