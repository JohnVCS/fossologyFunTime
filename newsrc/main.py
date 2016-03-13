import subprocess
import os

 
devnull=open('/dev/null','w')

# creates the temporary directory to store the jar files
def createTempDirectory():
	newpath = r'mydep' 
	if not os.path.exists(newpath):
    		os.makedirs(newpath)

# copies depedencies to folder 
def copyDependencyToTempFolder():
	copyDepCmd=["mvn","dependency:copy-dependencies","-DoutputDirectory=mydep","-Dclassifier=sources"]
	copyDepMvnPluginProcess=subprocess.Popen(copyDepCmd)

# creates the graphML
# graphML is one of the supported output type format of Maven
def createGraphMl():
	createGraphMlCommand = ["mvn", "dependency:tree","-DoutputFile=test.graphml", "-DoutputType=graphml"]
	createGraphMlMvnPluginProcess = subprocess.Popen(createGraphMlCommand, stdout=devnull)

#deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)
#end_of_pipe=deleteFirst4LinesProcess.stdout
#return end_of_pipe 

if __name__ == '__main__':
	createGraphMl()

