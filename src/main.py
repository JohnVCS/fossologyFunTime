#!/usr/bin/python

#It's working
import subprocess
import crudHelper
import configParserHelper 
import argumentParserHelper


def stdOutOfNomos(directory):
	nomoscmd=["/usr/share/fossology/nomos/agent/nomos" ,"-d",directory]
	nomosProcess=subprocess.Popen(nomoscmd, stdout=subprocess.PIPE)
	deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)
	end_of_pipe=deleteFirst4LinesProcess.stdout
	return end_of_pipe 


args=argumentParserHelper.arguments()
print stdOutOfNomos(args.directory)
for line in stdOutOfNomos(args.directory):
	splitline=line.strip().split()
	try:
		filename=splitline[1]
		licenses=",".join(splitline[4:])
		print "filename", filename
		print "licenses", licenses 
		crudHelper.insertFilenameLicenses(args,filename,licenses)
	except IndexError:
		print "index error", splitline