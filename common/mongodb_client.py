''' python module that connect to mongodb '''

from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = '27017'
DB_NAME = 'tap-news'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))


def get_db(database=DB_NAME):
    ''' connect to mongodb '''
    return client[database]
