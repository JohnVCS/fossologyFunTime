import networkx as nx
import matplotlib.pyplot as plt
G=nx.drawing.nx_agraph.read_dot("depmetadata.dot")
print G.nodes()
