from Graph import Graph

graph = Graph()
graph.jsonToGraph('./classlist.json')


def getPrereqInfo(className):
    print("Class: " + className)
    print("Num Prereqs: " + str(graph.numPreReqs(className)))
    print("Prereq List: " + str(graph.listPrereqs(className)))


getPrereqInfo("FEW 2.3")
