import MySQLdb
import configParserHelper 

def insertFilenameLicenses(args,filename,licenses):
	# Open database connection
	dbconfig=configParserHelper.getDatabaseInfo()
	db = MySQLdb.connect("localhost",args.username,args.password,args.database)

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