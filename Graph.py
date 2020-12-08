from Vertex import Vertex
import json


class Graph:
    def __init__(self):
        self.nodes = {}

    def addVertex(self, vertex):
        self.nodes[vertex.id] = vertex

    def jsonToGraph(self, filepath):
        #  get json -> dictionary
        with open(filepath) as f:
            schedule = json.load(f)

        # loop through all classes in the list
        for MSclass in schedule:
            newVertex = Vertex(MSclass["name"])
            self.addVertex(newVertex)

            # loop through all prereqs and add them as edges
            for prereq in MSclass["prerequisites"]:
                self.nodes.get(MSclass.get("name")).add_edge(
                    self.nodes.get(prereq))
