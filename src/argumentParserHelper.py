#!/usr/bin/python
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
