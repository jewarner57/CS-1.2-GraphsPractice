from Graph import Graph

graph = Graph()
graph.jsonToGraph('./classlist.json')

print(graph.nodes)

for id in graph.nodes:
    print(id + ":")
    edges = graph.nodes[id].get_edges()
    for edge in edges:
        print("  " + edges[edge].id)
    print("----------------")
