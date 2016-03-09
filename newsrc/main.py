import subprocess
import os
 
#creates directory
newpath = r'mydep' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

#copies depedencies to folder 
copyDepCmd=["mvn","dependency:copy-dependencies","-DoutputDirectory=mydep","-Dclassifier=sources"]
copyDepMvnPluginProcess=subprocess.Popen(copyDepCmd, stdout=None)


#deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)
#end_of_pipe=deleteFirst4LinesProcess.stdout
#return end_of_pipe 

