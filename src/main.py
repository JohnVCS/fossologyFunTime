#!/usr/bin/python

# Copyright (C) 2016 Jesse Moseman, and John Carlo B. Viernes IV
#
# This file is part of fossologyFunTime.
#
# fossologyFunTime is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# fossologyFunTime is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fossologyFunTime.  If not, see <http://www.gnu.org/licenses/>.

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
if args.create:
	crudHelper.createTable(args)	
	
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
