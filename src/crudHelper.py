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
#
# SPDX-License-Identifier: GPL-2.0+

import MySQLdb
import configParserHelper 

def insertFilenameLicenses(args,filename,licenses):
	# Open database connection
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


def createTable(args):
	# Open database connection
	db = MySQLdb.connect("localhost",args.username,args.password,args.database)

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Drop table if it already exist using execute() method.
	# cursor.execute("DROP TABLE IF EXISTS FILE_LICENSES")

	# Create table as per requirement
	sql = """
	CREATE TABLE FILE_LICENSES
	(
  		FileName VARCHAR(255), 
  		Licenses VARCHAR(255)
	);
	"""
	cursor.execute(sql)

	# disconnect from server
	db.close()
