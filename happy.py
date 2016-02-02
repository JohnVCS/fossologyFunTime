import subprocess

nomosProcess=subprocess.Popen(["/usr/share/fossology/nomos/agent/nomos" ,"-d","openssl-1.0.2e/"], stdout=subprocess.PIPE)
deleteFirst4LinesProcess=subprocess.Popen(["sed" ,"1,4d"], stdin=nomosProcess.stdout,stdout=subprocess.PIPE)

end_of_pipe=deleteFirst4LinesProcess.stdout

for line in end_of_pipe:
	splitline=line.strip().split()
	#print splitline
	try:
		filename=splitline[1]
		licenses=",".join(splitline[4:])
		print "filename", filename
		print "licenses", licenses 
	except IndexError:
		print "index error", splitline
