class Vertex:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data

        # dictionary of vertices I connect to
        # id: vertex object
        self.edges = {}

    def add_edge(self, vert):
        self.edges[vert.id] = vert

    def get_edges(self):
        return self.edges
