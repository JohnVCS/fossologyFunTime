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
def parseGraphMl():
	import networkx
	import os.path
	import time

	graph=networkx.read_graphml("test.graphml")
	nodesDict=dict(graph.nodes(data="NodeLabel"))
	edgeLabels=[]
	for e1,e2 in graph.edges():
		edgeLabels.append((nodesDict[e1]['label'],nodesDict[e2]['label']))
	return edgeLabels



#deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)
#end_of_pipe=deleteFirst4LinesProcess.stdout
#return end_of_pipe 

if __name__ == '__main__':
	#createTempDirectoryIfDoesntExist()
	#copyDependencyToTempFolder()

	createGraphMl()

	while not os.path.exists("test.graphml"):
	    time.sleep(1)

	edgeLabels=parseGraphMl()
	for e in edgeLabels:
		print e
