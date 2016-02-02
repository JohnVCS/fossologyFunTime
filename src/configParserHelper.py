import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("app.conf")

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def getDatabaseInfo():
	database=ConfigSectionMap("database")['database']
	username=ConfigSectionMap("database")['username']
	password=ConfigSectionMap("database")['password']
	return (database,username,password)
def packageInfo():
	packagePath=ConfigSectionMap("package")['path']
	return packagePath
