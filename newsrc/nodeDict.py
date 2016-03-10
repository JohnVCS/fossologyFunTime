import networkx

graph=networkx.read_graphml("test.graphml")
nodesDict=dict(graph.nodes(data="NodeLabel"))
edgeLabels=[]
for e1,e2 in graph.edges():
	edgeLabels.append((nodesDict[e1]['label'],nodesDict[e2]['label']))

print edgeLabels
