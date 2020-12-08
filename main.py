from Graph import Graph

graph = Graph()
graph.jsonToGraph('./classlist.json')

print(graph.nodes)

print(graph.numPreReqs("FEW 2.3"))

# for id in graph.nodes:
#     print(id + ":")
#     edges = graph.nodes[id].get_edges()
#     for edge in edges:
#         print("  " + edges[edge].id)
#     print("----------------")
