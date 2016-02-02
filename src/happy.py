#!/usr/bin/python

#It's working
import subprocess
import crudHelper
import configParserHelper 


def stdOutOfNomos():
	packageConf=configParserHelper.packageInfo()
	nomosProcess=subprocess.Popen(["/usr/share/fossology/nomos/agent/nomos" ,"-d",packageConf], stdout=subprocess.PIPE)
	deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)
	end_of_pipe=deleteFirst4LinesProcess.stdout
	return end_of_pipe


for line in stdOutOfNomos():
	splitline=line.strip().split()
	#print splitline
	try:
		filename=splitline[1]
		licenses=",".join(splitline[4:])
		print "filename", filename
		print "licenses", licenses 
		crudHelper.insertFilenameLicenses(filename,licenses)
	except IndexError:
		print "index error", splitline
