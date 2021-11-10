import pymongo


def get_database():
    connection_string = "mongodb://localhost:27017/backup"
    client = pymongo.MongoClient(connection_string)
    return client['backup']
