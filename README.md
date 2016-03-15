# fossologyFunTime

## System Description
  Maven allows the ability to get the transitive dependency hierarchy metadata from a POM.xml file.  It also has the ability to grab transitive dependencies from maven central.  These two features will be invoked using our python script.  The transitive dependencies will be placed into a temporary directory to be scanned by DoSOCSv2, and the transitive dependency hierarchy metadata will passed to a DoSOCSv2 Maven Dependency plugin which will facilitate DoSOCSv2’s ability to persist the HAS_PREREQUISITE and PREREQUISITE_FOR relationships defined in the relationship_types SPDX schema.

## Development Environment
OS 
 * (John)   -  Ubuntu 14.04 
 * (Jesse)  -  Ubuntu Gnome 15.10
 
IDE
* Eclipse/Pydev

Language(s)
* Python 2.7.x

Dependency
* Maven 3.3.3 - https://gist.github.com/ervinb/34203f0cc54c1e7f982b (Link on how to install for ubuntu 14.04 - You also need to create a directory called .semaphore-cache)

## Communication Management Plan
Your Team -
Jesse and John communicate through phone/email and in person. We are both taking the same classes currently, and we schedule a face-to-face meeting at PKI every weekend. In addition, we are also using Github's issue tracker as another means of communication.

* Your Community 
  * irc
    * freenode
      * #spdx
* DoSOCSv2
  * Thomas T Gurney <ttg@tuta.io>  
* SPDX

## Data Flow Diagram of the System
!["Data Flow Diagram"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/dataFlowDiagram.png)

## DoSOCSv2 Schema
!["DoSOCSv2 Schema"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/SchemaDiagramDoSocs.png)
!["DoSOCSv2 Schema Partial"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/schemaPartial.png)

## Dependencies
DoSOCSv2 - https://github.com/DoSOCSv2/DoSOCSv2

networkx



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
