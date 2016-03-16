# fossologyFunTime

## System Description

  fossologyFunTime is a tool that provides features that will be merged into DoSOCSv2 to persist depedency information in the DoSOCSv2 database.

  fossologyFunTime works by accepting a POM.xml file and the project artifact from a user. The POM.xml is passed to a python script that uses Maven. Maven allows the ability to get the transitive dependency hierarchy metadata from the passed POM.xml file. It also has the ability to grab transitive dependencies from maven central.  These two features will be invoked using our python script.  The transitive dependencies will be placed into a temporary directory to be scanned by DoSOCSv2, and the transitive dependency hierarchy metadata will passed to a DoSOCSv2 Maven Dependency plugin which will facilitate DoSOCSv2’s ability to persist the HAS_PREREQUISITE and PREREQUISITE_FOR relationships defined in the relationship_types SPDX schema.
  
Eventually fossologyFunTime will be merged with the DOSOCSv2 project.  It'll work in series of steps.  First the project will be scaned by DoSOCS and a document will be generated.  From here DoSOCSv2 will request the depedency source archieves into a temporary directory.  The depedency source archives will be scanned and documents will be created for them.  After all the documents are created the depedency hierarchy metadata will be persisted in it's affiliated document via package identifiers.  These depedency relationships will be seen at the project artifact document via external document references.

### Atribution for implementation ideas
Thomas T Gurney helped in the decision to use external document references to get depedency relationships across different namespaces. 

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

## use case
        title
                developer submitting something....
        primary actor
                external entity - developer
        goal in context
                lines up with title
                "to record depedency tree structure" and identify packages
        stakeholders and interests
                decision maker/manager who want's to see spdx information
        preconditions
          valid pom file and prebuilt artifact
          proper connections with dosocs db and maven central
        success scenario
                tree information in the database
        failed end condition
                can't connect to maven central
                can't connect to dosocs
                non-valid pom
        trigger
                pom.xml
        Notes:
                don't worry about it

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
!["Data Flow Diagram"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/Diagram2.png)

## DoSOCSv2 Schema
!["DoSOCSv2 Schema"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/SchemaDiagramDoSocs.png)
!["DoSOCSv2 Schema Partial"](https://raw.githubusercontent.com/JohnVCS/fossologyFunTime/master/SchemaAndDataFlowImages/schemaPartial.png)

## Use Case

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
