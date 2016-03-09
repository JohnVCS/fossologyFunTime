import networkx as nx
import matplotlib.pyplot as plt
G=nx.drawing.nx_agraph.read_dot("depmetadata.dot")
#print G.nodes()
#print G.successors(1)
for n in G.nodes_iter():
	print (n,G.successors(n))

