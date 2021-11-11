import pymongo


def get_database():
    connection_string = "mongodb+srv://<USER>:<PASSWORD>X@cluster0.owcnv.mongodb.net/backup?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_string)
    return client['backup']
