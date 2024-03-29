
class Node:

    node_list = []
    node_size = 15
    node_height = int(node_size*0.866)

    max_weight = 5

    def __init__(self, label, connections = [], x = 0, y = 0, flipped = False):

        # self.label refers to the id of the node
        # self.connections is a list of all Edges this node is connected to
        self.label = label
        self.connections = connections
        self.is_barrier = False

        self.is_start = False
        self.is_end = False
        self.is_highlighted = False
        self.x = x
        self.y = y
        self.weight = 0
        self.flipped = flipped
        self.fastest_trace_previous_node = None

        self.center_x = x + Node.node_size//2
        if self.flipped:
            self.center_y = y + Node.node_height//3
        else:
            self.center_y = y + 2*Node.node_height//3


        if self.flipped:
            self.triangle_poly = [x, y, int(x + Node.node_size/2), y + Node.node_height, x + Node.node_size, y]
        else:
            self.triangle_poly = [x, y + Node.node_height, int(x + Node.node_size/2), y, x + Node.node_size,
                                  y + Node.node_height]

    # Relative weight of the node (if needed)
    def relative_weight(self):
        return self.weight/self.max_weight

    # Draws the node on the passed canvas
    def draw_node(self, canvas):
        rel_weight = self.relative_weight()
        color = fill='#{:02x}{:02x}{:02x}'.format(int(70 + rel_weight * 180),
                                                                      int(50 + rel_weight * 180),
                                                                      int(rel_weight * 180))
        if self.is_barrier:
            color='blue'
        elif self.is_start:
            color = 'red'
        elif self.is_end:
            color = 'green'

        ## canvas.create_rectangle(self.x, self.y, self.x + Node.node_size, self.y + Node.node_size, fill=color)
        if self.is_highlighted:
            canvas.create_polygon(self.triangle_poly, fill=color, outline='red', width = 2)
        else :
            canvas.create_polygon(self.triangle_poly, fill = color, outline = 'black')

    def contains(self, mouse_x, mouse_y):
        return self.isInside(self.triangle_poly[0], self.triangle_poly[1], self.triangle_poly[2], self.triangle_poly[3]
                             , self.triangle_poly[4], self.triangle_poly[5], mouse_x, mouse_y)

    def isInside(self, x1, y1, x2, y2, x3, y3, x, y):
        if (self.area(x1, y1, x2, y2, x3, y3) == self.area(x, y, x2, y2, x3, y3) + self.area(x1, y1, x, y, x3, y3)
                + self.area(x1, y1, x2, y2, x, y)):
            return True
        else:
            return False

    def area(self, x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def increase_weight(self):
        self.weight = min(self.weight+1, 5)
        self.update_edge_weight()

    def update_edge_weight(self):
        for edge in self.connections:
            #edge.weight = abs(edge.start.weight - edge.end.weight)
            edgeDiff = edge.start.weight - edge.end.weight
            gradient = abs(edgeDiff) / (1.717 / 3 * 1)

            riskfactor = (4.966 * gradient + 143.9)/143.9
            edge.weight = riskfactor

    def reset(self):
        self.weight = 0
        self.is_barrier = False
        self.is_highlighted = False
        self.is_start = False
        self.is_end = False

    def highlight_edge(self, canvas, other):
        canvas.create_line(self.center_x, self.center_y, other.center_x, other.center_y, fill='green', width=2)

    def highlight_all_edges(self, canvas):
        for edge in self.connections:
            self.highlight_edge(canvas, edge.end)