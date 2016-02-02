#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","tangina4","fossologyDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO FILE_LICENSES(FileName, Licenses) \
       VALUES ('%s', '%s')" % \
       ('John', 'Jesse')

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
