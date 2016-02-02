#!/usr/bin/python

#It's working
import subprocess
import MySQLdb
import configParserHelper 

# function
def insertFilenameLicenses(filename,licenses):
	# Open database connection
	dbconfig=configParserHelper.getDatabaseInfo()
	db = MySQLdb.connect("localhost",dbconfig[1],dbconfig[2],dbconfig[0])

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO FILE_LICENSES(FileName, Licenses) \
	       VALUES ('%s', '%s')" % \
	       (filename, licenses)

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()

packageConf=configParserHelper.packageInfo()
nomosProcess=subprocess.Popen(["/usr/share/fossology/nomos/agent/nomos" ,"-d",packageConf], stdout=subprocess.PIPE)
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
		insertFilenameLicenses(filename,licenses)
	except IndexError:
		print "index error", splitline
