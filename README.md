# fossologyFunTime

## System Description
  Maven allows the ability to get the transitive dependency hierarchy metadata from a POM.xml file.  It also has the ability to grab transitive dependencies from maven central.  These two features will be invoked using our python script.  The transitive dependencies will be placed into a temporary directory to be scanned by DoSOCSv2, and the transitive dependency hierarchy metadata will passed to a DoSOCSv2 Maven Dependency plugin which will facilitate DoSOCSv2’s ability to persist the HAS_PREREQUISITE and PREREQUISITE_FOR relationships defined in the relationship_types SPDX schema.

## Development Environment

OS 
 * (John)   -  Ubuntu 14.04 ; 
 * (Jesse)  -  Ubuntu Gnome 15.10 ;
IDE
* Eclipse/Pydev

## Communication Management plan
Your Team
Jesse and John communicate through phone/email and in person. We are both taking the same classes currently, and we schedule a face-to-face meeting at PKI every weekend.

* Your Community 
  * irc
    * freenode
    * #spdx
* irc.oftc.net
  * #fossology

* DoSOCSv2
* SPDX
* fossology
* http://www.fossology.org/projects/fossology/wiki/Contact_Us
* Linux Foundation



## install dependencies
```bash
sudo apt-get install libmysqlclient-dev python-dev python-setuptools
sudo easy_install MySQL-python
```

## database schema
```sql
CREATE TABLE FILE_LICENSES
(
  FileName VARCHAR(255), 
  Licenses VARCHAR(255)
);

```

##google doc
https://docs.google.com/document/d/1xuFlnHZnXJlvCpfcOzlIjIB5OAP9E_8FbCU4mbE0tp4/edit

##Usage
```python
usage: main.py [-h] [-db DATABASE] [-d DIRECTORY] [-u USERNAME] [-p PASSWORD]

processes licenses and throws into DB

optional arguments:
  -h, --help            show this help message and exit
  -db DATABASE, --database DATABASE
                        database name
  -d DIRECTORY, --directory DIRECTORY
                        directory path to package
  -u USERNAME, --username USERNAME
                        your username
  -p PASSWORD, --password PASSWORD
                        your password
```

##License and Copyright

Copyright © 2016 Jesse Moseman, and John Carlo B. Viernes IV

fossologyFunTime is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution 4.0 International (CC BY 4.0) license. 
