#!/usr/bin/python

import subprocess
import os

 
devnull=open('/dev/null','w')

# creates the temporary directory to store the jar files
def createTempDirectoryIfDoesntExist():
	newpath = r'mydep' 
	if not os.path.exists(newpath):
    		os.makedirs(newpath)

# copies depedencies to folder 
def copyDependencyToTempFolder():
	copyDepCmd=["mvn","dependency:copy-dependencies","-DoutputDirectory=mydep","-Dclassifier=sources"]
	copyDepMvnPluginProcess=subprocess.Popen(copyDepCmd, stdout=devnull)

# creates the graphML
# graphML is one of the supported output type format of Maven
def createGraphMl():
	createGraphMlCommand = ["mvn", "dependency:tree","-DoutputFile=test.graphml", "-DoutputType=graphml"]
	createGraphMlMvnPluginProcess = subprocess.Popen(createGraphMlCommand, stdout=devnull)

# parses graphml file and returns dependency tuples
# basically it shows the parent-child relationship in a sort of like a pair
def parseGraphMl():
	import networkx
	import os.path
	import time
	
	# graph is an oject imported by networkx
	graph=networkx.read_graphml("test.graphml")
	
	# optional argument data="NodeLabel" since that is what we need
	# nodes grabs all the nodes and nodelabel, and then returns a set of tuples
	# dict changes the comma to colon so we can grab the id's and labels
	# essentially, the purpose is to map the node-id to package name 
	nodesDict=dict(graph.nodes(data="NodeLabel"))
	# print(dict(graph.nodes(data="NodeLabel")))
	edgeLabels=[]
	for e1,e2 in graph.edges():
		edgeLabels.append((nodesDict[e1]['label'],nodesDict[e2]['label']))
	return edgeLabels

# main method
if __name__ == '__main__':
	#createTempDirectoryIfDoesntExist()
	#copyDependencyToTempFolder()

	createGraphMl()

	while not os.path.exists("test.graphml"):
	    time.sleep(1)

	edgeLabels=parseGraphMl()
	for e in edgeLabels:
		print e
