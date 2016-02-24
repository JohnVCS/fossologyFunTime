# fossologyFunTime

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
