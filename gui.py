
from node import Node
from styles import *
from threading import Thread
from algorithms import Algorithms
from edge import Edge

from reader import IOManager

import sys

import time

#######
# GUI #
#######

class MainFrame(Frame):

    #########################
    # Widget Initialization #
    #########################

    def __init__(self, parent, load_path = None, node_width = 20, node_height = 40, img_path = None):
        super().__init__(parent)

        self.node_width = node_width
        self.node_height = node_height
        self.frame_width = self.node_width*Node.node_size - Node.node_size//2
        self.frame_height = (self.node_height*Node.node_height)//2

        self.add_barriers = False
        self.mark_start = False
        self.mark_end = False
        self.start_node = None
        self.end_node = None

        self.finding_path = False

        self.pack(fill=BOTH)
        self.parent = parent

        self.init_algorithms()
        self.init_components(parent)
        self.init_grid()

        self.io_manager = IOManager()
        self.io_manager.set_nodes_list(self.node_grid)
        self.io_manager.read_elevation_data(load_path)

        self.draw_grid()

        self.update()



    #########################
    # Algorithm Initialization #
    #########################

    def init_algorithms(self):
        self.algorithms = Algorithms(self)


    #########################
    # Widget Initialization #
    #########################

    def init_components(self, root):
        self.grid_frame = Frame(self.pack()).pack()

        Label(self.grid_frame, text="Select block type : ").pack(side=LEFT)

        self.block_types_combobox = ttk.Combobox(self.grid_frame, state="readonly"
                                                 , values=["Regular", "Barrier", "Start", "End"])
        self.block_types_combobox.current(0)
        self.block_types_combobox.pack(side=LEFT)

        def select_block_type(event):
            if self.block_types_combobox.get() == "Barrier":
                self.add_barriers = True
                self.mark_start = False
                self.mark_end = False
            elif self.block_types_combobox.get() == "Start":
                self.add_barriers = False
                self.mark_start = True
                self.mark_end = False
            elif self.block_types_combobox.get() == "End":
                self.add_barriers = False
                self.mark_start = False
                self.mark_end = True
            elif self.block_types_combobox.get() == "Regular":
                self.add_barriers = False
                self.mark_start = False
                self.mark_end = False

        self.block_types_combobox.bind("<<ComboboxSelected>>", select_block_type)

        # Add Algorithm Select combobox
        Label(self.grid_frame, text="Select algorithm : ").pack(side=LEFT)
        self.graph_algorithms = ttk.Combobox(self.grid_frame, values=list(self.algorithms.function_map.keys()))
        self.graph_algorithms.current(2)
        self.graph_algorithms.pack(side=LEFT)

        # Add Start Paths Button
        def start_path_finder():
            self.finding_path = True
            self.path_finder_button.configure(state="disabled")
            self.clear_grid_button.configure(state="disabled")
            def path_finder():
                path_list = self.algorithms.function_map[self.graph_algorithms.get()](self.start_node, self.end_node)

                for row in self.node_grid:
                    for node in row:
                        node.is_highlighted = False

                self.draw_grid()

                print(len(path_list))
                for i in range(len(path_list) - 1):
                    path_list[i].highlight_edge(self.canvas, path_list[i+1])
                    print(path_list[i].center_x)
                self.canvas.update()
                self.finding_path = False
                self.path_finder_button.configure(state="normal")
                self.clear_grid_button.configure(state="normal")

            self.current_thread = Thread(target=path_finder)
            self.current_thread.start()

        self.path_finder_button = Button(self.grid_frame, text="Start Path Finder",
                                         command=start_path_finder).pack(side=LEFT, padx=(10, 0))

        # Add Clear Grid button
        def clear_grid():
            for row in self.node_grid:
                for node in row:
                    node.reset()
            self.start_node = None
            self.end_node = None
            self.draw_grid()
            self.update()

        self.clear_grid_button = Button(self.grid_frame, text="Clear Grid", command=clear_grid)
        self.clear_grid_button.pack(side=LEFT, padx=(10, 0))


        # Create instance of Canvas and add to main Frame

        self.canvas = Canvas(self, width=self.frame_width, height=self.frame_height, bg='white')
        self.canvas.pack(side=BOTTOM)



        # Handling mouse events

        def mouse_drag(event):
            self.add_weights(event.x, event.y)

        def mouse_press(event):
            self.passed_nodes = []
            self.add_weights(event.x, event.y)

        self.canvas.bind("<B1-Motion>", mouse_drag)
        self.canvas.bind("<Button-1>", mouse_press)

    def init_grid(self):
        self.node_grid = []
        node = None
        for y in range(self.node_width):
            self.node_grid.append([])
            for x in range(self.node_height):
                node = Node(str(x) + " " + str(y), [], (x-1)*Node.node_size//2
                                              , (y)*Node.node_height, x%2 == y%2)
                self.node_grid[y].append(node)
                Node.node_list.append(node)

        # Create connections
        grid = self.node_grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j != len(grid[i])-1:
                    grid[i][j].connections.append(Edge(grid[i][j], grid[i][j+1]))
                if j != 0:
                    grid[i][j].connections.append(Edge(grid[i][j], grid[i][j-1]))
                if grid[i][j].flipped and i > 0:
                    grid[i][j].connections.append(Edge(grid[i][j], grid[i-1][j]))
                if not grid[i][j].flipped and i < len(grid) - 1:
                    grid[i][j].connections.append(Edge(grid[i][j], grid[i + 1][j]))
                Edge.edge_list.extend(grid[i][j].connections)




    def highlight_node(self, node):
        node.is_highlighted = True
        node.draw_node(self.canvas)
        self.canvas.update()

    def draw_grid(self):
        for row in self.node_grid:
            for node in row:
                node.draw_node(self.canvas)

    def add_weights(self, x, y):
        if self.finding_path:
            return

        # search for selected node
        # iterates through each node and determine if mouse_x and mouse_y is in the node
        selected_node = None
        for row in self.node_grid:
            for node in row:
                if node.contains(x, y):
                    selected_node = node
                    break


        # check if the selected node has already been selected
        if selected_node is not None and selected_node not in self.passed_nodes:
            if not selected_node.is_barrier and not self.add_barriers and not self.mark_start and not self.mark_end:
                selected_node.increase_weight()

            # only one node can be marked as the starting node
            if self.mark_start:
                if self.start_node is not None:
                    self.start_node.is_start = False
                    self.start_node.draw_node(self.canvas)
                self.start_node = selected_node
                selected_node.is_start = self.mark_start

            # only one node can be marked as the end node
            elif self.mark_end:
                if self.end_node is not None:
                    self.end_node.is_end = False
                    self.end_node.draw_node(self.canvas)
                self.end_node = selected_node
                selected_node.is_end = self.mark_end
            else:
                selected_node.is_barrier = self.add_barriers
                self.passed_nodes.append(selected_node)

            selected_node.draw_node(self.canvas)
            self.update()


    def destroy(self):
        """Overrides the destroy method to end the current game."""
        super().destroy()
        exit(1)


def run_GUI(args=[]):
    """Start the GUI.

    computer -- True if playing against computer
    """
    root = Tk()
    root.title('Path Generator')
    root.minsize(800, 600)
    root.geometry("520x600")

    if len(args) == 3:
        app = MainFrame(root, None, int(args[1]), int(args[2]), None)
    if len(args) == 1:
        app = MainFrame(root, str(args[1]), int(args[2]), int(args[3]), str(args[4]))
    else:
        app = MainFrame(root)
    root.mainloop()


##########################
# Command Line Interface #
##########################

def run():
    run_GUI(sys.argv)

if __name__ == '__main__':
    run()









