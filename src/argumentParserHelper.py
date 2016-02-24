#!/usr/bin/python

# Copyright (C) 2015 Jesse Moseman, and John Carlo B. Viernes IV
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


import argparse
import configParserHelper
#./happy.py -d directoryPackage -u name -p password

def arguments():
    #returns database, username, and password as a tuple(immutable array)
    dbInfo = configParserHelper.getDatabaseInfo() 
    #returns path of package(i.e. directory)
    packageInfo = configParserHelper.packageInfo()
     
    parser = argparse.ArgumentParser(description="processes licenses and throws into DB")
    parser.add_argument('-db', '--database',
                        help='database name',
                        default=dbInfo[0])
    parser.add_argument('-d', '--directory',
                        help='directory path to package',
                        default=packageInfo)
    parser.add_argument('-u', '--username',
                        help='your username',
                        default=dbInfo[1])
    parser.add_argument('-p', '--password',
                        help='your password',
                        default=dbInfo[2])
    parser.add_argument('-c', '--create', action="store_true",
			help='create database and run the script',
			default=False)
    args = parser.parse_args()
    return args
#     print(args.directory)
#     print(args.username)
#     print(args.password)
