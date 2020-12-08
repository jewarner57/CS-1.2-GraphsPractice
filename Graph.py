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

    def numPreReqs(self, courseName):
        # get the course
        course = self.nodes.get(courseName)
        prereqs = []

        # check if the coursename is valid
        if course is None:
            return "Invalid Course Name"

        # check if course has any prereqs
        if len(course.edges) == 0:
            return None

        # get prereqs
        for prereq in course.edges:

            prereqs.append(prereq)

            nestedPrereq = self.numPreReqs(prereq)
            if nestedPrereq is not None:
                for course in nestedPrereq:
                    prereqs.append(course)

        prereqs = list(dict.fromkeys(prereqs))
        return prereqs
