import networkx

graph=networkx.read_graphml("test.graphml")
for n,nbrs in graph.adjacency_iter():
	print n,nbrs
	for nbr,eattr in nbrs.items():
		print nbr,eattr
		#data=eattr['weight']
		#if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))
print graph.graph
print graph.nodes(data=True)
