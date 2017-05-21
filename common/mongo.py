import pymongo
import sys
import os

sys.path.append(os.path.split(os.path.realpath(__file__))[0]+"/../../")
from config import config

db_conn = pymongo.MongoClient(config['testing'].MONGODB_DATABASE_URI)
xqseccenter_db = getattr(db_conn,config['testing'].MONGODB_DBNAME)
