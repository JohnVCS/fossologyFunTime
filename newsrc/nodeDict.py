import networkx

graph=networkx.read_graphml("test.graphml")
nodesDict=dict(graph.nodes(data="NodeLabel"))
for e1,e2 in graph.edges():
	print (nodesDict[e1]['label'],nodesDict[e2]['label'])

