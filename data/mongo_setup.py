import os
import json
import mongoengine

def get_mongo_credentials():
    configPath = os.path.dirname(__file__) + "/configfile.json"
    with open(configPath) as json_file: #Print the config file json
        data = json.load(json_file)
        return data

crendentials = get_mongo_credentials()

db_uri = "mongodb+srv://%s:%s@nominasystemrodwel-rj63p.mongodb.net/test?retryWrites=true&w=majority" % (crendentials["username"], crendentials["password"])

def global_init():
    mongoengine.connect(host=db_uri)
    print("Mongo Connection Done")


